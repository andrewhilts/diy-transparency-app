from sqlalchemy import Column, Integer, Boolean, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class GovernmentRequestResponse(Base):
  __tablename__ = 'government_request_responses'
  response_id=Column(Integer, primary_key=True)
  #g "total requests, contested, etc"
  name=Column(String(length=255))
  description=Column(Text)