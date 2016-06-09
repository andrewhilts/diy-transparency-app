from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class LawEnforcementHandbookActionCategory(Base):
  __tablename__ = 'law_enfocement_handbook_action_categories'
  handbook_category_id=Column(Integer, primary_key=True)
  handbook_id=Column(Integer, ForeignKey('law_enforcement_handbooks.handbook_id'))
  action_category_id=Column(Integer, ForeignKey('law_enforcement_action_categories.category_id'))
  inclusion_status=Column(Boolean)
  category=relationship('LawEnforcementActionCategory', cascade='delete, delete-orphan', single_parent=True)
  handbook_actions=relationship('LawEnforcementHandbookAction')