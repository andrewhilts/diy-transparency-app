from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class LawEnforcementHandbookActionCategory(Base):
	__tablename__ = 'law_enfocement_handbook_action_categories'
	handbook_category_id=Column(Integer, primary_key=True)
	handbook_id=Column(Integer, ForeignKey('law_enforcement_handbooks.handbook_id'))
	action_category_id=Column(Integer, ForeignKey('law_enforcement_action_categories.category_id'))
	inclusion_status=Column(Boolean)
	category=relationship('LawEnforcementActionCategory', single_parent=True)
	handbook_actions=relationship('LawEnforcementHandbookAction', order_by="LawEnforcementHandbookAction.handbook_action_id", cascade="delete")

	def serialize(self):
		parent = self.category.serialize()
		handbook_category = {
			"handbook_category_id": self.handbook_category_id,
			"parent_category_id": parent['category_id'],
			"name": parent['name'],
			"description": parent['description'],
			"action_selection_type": parent['action_selection_type'],
			"inclusion_status": self.inclusion_status,
		"actions": self.serializeActions()
		}
		return handbook_category

	def serializeActions(self):
		actions = []
		for handbook_action in self.handbook_actions:
			actions.append(handbook_action.serialize())
		return actions