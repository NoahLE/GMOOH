# Parses the results from the Indeed API
from sqlalchemy import create_engine
engine = create_engine('sqlite:///')


class JobResult(Base):
    __tablename__ = 'job_result'

    id = Column(Integer, primary_key=True)

    job_title = Column(String)
    company = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    language = Column(String)
    formatted_location = Column(String)
    source = Column(String)
    date = Column(String)
    snippet = Column(String)
    url = Column(String)
    onmousedown = Column(String)
    job_key = Column(String)
    sponsored = Column(String)
    expired = Column(String)
    indeed_apply = Column(String)
    formatted_location_full = Column(String)
    formatted_relative_time = Column(String)
