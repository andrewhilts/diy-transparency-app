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

  def serialize(self):
    return {
      'report_id': self.report_id,
      'transparency_report_id': self.transparency_report_id,
      'inclusion_status': self.inclusion_status,
      'complete_status': self.complete_status,
      'narrative': self.narrative,
      'categorized_disclosures': self.serializeDisclosures()
  }
  def serializeDisclosures(self):
	categories = {}
	for disclosure in self.disclosures:
		category = disclosure.request_type.category
		cat_key = category.category_id
		if not cat_key in categories:
			categories[cat_key] = []
			serialized_category = category.serialize()
			serialized_category['disclosures'] = []
			categories[cat_key] = serialized_category
		categories[cat_key]['disclosures'].append(disclosure.serialize())
	return categories