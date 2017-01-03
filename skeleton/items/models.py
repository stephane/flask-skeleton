from skeleton.database import db
from skeleton.core.mixins import CRUDMixin


class Item(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(length=24), unique=True)
    name = db.Column(db.String, unique=True)

    def __repr__(self):
        return '%s - %s' % (self.code, self.name)
