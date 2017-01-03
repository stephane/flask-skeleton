from flask import Flask

__version__ = '0.1'

def create_app(config_object):
    app = Flask(__name__, instance_relative_config=True)

    # Load config
    app.config.from_object(config_object)

    # Load from instance folder
    app.config.from_pyfile('instance.py')

    register_extensions(app)
    register_blueprints(app)
    # register_cli is only called when necessary
    return app

def register_extensions(app):
    from .database import db
    db.init_app(app)

    if app.debug:
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            DebugToolbarExtension(app)
        except ImportError:
            pass

    if app.testing:
        from .response import ContainsResponse
        app.response_class = ContainsResponse

def register_blueprints(app):
    from .items.views import items
    app.register_blueprint(items, url_prefix='/')


def register_cli(app):
    import click

    @app.cli.command(short_help="Initialize the database")
    @click.option('--fixtures/--no-fixtures', 'with_fixtures', default=False, help="load a set of initial fixtures")
    def initdb(with_fixtures):
        click.echo("Create tables of %s" % app.config['SQLALCHEMY_DATABASE_URI'])
        from .database import db
        from .items import data as items_data
        db.create_all()

        if with_fixtures:
            click.echo("Load fixtures...")
            items_data.load(db)

        db.session.commit()

    @app.cli.command(short_help="Display list of URLs")
    def urls():
        print(app.url_map)
