from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class LawEnforcementHandbookAction(Base):
  __tablename__ = 'law_enfocement_handbook_actions'
  handbook_id=Column(Integer, ForeignKey('law_enforcement_handbooks.handbook_id'), primary_key=True)
  action_id=Column(Integer, ForeignKey('law_enforcement_actions.action_id'), primary_key=True)
  narrative=Column(Text)
  inclusion_status=Column(Boolean)
  action=relationship('LawEnforcementAction', cascade='delete, delete-orphan', single_parent=True)