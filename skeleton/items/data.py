from . import models

def load(db):
    items = [
        {'code': 'KNIFE', 'name': 'Knife'},
        {'code': 'SHOVEL', 'name': 'Shovel'},
        {'code': 'BUCKET', 'name': 'Bucket'}
    ]
    for item in items:
        db.session.add(models.Item(**item))
