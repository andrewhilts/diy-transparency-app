from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class GovernmentRequestCategory(Base):
  __tablename__ = 'government_request_categories'
  category_id=Column(Integer, primary_key=True)
  name=Column(String(length=255))
  description=Column(Text)
  types=relationship('GovernmentRequestType', back_populates="category")