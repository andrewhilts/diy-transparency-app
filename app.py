from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

import database
from models.base import Base as Base
from models.dataCategory import DataCategory
from models.dataItem import DataItem
from models.dataRetentionGuideCategory import DataRetentionGuideCategory
from models.dataRetentionGuideItem import DataRetentionGuideItem
from models.dataRetentionGuide import DataRetentionGuide
from models.governmentRequestCategory import GovernmentRequestCategory
from models.governmentRequestReportTypeDisclosure import GovernmentRequestReportTypeDisclosure
from models.governmentRequestResponse import GovernmentRequestResponse
from models.governmentRequestsReport import GovernmentRequestsReport
from models.governmentRequestType import GovernmentRequestType
from models.lawEnforcementActionCategory import LawEnforcementActionCategory
from models.lawEnforcementAction import LawEnforcementAction
from models.lawEnforcementHandbookActionCategory import LawEnforcementHandbookActionCategory
from models.lawEnforcementHandbookAction import LawEnforcementHandbookAction
from models.lawEnforcementHandbook import LawEnforcementHandbook
from models.transparencyReport import TransparencyReport
from models.typeDisclosureResponse import TypeDisclosureResponse

db_connection = database.db_connect()
db_session = database.db_session_maker(db_connection)()

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

@app.route("/")
def hello():
    return "Hello World!"

class TransparencyReportListAPI(Resource):
    def get(self):
    	reports = db_session.query(TransparencyReport).all()
    	reports_as_dicts = []
    	for r in reports:
    		reports_as_dicts.append(r.serialize())
    	print reports_as_dicts
        return reports_as_dicts
    def put(self):
		parser.add_argument('author_name', type=str, location='json')
		parser.add_argument('report_period_start', type=str, location='json')
		parser.add_argument('report_period_end', type=str, location='json')
		parser.add_argument('publication_date', type=str, location='json')
		args = parser.parse_args()
		print args
		report = TransparencyReport(
			author_name=args.author_name,
			report_period_start=args.report_period_start,
			report_period_end=args.report_period_end,
			publication_date=args.publication_date
		)
		db_session.add(report)
		db_session.commit()
		r = report.serialize()
		return r

    def options(self):
    	return {}, 200

class TransparencyReportAPI(Resource):
    def get(self, id):
        report = db_session.query(TransparencyReport).get(id)
    	r = report.serialize()
        return r

    def post(self, id):
		parser.add_argument('author_name', type=str, location='json')
		parser.add_argument('report_period_start', type=str, location='json')
		parser.add_argument('report_period_end', type=str, location='json')
		parser.add_argument('publication_date', type=str, location='json')
		args = parser.parse_args()
		
		print args
		report = db_session.query(TransparencyReport).get(id)
		report.author_name = args.author_name
		report.report_period_start = args.report_period_start
		report.report_period_end = args.report_period_end
		report.publication_date = args.publication_date
		db_session.commit()
		r = report.serialize()
		return r

    def delete(self, id):
        report = db_session.query(TransparencyReport).get(id)
        db_session.delete(report)
        print db_session.commit()
        return ""

class DataRetentionGuideAPI(Resource):
	def get(self, transparency_report_id):
		report = db_session.query(TransparencyReport).get(transparency_report_id)
		guide = report.data_retention_guide
		if guide is not None:
			g = guide.serialize()
		else:
			g = None
		return g

	def put(self, transparency_report_id):
		report = db_session.query(TransparencyReport).get(transparency_report_id)

		parser.add_argument('inclusion_status', type=bool, location='json', required=True)
		parser.add_argument('complete_status', type=bool, location='json', required=True)
		parser.add_argument('narrative', type=str, location='json', required=True)
		args = parser.parse_args()
		print args

		guide = DataRetentionGuide(
			inclusion_status=args.inclusion_status,
			complete_status=args.complete_status,
			narrative=args.narrative
		)
		guide.transparency_report = report
		db_session.add(guide)
		db_session.commit()
		g = guide.serialize()
		return g
	def post(self, transparency_report_id):
		report = db_session.query(TransparencyReport).get(transparency_report_id)

		parser.add_argument('inclusion_status', type=bool, location='json', required=True)
		parser.add_argument('complete_status', type=bool, location='json', required=True)
		parser.add_argument('narrative', type=str, location='json', required=True)
		args = parser.parse_args()

		guide = report.data_retention_guide
		guide.inclusion_status = args.inclusion_status
		guide.complete_status = args.complete_status
		guide.narrative = args.narrative
		
		db_session.add(guide)
		db_session.commit()
		g = guide.serialize()
		return g
	def delete(self, transparency_report_id):
		pass

api.add_resource(TransparencyReportListAPI, '/transparency-reports', endpoint = 'transparency-reports')
api.add_resource(TransparencyReportAPI, '/transparency-reports/<int:id>', endpoint = 'transparency-report')

api.add_resource(DataRetentionGuideAPI, '/transparency-reports/<int:transparency_report_id>/retention_guide')

if __name__ == "__main__":
    app.run(debug=True)