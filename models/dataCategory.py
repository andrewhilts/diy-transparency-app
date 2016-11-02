from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class DataCategory(Base):
	__tablename__ = 'data_categories'
	category_id=Column(Integer, primary_key=True)
	name=Column(String(length=255))
	description=Column(Text)
	items=relationship("DataItem", cascade='delete', order_by="DataItem.item_id")
	guide_categories=relationship("DataRetentionGuideCategory", cascade="delete")

	def __init__(self, category_id = None, name = None, description = None):
		if 'category_id' in locals():
			self.category_id = category_id
		if 'name' in locals():
			self.name = name
		if 'description' in locals():
			self.description = description
			
	def serialize(self):
		return {
			"category_id": self.category_id,
			"name": self.name,
			"description": self.description
		}