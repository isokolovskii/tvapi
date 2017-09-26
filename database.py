from sqlalchemy import create_engine
from config import config


engine = create_engine('{dms}+{driver}://{user}:{password}@{server}/{database}?charset={charset}'.format(**config))
