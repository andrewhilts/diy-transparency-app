from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class LawEnforcementActionCategory(Base):
  __tablename__ = 'law_enforcement_action_categories'
  category_id=Column(Integer, primary_key=True)
  name=Column(String(255))
  #denotes whether or not actions can be multiply selected, single selected, or are Text, if Text value, just show narrative box automatically...
  action_selection_type=Column(Integer) 