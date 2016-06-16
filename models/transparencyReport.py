from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class TransparencyReport(Base):
  __tablename__ = 'transparency_reports'
  report_id=Column(Integer, primary_key=True)
  publication_status=Column(Boolean)
  #be set by user (ideally date format control)
  complete_status=Column(Boolean)
  publication_date=Column(Date)
  update_date=Column(Date)
  report_period_start=Column(Date)
  report_period_end=Column(Date)
  author_name=Column(String(length=255))
  government_requests_report=relationship('GovernmentRequestsReport', uselist=False, back_populates="transparency_report", cascade="all, delete-orphan")
  data_retention_guide=relationship('DataRetentionGuide', uselist=False, back_populates="transparency_report", cascade="all, delete-orphan")
  law_enforcement_handbook=relationship('LawEnforcementHandbook', uselist=False, back_populates="transparency_report", cascade="all, delete-orphan")

  def __init__(self, report_id=None, author_name=None, report_period_start=None, report_period_end=None, publication_date=None):
    if 'report_id' in locals():
      self.report_id = report_id
    if 'author_name' in locals():
      self.author_name = author_name
    if 'report_period_start' in locals():
      self.report_period_start = report_period_start
    if 'report_period_end' in locals():
      self.report_period_end = report_period_end
    if 'publication_date' in locals():
      self.publication_date = publication_date


  def serialize(self):
    return {
      'report_id': self.report_id,
      'author_name': self.author_name,
      'report_period_start':  self.report_period_start.strftime('%Y-%m-%d') if self.report_period_start else None,
      'report_period_end': self.report_period_end.strftime('%Y-%m-%d') if self.report_period_end else None,
      'publication_date': self.publication_date.strftime('%Y-%m-%d') if self.publication_date else None
    }