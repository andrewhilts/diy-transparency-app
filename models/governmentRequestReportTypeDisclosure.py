from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class GovernmentRequestReportTypeDisclosure(Base):
  __tablename__ = 'government_request_report_type_disclosures'
  disclosure_id=Column(Integer, primary_key=True)
  request_report_id=Column(Integer, ForeignKey('government_requests_reports.report_id'))
  request_type_id=Column(Integer, ForeignKey('government_request_types.type_id'))
  report=relationship('GovernmentRequestsReport', cascade='delete, delete-orphan', back_populates="disclosures", single_parent=True)
  request_type=relationship('GovernmentRequestType', cascade='delete, delete-orphan', single_parent=True)
  disclosure_responses = relationship('TypeDisclosureResponse')