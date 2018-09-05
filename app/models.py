from app import db

# 'flask db migrate' create migration script
# 'flask db upgrade' apply migration scripts

class Seed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(120))

    def __repr__(self):
        return '<Seed {}>'.format(self.content) 