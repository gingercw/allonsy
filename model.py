"""Models for card maker app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,)
    username = db.Column(db.String, unique = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    
    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username}>'

        
class Board(db.Model):
    """A travel board to plan with a group of users."""

    __tablename__ = 'boards'

    board_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,)
    title = db.Column(db.String)
    location = db.Column(db.String)
    admin = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", backref="boards")

    def __repr__(self):
    return f'<Board board_id={self.board_id} title={self.name}>'

class Food(db.Model):
    """Food ideas to pin to the board."""

    __tablename__ = "food"

    food_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,)
    name = db.Column(db.String)
    url = db.Column(db.String)
    selected = db.Column(db.Boolean, default=False)
    board_id = db.Column(db.Integer, db.ForeignKey("boards.board_id"))

    board = db.relationship("Board", backref="food")
    def __repr__(self):
    return f'<Food food_id={self.food_id} title={self.name}>'

class Hotel(db.Model):
    """Hotel ideas to pin to the board."""

    __tablename__ = "hotels"

    hotel_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,)
    name = db.Column(db.String)
    url = db.Column(db.String)
    selected = db.Column(db.Boolean, default=False)
    board_id = db.Column(db.Integer, db.ForeignKey("boards.board_id"))

    board = db.relationship("Board", backref="hotels")

    def __repr__(self):
        return f'<Hotel hotel_id={self.hotel_id} title={self.name}>'

class Activity(db.Model):
    """Activity ideas to pin to the board."""

    __tablename__ = "activities"

    activity_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True,)
    name = db.Column(db.String)
    url = db.Column(db.String)
    selected = db.Column(db.Boolean, default=False)
    activity_id = db.Column(db.Integer, db.ForeignKey("boards.board_id"))

    board = db.relationship("Board", backref="activities")

    def __repr__(self):
        return f'<Activity activity_id={self.activity_id} title={self.name}>'









def connect_to_db(flask_app, db_uri="postgresql:///cards", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
