import pytest

from skeleton import create_app
from skeleton.database import db as _db

@pytest.fixture(scope='session')
def app(request):
    """Session-wide test `Flask` application."""
    app = create_app('config.TestingConfig')

    ctx = app.app_context()
    ctx.push()

    def tearDown():
        ctx.pop()

    request.addfinalizer(tearDown)
    return app

@pytest.yield_fixture(scope='session')
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""
    _db.init_app(app)
    _db.create_all()

    def teardown():
        _db.drop_all()

    request.addfinalizer(teardown)
    return _db

@pytest.fixture(scope='session')
def connection(db, request):
    connection = db.engine.connect()

    def teardown():
        connection.close()

    request.addfinalizer(teardown)
    return connection

@pytest.fixture(scope='function')
def session(db, connection, request):
    """Creates a new database session for a test."""
    options = dict(bind=connection, binds=None)
    db.session = db.create_scoped_session(options=options)
    db.session.begin(subtransactions=True)

    def teardown():
        db.session.rollback()

    request.addfinalizer(teardown)
    return db.session
