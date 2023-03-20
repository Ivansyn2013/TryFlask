from blog.models.init_db import db
from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime, func
from datetime import datetime
from sqlalchemy.orm import relationship

class Author(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    title = Column(String(200), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    dt_created = Column(DateTime, default=datetime.utcnow,
                        server_default=func.now())
    dt_updated = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    user = relationship("User", back_populates='author')
    article = relationship("Article", back_populates='author')

    def __str__(self):
        return self.user.first_name
