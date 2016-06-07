from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class DataItem(Base):
  __tablename__ = 'data_items'
  item_id=Column(Integer, primary_key=True)
  name=Column(String(length=255))
  #inherited by report instances of type, can be overwritten
  description=Column(Text) 