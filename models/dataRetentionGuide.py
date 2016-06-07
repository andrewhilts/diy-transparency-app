from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class DataRetentionGuide(Base):
  __tablename__ = 'data_retention_guides'
  guide_id=Column(Integer, primary_key=True)
  inclusion_status=Column(Boolean)
  complete_status=Column(Boolean)
  narrative=Column(Text)
  transparency_report_id=Column(Integer, ForeignKey('transparency_reports.report_id'))
  transparency_report=relationship('TransparencyReport', back_populates="data_retention_guide")
  categories=relationship("DataRetentionGuideCategory")
  items=relationship("DataRetentionGuideItem")

  def __init__(self, inclusion_status = None, complete_status = None, narrative = None):
    if 'inclusion_status' in locals():
      self.inclusion_status = inclusion_status
    if 'complete_status' in locals():
      self.complete_status = complete_status
    if 'narrative' in locals():
      self.narrative = narrative

  def serialize(self):
    return {
      'guide_id': self.guide_id,
      'transparency_report_id': self.transparency_report_id,
      'inclusion_status': self.inclusion_status,
      'complete_status': self.complete_status,
      'narrative': self.narrative
    }
