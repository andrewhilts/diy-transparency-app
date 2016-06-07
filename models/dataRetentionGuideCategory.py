from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class DataRetentionGuideCategory(Base):
  __tablename__ = 'data_retention_guide_categories'
  guide_id=Column(Integer, ForeignKey('data_retention_guides.guide_id'), primary_key=True)
  guide_data_category_id=Column(Integer, ForeignKey('data_categories.category_id'), primary_key=True)
  #denotes being included in the report
  inclusion_status=Column(Boolean) 
  #denotes explicitly whether data is retained or not retained
  retention_status=Column(Boolean) 
  category=relationship('DataCategory', cascade='delete, delete-orphan', single_parent=True)