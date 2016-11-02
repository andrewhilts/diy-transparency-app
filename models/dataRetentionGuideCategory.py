from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class DataRetentionGuideCategory(Base):
	__tablename__ = 'data_retention_guide_categories'
	guide_category_id=Column(Integer, primary_key=True)
	guide_id=Column(Integer, ForeignKey('data_retention_guides.guide_id'))
	guide_data_category_id=Column(Integer, ForeignKey('data_categories.category_id'))
	#denotes being included in the report
	inclusion_status=Column(Boolean) 
	#denotes explicitly whether data is retained or not retained
	retention_status=Column(Boolean) 
	category=relationship('DataCategory', single_parent=True)
	guide_items=relationship("DataRetentionGuideItem", order_by="DataRetentionGuideItem.guide_item_id", cascade='delete, delete-orphan',)

	def serialize(self):
		parent = self.category.serialize()
		guide_category = {
			"guide_category_id": self.guide_category_id,
			"parent_category_id": parent['category_id'],
			"name": parent['name'],
			"description": parent['description'],
			"inclusion_status": self.inclusion_status,
		"retention_status": self.retention_status,
		"items": self.serializeItems()
		}
		return guide_category

	def serializeItems(self):
		items = []
		for guide_item in self.guide_items:
			items.append(guide_item.serialize())
		return items