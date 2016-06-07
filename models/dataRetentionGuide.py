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