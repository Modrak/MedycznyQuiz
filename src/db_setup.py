from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base

import models.question
import models.section

engine = create_engine('sqlite:///development.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
