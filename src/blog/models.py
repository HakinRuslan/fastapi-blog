from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base
from src.auth.models import User

class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    img = Column(String, nullable=True)
    content = Column(String, nullable=False)
    creator = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User")