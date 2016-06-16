from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class DataRetentionGuideItem(Base):
  __tablename__ = 'data_retention_guide_items'
  guide_item_id=Column(Integer, primary_key=True)
  guide_id=Column(Integer, ForeignKey('data_retention_guides.guide_id'))
  guide_data_item_id=Column(Integer, ForeignKey('data_items.item_id'))
  guide_category_id=Column(Integer, ForeignKey('data_retention_guide_categories.guide_category_id'))
  narrative=Column(Text)
  #denotes being included in the report
  inclusion_status=Column(Boolean) 
  #denotes explicitly whether data is retained or not retained
  retention_status=Column(Boolean) 
  item=relationship('DataItem', single_parent=True)
  guide_category=relationship('DataRetentionGuideCategory', cascade='delete, delete-orphan', single_parent=True)

  def serialize(self):
  	parent = self.item.serialize()
  	return {
  		"guide_item_id": self.guide_item_id,
  		"name": parent['name'],
  		"description": parent['description'],
      "guide_category_id": self.guide_category_id,
  		"narrative": self.narrative,
		"inclusion_status": self.inclusion_status,
		"retention_status": self.retention_status
  	}