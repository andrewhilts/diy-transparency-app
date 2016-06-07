from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class DataCategory(Base):
  __tablename__ = 'data_categories'
  category_id=Column(Integer, primary_key=True)
  name=Column(String(length=255))