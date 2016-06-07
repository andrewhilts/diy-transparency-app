from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class GovernmentRequestsReport(Base):
  __tablename__ = 'government_requests_reports'
  report_id=Column(Integer, primary_key=True)
  transparency_report_id=Column(Integer, ForeignKey('transparency_reports.report_id'))
  inclusion_status=Column(Boolean)
  complete_status=Column(Boolean)
  narrative=Column(Text)
  transparency_report=relationship('TransparencyReport', back_populates="government_requests_report")
  disclosures=relationship('GovernmentRequestReportTypeDisclosure', back_populates="report")