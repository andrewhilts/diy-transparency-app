from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class GovernmentRequestType(Base):
  __tablename__ = 'government_request_types'
  type_id=Column(Integer, primary_key=True)
  category_id=Column(Integer, ForeignKey('government_request_categories.category_id'))
  name=Column(String(length=255))
  description=Column(Text)
  category=relationship('GovernmentRequestCategory', back_populates="types")