from blog.models.init_db import db
from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship
from datetime import  datetime

class Article(db.Model):

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id"))
    title = Column(String(200), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    dt_created = Column(DateTime, default=datetime.utcnow,
                        server_default=func.now())
    dt_updated = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    author = relationship("Author", back_populates='article')