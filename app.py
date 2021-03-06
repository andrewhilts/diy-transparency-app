from flask import Flask, jsonify, request, make_response, render_template, send_from_directory
from flask_restful import Api, Resource, reqparse
import json
import webbrowser
import threading
import datetime
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
import os, sys
import logging
logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

def handle_exception(exc_type, exc_value, exc_traceback):
	if issubclass(exc_type, KeyboardInterrupt):
		sys.__excepthook__(exc_type, exc_value, exc_traceback)
		return

	logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception

db_connection = database.db_connect()
db_session = database.db_session_maker(db_connection)()

app = Flask(__name__, static_url_path='')
api = Api(app)

@app.route('/app/<path:path>')
def send_js(path):
	return send_from_directory('static', path)

@app.route("/transparency-reports/<int:transparency_report_id>/gov-request-report/csv")
def govRequestReportCSV(transparency_report_id):
	report = db_session.query(TransparencyReport).get(transparency_report_id)
	req_report = report.government_requests_report
	if req_report is not None:
		csvStrIO = req_report.toCSV()
		output = make_response(csvStrIO.getvalue())
		output.headers["Content-Disposition"] = "attachment; filename=government_requests_report.csv"
		output.headers["Content-type"] = "text/csv"
	else:
		output = None
	return output, 200

@app.route("/transparency-reports/<int:transparency_report_id>/retention_guide/html")
def dataRetentionGuideHTML(transparency_report_id):
	report = db_session.query(TransparencyReport).get(transparency_report_id)
	guide = report.data_retention_guide
	if guide is not None:
		g = guide.serialize()
		html = render_template('retention-guide.html', guide=g)
		output = make_response(html)
		output.headers["Content-Disposition"] = "attachment; filename=data-retention-guide.html"
		output.headers["Content-type"] = "text/html"
	else:
		output = None
	return output, 200

@app.route("/transparency-reports/<int:transparency_report_id>/law-enforcement-handbook/html")
def LEAHandbookHTML(transparency_report_id):
	report = db_session.query(TransparencyReport).get(transparency_report_id)
	handbook = report.law_enforcement_handbook
	if handbook is not None:
		h = handbook.serialize()
		html = render_template('lea-handbook.html', handbook=h)
		output = make_response(html)
		output.headers["Content-Disposition"] = "attachment; filename=gov-request-handbook.html"
		output.headers["Content-type"] = "text/html"
	else:
		output = None
	return output, 200

@app.route("/transparency-reports/<int:transparency_report_id>/gov-request-report/html")
def GovRequestReportHTML(transparency_report_id):
	report = db_session.query(TransparencyReport).get(transparency_report_id)
	req_report = report.government_requests_report
	if req_report is not None:
		rr = req_report.serialize()
		t = req_report.toTable()
		r = report.serialize()
		html = render_template('gov-requests-report.html', report=rr, treport=r, table=t)
		output = make_response(html)
		output.headers["Content-Disposition"] = "attachment; filename=gov-requests-report.html"
		output.headers["Content-type"] = "text/html"
	else:
		output = None
	return output, 200

class TransparencyReportListAPI(Resource):
	def get(self):
		reports = db_session.query(TransparencyReport).order_by("report_id desc").all()
		reports_as_dicts = []
		for r in reports:
			reports_as_dicts.append(r.serialize())
		
		return reports_as_dicts, 200

	def put(self):
		parser = reqparse.RequestParser()
		parser.add_argument('author_name', type=str, location='json')
		parser.add_argument('report_period_start', type=str, location='json')
		parser.add_argument('report_period_end', type=str, location='json')
		parser.add_argument('publication_date', type=str, location='json')
		args = parser.parse_args()
		
		report = TransparencyReport(
			author_name=args.author_name,
			report_period_start=datetime.datetime.strptime(args.report_period_start, '%Y-%m-%d'),
			report_period_end=datetime.datetime.strptime(args.report_period_end, '%Y-%m-%d'),
			publication_date=datetime.datetime.strptime(args.publication_date, '%Y-%m-%d')
		)
		report.date_updated = datetime.date.today()
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

		json = request.get_json(silent=True)
		
		report = db_session.query(TransparencyReport).get(id)
		report.author_name = args.author_name
		report.report_period_start = datetime.datetime.strptime(args.report_period_start, '%Y-%m-%d')
		report.report_period_end = datetime.datetime.strptime(args.report_period_end, '%Y-%m-%d')
		report.publication_date = datetime.datetime.strptime(args.publication_date, '%Y-%m-%d')

		if report.government_requests_report is not None:
			if 'government_requests_report_inclusion_status' in json:
				report.government_requests_report.inclusion_status = json['government_requests_report_inclusion_status']

		if report.data_retention_guide is not None:
			if 'retention_guide_inclusion_status' in json:
				report.data_retention_guide.inclusion_status = json['retention_guide_inclusion_status']

		if report.law_enforcement_handbook is not None:
			if 'law_enforcement_handbook_inclusion_status' in json:
				report.law_enforcement_handbook.inclusion_status = json['law_enforcement_handbook_inclusion_status']

		report.complete_status = report.determineCompleteStatus()
		report.date_updated = datetime.date.today()
		db_session.add(report)
		db_session.commit()
		r = report.serialize()
		return r, 201

	def delete(self, id):
		report = db_session.query(TransparencyReport).get(id)
		db_session.delete(report)
		db_session.commit()
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

		guide = DataRetentionGuide()
		guide.transparency_report = report

		report.date_updated = datetime.date.today()
		guide.date_updated = datetime.date.today()
		
		#Add associative entities for the guide
		categories = db_session.query(DataCategory).order_by("category_id desc").all()
		for category in categories:
			guide_category = DataRetentionGuideCategory()
			guide_category.inclusion_status = False
			guide_category.category = category

			items = category.items
			for item in items:
				guide_item = DataRetentionGuideItem()
				guide_item.inclusion_status = False
				guide_item.item = item
				guide_category.guide_items.append(guide_item)
				guide.items.append(guide_item)

			guide.categories.append(guide_category)

		db_session.add(guide)
		db_session.add(report)

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

		report.complete_status = report.determineCompleteStatus()

		report.date_updated = datetime.date.today()
		guide.date_updated = datetime.date.today()

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
				if "retention_period" in item:
					guide_item.retention_period = item['retention_period']
				if "retention_period_unit" in item:
					try:
						guide_item.retention_period_unit = int(item['retention_period_unit'])
					except ValueError:
						guide_item.retention_period_unit = None
				guide_item.description = item['description']
				guide_items.append(guide_item)
				#db_session.add(guide_item)
			guide_category.guide_items = guide_items
			guide_categories.append(guide_category)
		guide.categories = guide_categories
		
		db_session.add(guide)
		db_session.add(report)
		db_session.commit()
		g = guide.serialize()
		return g, 201

class DataRetentionGuideItemAPI(Resource):
	def put(self, transparency_report_id, guide_category_id):
		parser = reqparse.RequestParser()
		report = db_session.query(TransparencyReport).get(transparency_report_id)
		guide = report.data_retention_guide

		report.date_updated = datetime.date.today()
		guide.date_updated = datetime.date.today()

		guide_categories = db_session.query(DataRetentionGuideCategory).all()
		guide_category = db_session.query(DataRetentionGuideCategory).get(guide_category_id)

		json = request.get_json(silent=True)
		
		data_item = db_session.query(DataItem).get(json['item_id'])
		guide_item = DataRetentionGuideItem()
		guide_item.inclusion_status = True
		guide_item.item = data_item

		guide.items.append(guide_item)
		guide_category.guide_items.append(guide_item)
		# guide_categories.append(guide_category)
		# guide.categories = guide_categories

		db_session.add(guide)
		db_session.add(report)
		db_session.commit()
		gi = guide_item.serialize()
		return gi, 201

	def options(self, transparency_report_id, guide_category_id):
		return {}, 200

class DataRetentionGuideCategoryAPI(Resource):
	def put(self, transparency_report_id):
		parser = reqparse.RequestParser()
		report = db_session.query(TransparencyReport).get(transparency_report_id)
		guide = report.data_retention_guide

		report.date_updated = datetime.date.today()
		guide.date_updated = datetime.date.today()

		json = request.get_json(silent=True)
		
		data_category = db_session.query(DataCategory).get(json['category_id'])
		guide_category = DataRetentionGuideCategory()
		guide_category.inclusion_status = True
		guide_category.category = data_category

		guide.categories.append(guide_category)


		db_session.add(guide)
		db_session.add(report)
		db_session.commit()
		gc = guide_category.serialize()
		return gc, 201

	def options(self, transparency_report_id):
		return {}, 200

class DataCategoryListAPI(Resource):
	def get(self):
		categories = db_session.query(DataCategory).order_by("category_id desc").all()
		categories_as_dicts = []
		for c in categories:
			categories_as_dicts.append(c.serialize())
		
		return categories_as_dicts, 200

	def put(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str, location='json')
		parser.add_argument('description', type=str, location='json')
		args = parser.parse_args()
		
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
		

		category.name = args.name
		category.description = args.description
		
		db_session.add(category)
		db_session.commit()
		c = category.serialize()
		return c, 201

	def delete(self, data_category_id):
		category = db_session.query(DataCategory).get(data_category_id)
		db_session.delete(category)
		db_session.commit()
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
		parser.add_argument('description', type=str, location='json')
		args = parser.parse_args()
		

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
		
		

		item = db_session.query(DataItem).get(data_item_id)
		item.name = args.name
		item.description = args.description

		db_session.commit()
		item = item.serialize()
		return item, 201

	def delete(self, data_category_id, data_item_id):
		item = db_session.query(DataItem).get(data_item_id)
		db_session.delete(item)
		db_session.commit()
		return "", 204

class LawEnforcementActionCategoryListAPI(Resource):
	def get(self):
		lea_categories = db_session.query(LawEnforcementActionCategory).order_by("category_id desc").all()
		lea_categories_as_dicts = []
		for c in lea_categories:
			lea_categories_as_dicts.append(c.serialize())
		
		return lea_categories_as_dicts, 200

	def put(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str, location='json')
		parser.add_argument('action_selection_type', type=int, location='json')
		parser.add_argument('description', type=str, location='json')
		args = parser.parse_args()
		
		lea_category = LawEnforcementActionCategory(
			name=args.name,
			action_selection_type=args.action_selection_type,
			description=args.description
		)
		db_session.add(lea_category)
		db_session.commit()
		c = lea_category.serialize()
		return c, 201

	def options(self):
	 	return {}, 200

class LawEnforcementActionCategoryAPI(Resource):
	def get(self, lea_category_id):
		lea_category = db_session.query(LawEnforcementActionCategory).get(lea_category_id)
		c = lea_category.serialize()
		return c, 200

	def post(self, lea_category_id):
		parser = reqparse.RequestParser()
		lea_category = db_session.query(LawEnforcementActionCategory).get(lea_category_id)

		parser.add_argument('name', type=str, location='json', required=True)
		parser.add_argument('action_selection_type', type=int, location='json')
		parser.add_argument('description', type=str, location='json')

		args = parser.parse_args()
		

		lea_category.name = args.name
		lea_category.action_selection_type = args.action_selection_type
		lea_category.description = args.description
		
		db_session.add(lea_category)
		db_session.commit()
		c = lea_category.serialize()
		return c, 201

	def delete(self, lea_category_id):
		lea_category = db_session.query(LawEnforcementActionCategory).get(lea_category_id)
		db_session.delete(lea_category)
		db_session.commit()
		return "", 204

class LawEnforcementActionListAPI(Resource):
	def get(self, lea_category_id):
		lea_category = db_session.query(LawEnforcementActionCategory).get(lea_category_id)
		actions = lea_category.actions
		actions_as_dicts = []
		if actions is not None:
			for a in actions:
				actions_as_dicts.append(a.serialize())
		return actions_as_dicts

	def put(self, lea_category_id):
		parser = reqparse.RequestParser()
		lea_category = db_session.query(LawEnforcementActionCategory).get(lea_category_id)

		parser.add_argument('name', type=str, location='json', required=True)
		parser.add_argument('narrative', type=str, location='json')
		parser.add_argument('narrative_label', type=str, location='json')
		parser.add_argument('inclusion_status_default', type=bool, location='json')
		args = parser.parse_args()
		

		action = LawEnforcementAction(
			name=args.name,
			narrative=args.narrative,
			narrative_label=args.narrative_label,
		)
		action.inclusion_status_default = args.inclusion_status_default
		lea_category.actions.append(action)
		db_session.add(action)
		db_session.commit()
		action = action.serialize()
		return action

	def options(self, lea_category_id):
	 	return {}, 200

class LawEnforcementActionAPI(Resource):
	def get(self, lea_category_id, lea_action_id):
		action = db_session.query(LawEnforcementAction).get(lea_action_id)
		if action is not None:
			a = action.serialize()
		else:
			a = None
		return a, 200

	def post(self, lea_category_id, lea_action_id):
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str, location='json', required=True)
		parser.add_argument('narrative', type=str, location='json')
		parser.add_argument('narrative_label', type=str, location='json')
		parser.add_argument('inclusion_status_default', type=bool, location='json')
		args = parser.parse_args()
		

		action = db_session.query(LawEnforcementAction).get(lea_action_id)
		action.name = args.name
		action.narrative = args.narrative
		action.narrative_label = args.narrative_label
		action.inclusion_status_default = args.inclusion_status_default

		db_session.commit()
		action = action.serialize()
		return action, 201

	def delete(self, lea_category_id, lea_action_id):
		action = db_session.query(LawEnforcementAction).get(lea_action_id)
		db_session.delete(action)
		db_session.commit()
		return "", 204

class LawEnforcementHandbookActionAPI(Resource):
	def put(self, transparency_report_id, handbook_category_id):
		parser = reqparse.RequestParser()
		report = db_session.query(TransparencyReport).get(transparency_report_id)
		handbook = report.law_enforcement_handbook

		report.date_updated = datetime.date.today()
		handbook.date_updated = datetime.date.today()

		handbook_category = db_session.query(LawEnforcementHandbookActionCategory).get(handbook_category_id)

		json = request.get_json(silent=True)
		
		action = db_session.query(LawEnforcementAction).get(json['action_id'])
		handbook_action = LawEnforcementHandbookAction()
		handbook_action.inclusion_status = False
		handbook_action.action = action
		handbook_action.narrative = action.narrative

		handbook.actions.append(handbook_action)
		handbook_category.handbook_actions.append(handbook_action)

		db_session.add(handbook)
		db_session.add(report)
		db_session.commit()
		action = handbook_action.serialize()
		return action, 201

	def options(self, transparency_report_id, handbook_category_id):
		return {}, 200

class LawEnforcementHandbookActionCategoryAPI(Resource):
	def put(self, transparency_report_id):
		parser = reqparse.RequestParser()
		report = db_session.query(TransparencyReport).get(transparency_report_id)
		handbook = report.law_enforcement_handbook

		report.date_updated = datetime.date.today()
		handbook.date_updated = datetime.date.today()

		json = request.get_json(silent=True)
		
		action_category = db_session.query(LawEnforcementActionCategory).get(json['category_id'])
		handbook_category = LawEnforcementHandbookActionCategory()
		handbook_category.inclusion_status = True
		handbook_category.category = action_category

		handbook.categories.append(handbook_category)


		db_session.add(handbook)
		db_session.add(report)
		db_session.commit()
		hc = handbook_category.serialize()
		return hc, 201

	def options(self, transparency_report_id):
		return {}, 200

class LawEnforcementHandbookAPI(Resource):
	def get(self, transparency_report_id):
		report = db_session.query(TransparencyReport).get(transparency_report_id)
		handbook = report.law_enforcement_handbook
		if handbook is not None:
			h = handbook.serialize()
		else:
			h = None
		return h, 200

	def put(self, transparency_report_id):
		parser = reqparse.RequestParser()
		report = db_session.query(TransparencyReport).get(transparency_report_id)

		handbook = LawEnforcementHandbook()
		handbook.transparency_report = report
		
		report.date_updated = datetime.date.today()
		handbook.date_updated = datetime.date.today()

		#Add associative entities for the guide
		categories = db_session.query(LawEnforcementActionCategory).order_by("category_id desc").all()
		for category in categories:
			handbook_category = LawEnforcementHandbookActionCategory()
			handbook_category.inclusion_status = False
			handbook_category.category = category

			actions = category.actions
			for action in actions:
				handbook_action = LawEnforcementHandbookAction()
				if category.action_selection_type == 3:
					handbook_action.inclusion_status = True
				else:
					handbook_action.inclusion_status = False
				if action.inclusion_status_default:
					handbook_action.inclusion_status = True

				handbook_action.action = action
				handbook_category.handbook_actions.append(handbook_action)
				handbook.actions.append(handbook_action)

			handbook.categories.append(handbook_category)

		db_session.add(handbook)
		db_session.add(report)

		db_session.commit()
		h = handbook.serialize()
		return h, 201

	def post(self, transparency_report_id):
		parser = reqparse.RequestParser()
		report = db_session.query(TransparencyReport).get(transparency_report_id)

		parser.add_argument('inclusion_status', type=bool, location='json', required=True)
		parser.add_argument('complete_status', type=bool, location='json', required=True)
		parser.add_argument('narrative', type=str, location='json', required=True)
		parser.add_argument('lea_categories', type=str, location='json', required=True)
		args = parser.parse_args()

		json = request.get_json(silent=True)

		lea_categories = json['lea_categories']

		handbook = report.law_enforcement_handbook
		handbook.inclusion_status = args.inclusion_status
		handbook.complete_status = args.complete_status
		handbook.narrative = args.narrative

		report.complete_status = report.determineCompleteStatus()

		report.date_updated = datetime.date.today()
		handbook.date_updated = datetime.date.today()

		handbook_categories = []
		for category in lea_categories:
			handbook_category = db_session.query(LawEnforcementHandbookActionCategory).get(category['handbook_category_id'])
			handbook_category.inclusion_status = category['inclusion_status']
			#db_session.add(handbook_category)

			handbook_actions = []
			category_actions = category['actions']
			for action in category_actions:
				try: 
					action['handbook_action_id']
					handbook_action = db_session.query(LawEnforcementHandbookAction).get(action['handbook_action_id'])
					handbook_action.inclusion_status = action['inclusion_status']
					handbook_action.narrative = action['narrative']
					handbook_actions.append(handbook_action)
				except TypeError:
					continue
				#db_session.add(handbook_item)
			handbook_category.handbook_actions = handbook_actions
			handbook_categories.append(handbook_category)
		handbook.categories = handbook_categories
		
		db_session.add(handbook)
		db_session.add(report)
		db_session.commit()
		h = handbook.serialize()
		return h, 201

class GovRequestReportAPI(Resource):
	def get(self, transparency_report_id):
		report = db_session.query(TransparencyReport).get(transparency_report_id)
		req_report = report.government_requests_report
		if req_report is not None:
			rr = req_report.serialize()
		else:
			rr = None
		return rr, 200

	def put(self, transparency_report_id):
		parser = reqparse.RequestParser()
		report = db_session.query(TransparencyReport).get(transparency_report_id)

		req_report = GovernmentRequestsReport()
		req_report.transparency_report = report
		
		report.date_updated = datetime.date.today()
		req_report.date_updated = datetime.date.today()

		#Add associative entities for the request report
		req_types = db_session.query(GovernmentRequestType).order_by("category_id desc").all()
		for req_type in req_types:
			req_type_disclosure = GovernmentRequestReportTypeDisclosure()
			req_type_disclosure.request_type = req_type

			req_responses = db_session.query(GovernmentRequestResponse).order_by("response_id desc").all()
			for req_response in req_responses:
				type_disclosure_response = TypeDisclosureResponse()
				type_disclosure_response.response = req_response
				type_disclosure_response.count = 0

				req_type_disclosure.disclosure_responses.append(type_disclosure_response)

			req_report.disclosures.append(req_type_disclosure)

		db_session.add(req_report)
		db_session.add(report)

		db_session.commit()
		rr = req_report.serialize()
		return rr, 201

	def post(self, transparency_report_id):
		parser = reqparse.RequestParser()
		report = db_session.query(TransparencyReport).get(transparency_report_id)
		req_report = report.government_requests_report

		parser.add_argument('inclusion_status', type=bool, location='json', required=True)
		parser.add_argument('complete_status', type=bool, location='json', required=True)
		parser.add_argument('narrative', type=str, location='json', required=True)
		parser.add_argument('categorized_disclosures', type=str, location='json', required=True)
		args = parser.parse_args()

		json = request.get_json(silent=True)

		categorized_disclosures = json['categorized_disclosures']
		disclosures = []
		for key, category in categorized_disclosures.items():
			for disclosure in category['disclosures']:
				disclosures.append(disclosure)

		req_report.inclusion_status = args.inclusion_status
		req_report.complete_status = args.complete_status
		req_report.narrative = args.narrative

		report.complete_status = report.determineCompleteStatus()

		report.date_updated = datetime.date.today()
		req_report.date_updated = datetime.date.today()

		req_report_disclosures = []
		for disclosure in disclosures:
			req_report_disclosure = db_session.query(GovernmentRequestReportTypeDisclosure).get(disclosure['disclosure_id'])
			#db_session.add(handbook_category)

			req_report_disclosure_responses = []
			disclosure_responses = disclosure['disclosure_responses']
			for response in disclosure_responses:
				try: 
					response['type_disclosure_id']
					req_report_disclosure_response = db_session.query(TypeDisclosureResponse).get(response['type_disclosure_id'])
					req_report_disclosure_response.count = response['count']
					req_report_disclosure_responses.append(req_report_disclosure_response)
				except TypeError:
					continue
				#db_session.add(handbook_item)
			req_report_disclosure.disclosures = req_report_disclosure_responses
			req_report_disclosures.append(req_report_disclosure)
		
		req_report.disclosures = req_report_disclosures
		
		db_session.add(req_report)
		db_session.add(report)
		db_session.commit()
		rr = req_report.serialize()
		return rr, 201

class GovernmentRequestReportTypeAPI(Resource):
	def put(self, transparency_report_id, gov_request_category_id):
		parser = reqparse.RequestParser()
		report = db_session.query(TransparencyReport).get(transparency_report_id)

		req_report = report.government_requests_report
		
		report.date_updated = datetime.date.today()
		req_report.date_updated = datetime.date.today()

		#Add associative entities for the request report
		json = request.get_json(silent=True)
		
		# data_category = db_session.query(DataRetentionGuideCategory).get(gov_request_category_id)

		req_type = db_session.query(GovernmentRequestType).get(json['type_id'])
		req_type_disclosure = GovernmentRequestReportTypeDisclosure()
		req_type_disclosure.request_type = req_type

		req_responses = db_session.query(GovernmentRequestResponse).order_by("response_id desc").all()
		for req_response in req_responses:
			type_disclosure_response = TypeDisclosureResponse()
			type_disclosure_response.response = req_response
			type_disclosure_response.count = 0

			req_type_disclosure.disclosure_responses.append(type_disclosure_response)

		req_report.disclosures.append(req_type_disclosure)

		db_session.add(req_report)
		db_session.add(report)

		db_session.commit()
		rr = req_type_disclosure.serialize()
		return rr, 201

	def options(self, transparency_report_id, gov_request_category_id):
		return {}, 200

class GovernmentRequestCategoryListAPI(Resource):
	def get(self):
		gov_request_categories = db_session.query(GovernmentRequestCategory).order_by("category_id desc").all()
		gov_request_categories_as_dicts = []
		for c in gov_request_categories:
			gov_request_categories_as_dicts.append(c.serialize())
		
		return gov_request_categories_as_dicts, 200

	def put(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str, location='json')
		parser.add_argument('description', type=str, location='json')
		args = parser.parse_args()
		
		gov_request_category = GovernmentRequestCategory(
			name=args.name,
			description=args.description
		)
		db_session.add(gov_request_category)
		db_session.commit()
		c = gov_request_category.serialize()
		return c, 201

	def options(self):
	 	return {}, 200

class GovernmentRequestCategoryAPI(Resource):
	def get(self, gov_request_category_id):
		gov_request_category = db_session.query(GovernmentRequestCategory).get(gov_request_category_id)
		c = gov_request_category.serialize()
		return c, 200

	def post(self, gov_request_category_id):
		parser = reqparse.RequestParser()
		gov_request_category = db_session.query(GovernmentRequestCategory).get(gov_request_category_id)

		parser.add_argument('name', type=str, location='json', required=True)
		parser.add_argument('description', type=str, location='json')

		args = parser.parse_args()
		

		gov_request_category.name = args.name
		gov_request_category.description = args.description
		
		db_session.add(gov_request_category)
		db_session.commit()
		c = gov_request_category.serialize()
		return c, 201

	def delete(self, gov_request_category_id):
		gov_request_category = db_session.query(GovernmentRequestCategory).get(gov_request_category_id)
		db_session.delete(gov_request_category)
		db_session.commit()
		return "", 204

class GovernmentRequestTypeListAPI(Resource):
	def get(self, gov_request_category_id):
		gov_request_category = db_session.query(GovernmentRequestCategory).get(gov_request_category_id)
		types = gov_request_category.types
		types_as_dicts = []
		if types is not None:
			for t in types:
				types_as_dicts.append(t.serialize())
		return types_as_dicts

	def put(self, gov_request_category_id):
		parser = reqparse.RequestParser()
		gov_request_category = db_session.query(GovernmentRequestCategory).get(gov_request_category_id)

		parser.add_argument('name', type=str, location='json', required=True)
		parser.add_argument('description', type=str, location='json', required=True)
		args = parser.parse_args()
		

		type = GovernmentRequestType(
			name=args.name,
			description=args.description
		)
		gov_request_category.types.append(type)
		db_session.add(type)
		db_session.commit()
		type = type.serialize()
		return type

	def options(self, gov_request_category_id):
	 	return {}, 200

class GovernmentRequestTypeAPI(Resource):
	def get(self, gov_request_category_id, gov_request_type_id):
		type = db_session.query(GovernmentRequestType).get(gov_request_type_id)
		if type is not None:
			t = type.serialize()
		else:
			t = None
		return t, 200

	def post(self, gov_request_category_id, gov_request_type_id):
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str, location='json', required=True)
		parser.add_argument('description', type=str, location='json', required=True)
		args = parser.parse_args()
		

		type = db_session.query(GovernmentRequestType).get(gov_request_type_id)
		type.name = args.name
		type.description = args.description

		db_session.commit()
		type = type.serialize()
		return type, 201

	def delete(self, gov_request_category_id, gov_request_type_id):
		type = db_session.query(GovernmentRequestType).get(gov_request_type_id)
		db_session.delete(type)
		db_session.commit()
		return "", 204

class GovernmentRequestResponseListAPI(Resource):
	def get(self):
		gov_request_responses = db_session.query(GovernmentRequestResponse).order_by("response_id desc").all()
		gov_request_responses_as_dicts = []
		for c in gov_request_responses:
			gov_request_responses_as_dicts.append(c.serialize())
		
		return gov_request_responses_as_dicts, 200

	def put(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str, location='json')
		parser.add_argument('description', type=str, location='json')
		args = parser.parse_args()
		
		gov_request_response = GovernmentRequestResponse(
			name=args.name,
			description=args.description
		)
		db_session.add(gov_request_response)
		db_session.commit()
		c = gov_request_response.serialize()
		return c, 201

	def options(self):
	 	return {}, 200

class GovernmentRequestResponseAPI(Resource):
	def get(self, gov_request_response_id):
		gov_request_response = db_session.query(GovernmentRequestResponse).get(gov_request_response_id)
		c = gov_request_response.serialize()
		return c, 200

	def post(self, gov_request_response_id):
		parser = reqparse.RequestParser()
		gov_request_response = db_session.query(GovernmentRequestResponse).get(gov_request_response_id)

		parser.add_argument('name', type=str, location='json', required=True)
		parser.add_argument('description', type=str, location='json')

		args = parser.parse_args()
		

		gov_request_response.name = args.name
		gov_request_response.description = args.description
		
		db_session.add(gov_request_response)
		db_session.commit()
		c = gov_request_response.serialize()
		return c, 201

	def delete(self, gov_request_response_id):
		gov_request_response = db_session.query(GovernmentRequestResponse).get(gov_request_response_id)
		db_session.delete(gov_request_response)
		db_session.commit()
		return "", 204

api.add_resource(TransparencyReportListAPI, '/transparency-reports', endpoint = 'transparency-reports')
api.add_resource(TransparencyReportAPI, '/transparency-reports/<int:id>', endpoint = 'transparency-report')

api.add_resource(DataRetentionGuideAPI, '/transparency-reports/<int:transparency_report_id>/retention_guide')
api.add_resource(DataRetentionGuideItemAPI, '/transparency-reports/<int:transparency_report_id>/retention_guide/data-categories/<int:guide_category_id>/data-items')
api.add_resource(DataRetentionGuideCategoryAPI, '/transparency-reports/<int:transparency_report_id>/retention_guide/data-categories')

api.add_resource(DataCategoryListAPI, '/data-categories')
api.add_resource(DataCategoryAPI, '/data-categories/<int:data_category_id>')
api.add_resource(DataItemListAPI, '/data-categories/<int:data_category_id>/data-items')
api.add_resource(DataItemAPI, '/data-categories/<int:data_category_id>/data-items/<int:data_item_id>')

api.add_resource(LawEnforcementHandbookAPI, '/transparency-reports/<int:transparency_report_id>/law-enforcement-handbook')
api.add_resource(LawEnforcementHandbookActionAPI, '/transparency-reports/<int:transparency_report_id>/law-enforcement-handbook/lea-categories/<int:handbook_category_id>/lea-actions')
api.add_resource(LawEnforcementHandbookActionCategoryAPI, '/transparency-reports/<int:transparency_report_id>/law-enforcement-handbook/lea-categories')

api.add_resource(LawEnforcementActionCategoryListAPI, '/lea-categories')
api.add_resource(LawEnforcementActionCategoryAPI, '/lea-categories/<int:lea_category_id>')
api.add_resource(LawEnforcementActionListAPI, '/lea-categories/<int:lea_category_id>/lea-actions')
api.add_resource(LawEnforcementActionAPI, '/lea-categories/<int:lea_category_id>/lea-actions/<int:lea_action_id>')

api.add_resource(GovRequestReportAPI, '/transparency-reports/<int:transparency_report_id>/gov-request-report')
api.add_resource(GovernmentRequestReportTypeAPI, '/transparency-reports/<int:transparency_report_id>/gov-request-report/gov-request-categories/<int:gov_request_category_id>/gov-request-types')

api.add_resource(GovernmentRequestCategoryListAPI, '/gov-request-categories')
api.add_resource(GovernmentRequestCategoryAPI, '/gov-request-categories/<int:gov_request_category_id>')
api.add_resource(GovernmentRequestTypeListAPI, '/gov-request-categories/<int:gov_request_category_id>/gov-request-types')
api.add_resource(GovernmentRequestTypeAPI, '/gov-request-categories/<int:gov_request_category_id>/gov-request-types/<int:gov_request_type_id>')
api.add_resource(GovernmentRequestResponseListAPI, '/gov-request-responses')
api.add_resource(GovernmentRequestResponseAPI, '/gov-request-responses/<int:gov_request_response_id>')

if __name__ == "__main__":
	threading.Timer(1.25, lambda: webbrowser.open('http://localhost:5000/app/index.html') ).start()
	app.run(debug=False)