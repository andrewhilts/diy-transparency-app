from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class GovernmentRequestReportTypeDisclosure(Base):
	__tablename__ = 'government_request_report_type_disclosures'
	disclosure_id=Column(Integer, primary_key=True)
	request_report_id=Column(Integer, ForeignKey('government_requests_reports.report_id'))
	request_type_id=Column(Integer, ForeignKey('government_request_types.type_id'))
	report=relationship('GovernmentRequestsReport',  back_populates="disclosures", single_parent=True)
	request_type=relationship('GovernmentRequestType', single_parent=True)
	disclosure_responses = relationship('TypeDisclosureResponse', order_by="TypeDisclosureResponse.type_disclosure_id", cascade="delete, save-update")

	def serialize(self):
		parent = self.request_type.serialize()
		disclosure_responses = self.serializeResponses()
		return {
			"disclosure_id": self.disclosure_id,
			"name": parent['name'],
			"description": parent['description'],
			"disclosure_responses": disclosure_responses
		}

	def serializeResponses(self):
		responses = []
		for response in self.disclosure_responses:
			responses.append(response.serialize())
		return responses