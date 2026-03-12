# from datetime import datetime


# class TodoModel:
#     def __init__(self, id: int, title: str, is_done: bool = False):
#         self.id = id
#         self.title = title
#         self.is_done = is_done
#         self.created_at = datetime.utcnow()

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "title": self.title,
#             "is_done": self.is_done,
#             "created_at": self.created_at
#         }

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from datetime import datetime
from core.database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    is_done = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)