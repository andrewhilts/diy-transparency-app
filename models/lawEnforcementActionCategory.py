from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class LawEnforcementActionCategory(Base):
  __tablename__ = 'law_enforcement_action_categories'
  category_id=Column(Integer, primary_key=True)
  name=Column(String(255))
  description=Column(Text)
  #denotes whether or not actions can be multiply selected, single selected, or are Text, if Text value, just show narrative box automatically...
  action_selection_type=Column(Integer)
  actions=relationship("LawEnforcementAction", order_by="LawEnforcementAction.action_id", cascade="delete")
  handbook_categories=relationship("LawEnforcementHandbookActionCategory", cascade="delete")

  def serialize(self):
  	return {
  		"name": self.name,
  		"category_id": self.category_id,
  		"action_selection_type": self.action_selection_type,
      "description": self.description
  	}