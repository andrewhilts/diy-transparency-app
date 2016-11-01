from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
import os
import sqlite3
import psycopg2
from settings.database import config as dbconfig

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

def db_connect():
	return create_engine(dbconfig['db_protocol'] + dbconfig['db_url'])

def db_session_maker(engine):
	return sessionmaker(bind=engine)

def db_create_tables():
	engine=db_connect()
	Base.metadata.create_all(engine)

# def db_delete():
# 	if os.path.isfile(dbconfig['db_url']):
# 		os.remove(dbconfig['db_url'])

# def db_restore():
# 	restore_query = open('transdb-backup.sql', 'r').read()
# 	db_delete()
# 	db_create_tables()
# 	conn = sqlite3.connect(dbconfig['db_url'])
# 	c = conn.cursor()
# 	c.executescript(restore_query)
# 	conn.commit()
# 	c.close()
# 	conn.close()
