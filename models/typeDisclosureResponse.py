from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class TypeDisclosureResponse(Base):
  __tablename__ = 'type_disclosure_responses'
  response_id=Column(Integer, ForeignKey('government_request_responses.response_id'), primary_key=True)
  disclosure_id=Column(Integer, ForeignKey('government_request_report_type_disclosures.disclosure_id'), primary_key=True)
  count=Column(Integer)
  response = relationship('GovernmentRequestResponse', cascade='delete, delete-orphan', single_parent=True)