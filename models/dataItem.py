from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class DataItem(Base):
	__tablename__ = 'data_items'
	item_id=Column(Integer, primary_key=True)
	name=Column(String(length=255))
	category_id=Column(Integer, ForeignKey('data_categories.category_id'))
	#inherited by report instances of type, can be overwritten
	description=Column(Text)
	category=relationship('DataCategory', single_parent=True)
	guide_items=relationship("DataRetentionGuideItem", cascade="delete")

	def __init__(self, name = None, description = None):
		if 'name' in locals():
			self.name = name
		if 'description' in locals():
			self.description = description
		
	def serialize(self):
		return {
			"item_id": self.item_id,
			"category_id": self.category_id,
			"name": self.name,
			"description": self.description
		}