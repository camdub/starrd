from flask import current_app, Blueprint, g, request, \
    url_for, redirect, session, json, render_template
from flask.ext.github import GitHub

from starrd.models import User, Language, Repository

main = Blueprint('main', __name__)
github = GitHub()

@main.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = User.query.get(session['user'])


@github.access_token_getter
def token_getter():
    return session['token']


@main.route('/login')
def login():
    return github.authorize()


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/auth')
@github.authorized_handler
def authorized(access_token):
    next_url = request.args.get('next') or url_for('.index')
    if access_token is None:
        return redirect(next_url)

    user = User.query.filter_by(auth_token=access_token).first()
    session['token'] = access_token
    if user is None:
        user = User(username=github.get('user')['login'], auth_token=access_token)
        db.session.add(user)
        db.session.commit()

    session['user'] = user.id
    return redirect(url_for('.private'))


@main.route('/private')
def private():
    results = []
    for repo in github.get('user/starred'):
        list = {f: repo[f] for f in ['full_name',
                                             'description',
                                             'id',
                                             'language']}
        r = Repository.query.get(repo['id'])
        l = Language.query.filter_by(display_name=repo['language']).first()
        if l is None:
            l = Language.query.filter_by(name='none').first()
        list['color'] = l.color

        if r is None:
            r = Repository(language=l, id=repo['id'])
            db.session.commit()
        u = User.query.get(session['user'])
        db.session.merge(UserRepo(user=u, repo=r))
        results.append(list)

    db.session.commit()
    return render_template('repos.html', repos=results)

@main.route('/languages')
def languages():
    return json.dumps([{'text': f.name, 'value': str(f.name).lower()}
                       for f in Language.query.all()])
