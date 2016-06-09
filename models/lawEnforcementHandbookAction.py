from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class LawEnforcementHandbookAction(Base):
  __tablename__ = 'law_enfocement_handbook_actions'
  handbook_action_id=Column(Integer, primary_key=True)
  handbook_id=Column(Integer, ForeignKey('law_enforcement_handbooks.handbook_id'))
  action_id=Column(Integer, ForeignKey('law_enforcement_actions.action_id'))
  handbook_category_id=Column(Integer, ForeignKey('law_enfocement_handbook_action_categories.handbook_category_id'))
  narrative=Column(Text)
  inclusion_status=Column(Boolean)
  action=relationship('LawEnforcementAction', cascade='delete, delete-orphan', single_parent=True)