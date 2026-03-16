from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, JSON
from datetime import datetime
from core.database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    is_done = Column(Boolean, default=False)
    due_date = Column(DateTime, nullable=True)
    tags = Column(JSON, nullable=True)  # List of strings
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)