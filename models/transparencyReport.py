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
	date_updated=Column(Date)
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

	def determineCompleteStatus(self):
		subreportCount = 0
		completedSubreportCount = 0

		if self.government_requests_report:
			if self.government_requests_report.inclusion_status:
				subreportCount += 1
				if self.government_requests_report.complete_status:
					completedSubreportCount += 1
		if self.data_retention_guide:
			if self.data_retention_guide.inclusion_status:
				subreportCount += 1
				if self.data_retention_guide.complete_status:
					completedSubreportCount += 1
		if self.law_enforcement_handbook:
			if self.law_enforcement_handbook.inclusion_status:
				subreportCount += 1
				if self.law_enforcement_handbook.complete_status:
					completedSubreportCount += 1

		if completedSubreportCount == subreportCount and subreportCount > 0:
			return True
		else:
			return False

	def serialize(self):
		return {
			'report_id': self.report_id,
			'author_name': self.author_name,
			'report_period_start':	self.report_period_start.strftime('%Y-%m-%d') if self.report_period_start else None,
			'report_period_end': self.report_period_end.strftime('%Y-%m-%d') if self.report_period_end else None,
			'publication_date': self.publication_date.strftime('%Y-%m-%d') if self.publication_date else None,
			'complete_status': self.complete_status,
			'date_updated': self.date_updated.strftime('%Y-%m-%d') if self.date_updated else None,
			'retention_guide_id': self.data_retention_guide.guide_id if self.data_retention_guide else None,
			'government_requests_report_id': self.government_requests_report.report_id if self.government_requests_report else None,
			'law_enforcement_handbook_id': self.law_enforcement_handbook.handbook_id if self.law_enforcement_handbook else None,
			'retention_guide_inclusion_status': self.data_retention_guide.inclusion_status if self.data_retention_guide else None,
			'government_requests_report_inclusion_status': self.government_requests_report.inclusion_status if self.government_requests_report else None,
			'law_enforcement_handbook_inclusion_status': self.law_enforcement_handbook.inclusion_status if self.law_enforcement_handbook else None,
			'retention_guide_complete_status': self.data_retention_guide.complete_status if self.data_retention_guide else None,
			'government_requests_report_complete_status': self.government_requests_report.complete_status if self.government_requests_report else None,
			'law_enforcement_handbook_complete_status': self.law_enforcement_handbook.complete_status if self.law_enforcement_handbook else None
		}