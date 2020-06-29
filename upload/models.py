from upload import db
from upload import login_manager 
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False,unique=True)
    password=db.Column(db.String(100),nullable=False)
    image_file=db.Column(db.String(120),default="default.jpg")
    def __repr__(self):
        return f"user=({self.name},{self.image_file})"