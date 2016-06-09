from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import json
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
		return reports_as_dicts, 200

    def put(self):
		parser = reqparse.RequestParser()
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
		return r, 201

    def options(self):
		return {}, 200

class TransparencyReportAPI(Resource):
    def get(self, id):
		report = db_session.query(TransparencyReport).get(id)
		r = report.serialize()
		return r, 200

    def post(self, id):
		parser = reqparse.RequestParser()
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
		return r, 201

    def delete(self, id):
		report = db_session.query(TransparencyReport).get(id)
		db_session.delete(report)
		print db_session.commit()
		return "", 204

class DataRetentionGuideAPI(Resource):
	def get(self, transparency_report_id):
		report = db_session.query(TransparencyReport).get(transparency_report_id)
		guide = report.data_retention_guide
		if guide is not None:
			g = guide.serialize()
		else:
			g = None
		return g, 200

	def put(self, transparency_report_id):
		parser = reqparse.RequestParser()
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
		
		#Add associative entities for the guide
		categories = db_session.query(DataCategory).all()
		for category in categories:
			guide_category = DataRetentionGuideCategory()
			guide_category.inclusion_status = True
			guide_category.category = category

			items = category.items
			for item in items:
				guide_item = DataRetentionGuideItem()
				guide_item.inclusion_status = True
				guide_item.item = item
				guide_category.guide_items.append(guide_item)
				guide.items.append(guide_item)

			guide.categories.append(guide_category)

		db_session.add(guide)

		db_session.commit()
		g = guide.serialize()
		return g, 201

	def post(self, transparency_report_id):
		parser = reqparse.RequestParser()
		report = db_session.query(TransparencyReport).get(transparency_report_id)

		parser.add_argument('inclusion_status', type=bool, location='json', required=True)
		parser.add_argument('complete_status', type=bool, location='json', required=True)
		parser.add_argument('narrative', type=str, location='json', required=True)
		parser.add_argument('data_categories', type=str, location='json', required=True)
		args = parser.parse_args()

		json = request.get_json(silent=True)

		categories = json['data_categories']

		guide = report.data_retention_guide
		guide.inclusion_status = args.inclusion_status
		guide.complete_status = args.complete_status
		guide.narrative = args.narrative

		guide_categories = []
		for category in categories:
			guide_category = db_session.query(DataRetentionGuideCategory).get(category['guide_category_id'])
			guide_category.inclusion_status = category['inclusion_status']
			guide_category.description = category['description']
			#db_session.add(guide_category)

			guide_items = []
			category_items = category['items']
			for item in category_items:
				guide_item = db_session.query(DataRetentionGuideItem).get(item['guide_item_id'])
				guide_item.inclusion_status = item['inclusion_status']
				guide_item.description = item['description']
				guide_items.append(guide_item)
				#db_session.add(guide_item)
			guide_category.guide_items = guide_items
			guide_categories.append(guide_category)
		guide.categories = guide_categories
		
		db_session.add(guide)
		db_session.commit()
		g = guide.serialize()
		return g, 201

class DataCategoryListAPI(Resource):
	def get(self):
		categories = db_session.query(DataCategory).all()
		categories_as_dicts = []
		for c in categories:
			categories_as_dicts.append(c.serialize())
		print categories_as_dicts
		return categories_as_dicts, 200

	def put(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str, location='json')
		parser.add_argument('description', type=str, location='json')
		args = parser.parse_args()
		print args
		category = DataCategory(
			name=args.name,
			description=args.description
		)
		db_session.add(category)
		db_session.commit()
		c = category.serialize()
		return c, 201

	def options(self):
	 	return {}, 200

class DataCategoryAPI(Resource):
	def get(self, data_category_id):
		category = db_session.query(DataCategory).get(data_category_id)
		c = category.serialize()
		return c, 200

	def post(self, data_category_id):
		parser = reqparse.RequestParser()
		category = db_session.query(DataCategory).get(data_category_id)

		parser.add_argument('name', type=str, location='json', required=True)
		parser.add_argument('description', type=str, location='json', required=True)
		args = parser.parse_args()
		print args

		category.name = args.name
		category.description = args.description
		
		db_session.add(category)
		db_session.commit()
		c = category.serialize()
		return c, 201

	def delete(self, data_category_id):
		category = db_session.query(DataCategory).get(data_category_id)
		db_session.delete(category)
		print db_session.commit()
		return "", 204

class DataItemListAPI(Resource):
	def get(self, data_category_id):
		category = db_session.query(DataCategory).get(data_category_id)
		items = category.items
		items_as_dicts = []
		if items is not None:
			for i in items:
				items_as_dicts.append(i.serialize())
		return items_as_dicts

	def put(self, data_category_id):
		parser = reqparse.RequestParser()
		category = db_session.query(DataCategory).get(data_category_id)

		parser.add_argument('name', type=str, location='json', required=True)
		parser.add_argument('description', type=str, location='json', required=True)
		args = parser.parse_args()
		print args

		item = DataItem(
			name=args.name,
			description=args.description,
		)
		category.items.append(item)
		db_session.add(item)
		db_session.commit()
		item = item.serialize()
		return item

	def options(self, data_category_id):
	 	return {}, 200

class DataItemAPI(Resource):
	def get(self, data_category_id, data_item_id):
		item = db_session.query(DataItem).get(data_item_id)
		if item is not None:
			i = item.serialize()
		else:
			i = None
		return i, 200

	def post(self, data_category_id, data_item_id):
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str, location='json')
		parser.add_argument('description', type=str, location='json')

		args = parser.parse_args()
		
		print args

		item = db_session.query(DataItem).get(data_item_id)
		item.name = args.name
		item.description = args.description

		db_session.commit()
		item = item.serialize()
		return item, 201

	def delete(self, data_category_id, data_item_id):
	    item = db_session.query(DataItem).get(data_item_id)
	    db_session.delete(item)
	    print db_session.commit()
	    return "", 204

api.add_resource(TransparencyReportListAPI, '/transparency-reports', endpoint = 'transparency-reports')
api.add_resource(TransparencyReportAPI, '/transparency-reports/<int:id>', endpoint = 'transparency-report')

api.add_resource(DataRetentionGuideAPI, '/transparency-reports/<int:transparency_report_id>/retention_guide')

api.add_resource(DataCategoryListAPI, '/data-categories')
api.add_resource(DataCategoryAPI, '/data-categories/<int:data_category_id>')
api.add_resource(DataItemListAPI, '/data-categories/<int:data_category_id>/data-items')
api.add_resource(DataItemAPI, '/data-categories/<int:data_category_id>/data-items/<int:data_item_id>')

if __name__ == "__main__":
    app.run(debug=True)