from sqlalchemy import Column, Integer, String, Boolean, LargeBinary, ForeignKey
from blog.models.init_db import db
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from blog.security import flask_bcrypt


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(80), unique=False, nullable=False, default="",
                        server_default="")
    last_name = Column(String(80), unique=False, nullable=False, default="",
                       server_default="")
    username = Column(String(80), unique=False, nullable=False, default="",
                      server_default="")
    is_staff = Column(Boolean, nullable=False, default=False)
    _password = Column(LargeBinary, nullable=True)
    email = Column(String(255), nullable=False, default="", server_default="")
    email2 = Column(String(255), nullable=False, default="", server_default="")

    author = relationship("Author", uselist=False, back_populates='user', cascade="all, delete")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self._password, password)

    def __repr__(self):
        return f"< User {self.id} {self.first_name!r} {self.last_name}>"
