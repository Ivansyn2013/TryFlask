from blog.models.init_db import db
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Article(db.Model):

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id"))

    author = relationship("Author", back_populates='articles')