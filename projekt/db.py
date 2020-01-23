from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Url(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    status = Column(String)

    def __str__(self):
        return "%s %s" % (
            self.url.ljust(30), self.status)
    def __repr__(self):
        return "<Url(url='%s', status='%s')>" % (
            self.url, self.status)

# engine = create_engine('sqlite://')
# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///data/test.db')#, echo=True)

Base.metadata.create_all(engine)

def add_url(url, status):
    Session = sessionmaker(bind=engine)
    session = Session()
    new_url = Url(url=url, status=status)
    session.add(new_url)
    session.commit()
    session.close()


def list_urls():
    Session = sessionmaker(bind=engine)
    session = Session()
    urls = []
    for url in session.query(Url):
        urls.append( url )
    session.close()
    return urls

def update_status(id, status):
    Session = sessionmaker(bind=engine)
    session = Session()
    url = session.query(Url).filter_by(id=id).first() 
    url.status = status
    session.commit()
    session.close()
