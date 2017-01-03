Flask Skeleton
==============

Skeleton of a Flask application using SQLAlchemy, pytest and advanced settings management.


Install
-------

    $ pip install -r requirements_dev.txt -e .

Create a PostgreSQL DB called 'skeleton' or tweak config via 'instance/instance.py' file.

    $ export FLASK_APP=dev
    $ flask initdb --fixtures

Run
---

There are files called dev.py and prod.py in root directory:

    $ export FLASK_APP=dev
    $ flask run

To run tests
------------

    $ ./setup.py test
    $ py.test --durations=3 -s --pdb
