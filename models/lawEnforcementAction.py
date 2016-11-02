from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class LawEnforcementAction(Base):
	__tablename__ = 'law_enforcement_actions'
	action_id=Column(Integer, primary_key=True)
	category_id=Column(Integer, ForeignKey('law_enforcement_action_categories.category_id'))
	name=Column(String(255))
	inclusion_status_default=Column(Boolean)
	#inherited by report instances of action, can be overwritten
	narrative=Column(Text) 
	narrative_label=Column(String(255))
	handbook_actions=relationship("LawEnforcementHandbookAction", cascade="delete")

	def serialize(self):
		return {
			"action_id": self.action_id,
			"name": self.name,
			"narrative": self.narrative,
			"narrative_label": self.narrative_label,
			"inclusion_status_default": self.inclusion_status_default
		}