from sqlalchemy.orm import exc as sqlalchemy_exc

from skeleton.database import db

class CRUDMixin(object):
    __table_args__ = {'extend_existing': True}

    @classmethod
    def create(cls, commit=True, **kwargs):
        instance = cls(**kwargs)
        return instance.save(commit=commit)

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def commit(self):
        db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()

    @classmethod
    def get_or_create(cls, defaults=None, **kwargs):
        try:
            return db.session.query(cls).filter_by(**kwargs).one(), False
        except sqlalchemy_exc.NoResultFound:
            if defaults:
                kwargs.update(defaults)
            instance = cls(**kwargs)
            try:
                db.session.add(instance)
                db.session.flush()
                return instance, True
            except sqlalchemy_exc.IntegrityError:
                db.session.rollback()
                return db.session.query(cls).filter_by(**kwargs).one(), True
