from blog.models.init_db import db
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Author(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship("User", back_populates='author')