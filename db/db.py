from ..models import models
from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv
from ..config import Config

load_dotenv()


engine = create_engine(Config.DATABASE_URI, echo=True)

session = Session(engine)

def create_stuff():
    SQLModel.metadata.create_all(engine)

create_stuff()