from BookSwap import db, login_manager
from BookSwap import bcrypt
from flask_login import UserMixin
from sqlalchemy.dialects import postgresql

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# wishlist = db.Table('wishlist',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
# )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=False)
    email_address = db.Column(db.String(length=50), index=True, nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    books = db.relationship("Book", backref="owned_user", lazy=True)
    # wishlist = db.relationship('Book', secondary=wishlist, backref=db.backref('wishlisted_by', lazy='dynamic'))

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, text_password):
        self.password_hash = bcrypt.generate_password_hash(text_password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __repr__(self):
        return f'User Email Address: {self.email_address}'


class Book(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    volume_id = db.Column(db.String(length=15), index=True, nullable=False)
    title = db.Column(db.String(length=150), index=True, nullable=True, unique=False)
    author = db.Column(postgresql.ARRAY(db.String(length=100)), index=True, nullable=True, unique=False)
    subtitle = db.Column(db.String(length=500), nullable=True, unique=False)
    description = db.Column(db.Text(), nullable=True, unique=False)
    categories = db.Column(postgresql.ARRAY(db.String(length=50)), index=True, nullable=True, unique=False)
    image = db.Column(db.String(length=150), nullable=True, unique=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Book Title: {self.title}'
    