from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class TypeDisclosureResponse(Base):
	__tablename__ = 'type_disclosure_responses'
	type_disclosure_id = Column(Integer, primary_key=True)
	response_id=Column(Integer, ForeignKey('government_request_responses.response_id'))
	disclosure_id=Column(Integer, ForeignKey('government_request_report_type_disclosures.disclosure_id'))
	count=Column(Integer)
	response = relationship('GovernmentRequestResponse')

	def serialize(self):
		parent = self.response.serialize()
		return {
			"type_disclosure_id": self.type_disclosure_id,
			"name": parent['name'],
			"description": parent['description'],
			"count": self.count,
		}