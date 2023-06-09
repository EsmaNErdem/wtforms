"""Models for adopt"""

from flask_sqlalchemy import SQLAlchemy

db =  SQLAlchemy()
default_img = "https://images.squarespace-cdn.com/content/v1/58093611f7e0abd4e568a539/1479522159374-HN971VS2Y60RNNBFZOPZ/image-asset.jpeg"
def connect_db(app):
    """Connecting the database"""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Creating Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                    autoincrement=True)
    
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False, default = default_img)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available =  db.Column(db.Boolean, nullable=False, default = True)

    def __repr__(self):
        """Show info"""

        u = self
        return f"<Pet id:{u.id}, name:{u.name}, species:{u.species}"