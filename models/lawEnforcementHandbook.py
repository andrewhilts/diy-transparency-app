from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class LawEnforcementHandbook(Base):
  __tablename__ = 'law_enforcement_handbooks'
  handbook_id=Column(Integer, primary_key=True)
  inclusion_status=Column(Boolean)
  complete_status=Column(Boolean)
  narrative=Column(Text)
  date_updated=Column(Date)
  date_updated_inclusion_status=Column(Boolean) 
  transparency_report_id=Column(Integer, ForeignKey('transparency_reports.report_id'))
  transparency_report=relationship('TransparencyReport', back_populates="law_enforcement_handbook")
  actions=relationship('LawEnforcementHandbookAction')
  categories=relationship('LawEnforcementHandbookActionCategory')
  #whether or not to show the date updated in the report

  def serialize(self):
    return {
      'handbook_id': self.handbook_id,
      'transparency_report_id': self.transparency_report_id,
      'inclusion_status': self.inclusion_status,
      'complete_status': self.complete_status,
      'narrative': self.narrative,
      'categories': self.serializeCategories()
  }
  def serializeCategories(self):
    categories = []
    for category in self.categories:
      categories.append(category.serialize())
    return categories