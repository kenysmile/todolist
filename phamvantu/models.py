class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text) # or varchar 

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_id = db.Column(db.Integer, db.ForeignKey('name.id'))

    _name = db.relationship('Name')

    @property
    def name(self):
        return self._name.name