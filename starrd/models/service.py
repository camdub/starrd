from starrd.models import db, User

class Service(object):
    __model__ = None

    def save(self, model):
        db.session.add(model)
        db.session.commit()
        return model


class UserService(Service):
    __model__ = User
