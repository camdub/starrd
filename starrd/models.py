from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()



tags_table = db.Table('tags',
                      db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                      db.Column('user_repo_id', db.Integer,
                                db.ForeignKey('userrepo.id'))
)


class UserRepo(db.Model):
    __tablename__ = 'userrepo'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    repo_id = db.Column(db.Integer, db.ForeignKey('repository.id'))
    repo = db.relationship("Repository")
    tags = db.relationship('Tag', secondary=tags_table,
                           backref=db.backref('userrepos', lazy='dynamic'))


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))


class Repository(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    language = db.relationship('Language',
                               backref=db.backref('languages', lazy='dynamic'))


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(80))
    name = db.Column(db.String(80))
    color = db.Column(db.String(7))
