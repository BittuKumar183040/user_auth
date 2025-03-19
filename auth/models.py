from sqlalchemy import Column, Integer, String
from auth.database import engine
from auth.database import Base

class SignupModel(Base):
	__tablename__ = "signup"
	id = Column(Integer, primary_key=True, index=True)
	fullname = Column(String)
	username = Column(String, unique=True, index=True)
	password = Column(String)
	email = Column(String, unique=True, index=True)
 
Base.metadata.create_all(bind=engine)