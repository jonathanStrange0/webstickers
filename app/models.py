from app import db

class Collection(db.Model):
    __tablename__ = 'collection'
    id = db.Column(db.Integer, primary_key=True)
    collection_name = db.Column(db.String(64), unique=True)
    items = db.relationship('CollectionItem', backref='collection', \
        cascade='save-update, delete, delete-orphan')
    def __repr__(self):
        return '<Collection Name: {}>'.format(self.collection_name)

class CollectionItem(db.Model):
    __tablename__ = 'collection_item'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64), unique=True)
    species = db.Column(db.String(64))
    width = db.Column(db.String(64))
    durability = db.Column(db.String(64))
    length = db.Column(db.String(64))
    iw_name = db.Column(db.String(64))
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'))
    def __repr__(self):
        return '<Item Name: {}>'.format(self.item_name)
