from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class DataRetentionGuideItem(Base):
  __tablename__ = 'data_retention_guide_items'
  guide_id=Column(Integer, ForeignKey('data_retention_guides.guide_id'), primary_key=True)
  guide_data_item_id=Column(Integer, ForeignKey('data_items.item_id'), primary_key=True)
  narrative=Column(Text)
  #denotes being included in the report
  inclusion_status=Column(Boolean) 
  #denotes explicitly whether data is retained or not retained
  retention_status=Column(Boolean) 
  item=relationship('DataItem', cascade='delete, delete-orphan', single_parent=True)