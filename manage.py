#!/usr/local/bin python
import os

from flask.ext.script import Manager
from starrd.models import Language, db
from starrd import create_app
from requests import get
import yaml

env = os.environ.get('APPNAME_ENV', 'prod')
app = create_app('starrd.settings.%sConfig' % env.capitalize(), env=env)

manager = Manager(app)

@manager.command
def run():
    app.run(debug=True)


@manager.command
def createdb():
    db.create_all()


@manager.command
def seed():
    response = get('https://rawgithub.com/github/linguist/master/lib/linguist/languages.yml')
    linguist = yaml.load(response.text)
    for key in linguist:
        if 'color' in linguist[key]:
            lang = linguist[key]
            if 'aliases' in lang:
                name = lang['aliases'][0]
            else:
                name = key.lower()
            db.session.merge(Language(color=lang['color'], name=name, display_name=key))

    db.session.add(Language(name='none',display_name='None', color='white'))
    db.session.commit()
    print "db seeded"

if __name__ == "__main__":
    manager.run()
