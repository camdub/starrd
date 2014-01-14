import os

from flask import Flask
from flask_assets import Environment
from webassets.loaders import PythonLoader as PythonAssetsLoader

from starrd import assets
from starrd.models import db
from starrd.controllers.main import github

assets_env = Environment()


def create_app(object_name, env="prod"):
    app = Flask(__name__)

    app.config.from_object(object_name)
    app.config['ENV'] = env

    db.init_app(app)
    github.init_app(app)

    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().iteritems():
        assets_env.register(name, bundle)

    from controllers.main import main
    app.register_blueprint(main)

    return app

if __name__ == '__main__':
    env = os.environ.get('APPNAME_ENV', 'prod')
    app = create_app('appname.settings.%sConfig' % env.capitalize(), env=env)
    app.run()
