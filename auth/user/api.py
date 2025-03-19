import datetime
from fastapi import APIRouter
import jwt
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from auth.models import SignupModel
from auth.database import get_db

router = APIRouter()

SECRET_KEY = "b3f7_bittu"
ALGORITHM = "HS256"

class Login(BaseModel):
	username: str
	password: str

class Signup(BaseModel):
	fullname: str
	username: str
	password: str
	email: str
class Forgot(BaseModel):
  email:str
  password: str
 
def create_jwt_token(fullname:str, username: str, email: str):
	payload = {
		"fullname": fullname,
		"username": username,
		"email": email,
		"exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
	}
	token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
	return token

@router.get("/")
def self(token: str):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		return payload
	except jwt.ExpiredSignatureError:
		raise HTTPException(status_code=401, detail="Signature has expired")
	except jwt.InvalidTokenError:
		raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/login/")
def login(login: Login, db: Session = Depends(get_db)):
	user = db.query(SignupModel).filter(SignupModel.username == login.username).first()
	if user and user.password == login.password:
		token = create_jwt_token(user.fullname, user.username, user.email)
		return {"token": token, "type": "bearer"}
	raise HTTPException(status_code=401, detail="Invalid username or password")

@router.post("/register/")
def register(signup: Signup, db: Session = Depends(get_db)):
	existing_user = db.query(SignupModel).filter(SignupModel.email == signup.email).first()
	if existing_user:
		raise HTTPException(status_code=401, detail="User already exists with this email id")

	db_signup = SignupModel(**signup.model_dump())
	db.add(db_signup)
	db.commit()
	db.refresh(db_signup)
    
	return {"status": f"Hello! {signup.username}, Your Account Created Successfully", "type": "success"}

@router.post('/forgot-password/')
def forgot_password(forgot: Forgot, db: Session = Depends(get_db)):
  user = db.query(SignupModel).filter(SignupModel.email == forgot.email).first()
  if not user:
    raise HTTPException(status_code=404, detail="Email not found")
  else:
    user.password = forgot.password
    db.commit()
    return {"status": "Password updated successfully", "type": "success"}

