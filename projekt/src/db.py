from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Url(Base):
    """
    **Url database type**
    Stores unique id, url and status
    """
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    status = Column(String)

    def __str__(self):
        return "%s %s" % (
            self.url.ljust(25), self.status)
    def __repr__(self):
        return "<Url(url='%s', status='%s')>" % (
            self.url, self.status)

# engine = create_engine('sqlite://')
# engine = create_engine('sqlite:///:memory:', echo=True)
# if __name__ == '__main__':
#     engine = create_engine('sqlite:///data/test.db')#, echo=True)
# else:
#     engine = create_engine('sqlite:///../src/data/test.db')#, echo=True)
engine = create_engine('sqlite:///../data/test.db')#, echo=True)


Base.metadata.create_all(engine)

def add_url(url, status):
    """
    **Add new url to databse**
    This creates new entry in batabase with url and it's status
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    new_url = Url(url=url, status=status)
    session.add(new_url)
    session.commit()
    id = new_url.id
    session.close()
    return id


def list_urls():
    """
    **List entires from databse**
    This list all entrys from batabase with url and status
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    urls = []
    for url in session.query(Url):
        urls.insert(0, url )
    session.close()
    return urls

def update_status(id, status):
    """
    **Update entry status in databse**
    This updates entry in batabase with new status
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    url = session.query(Url).filter_by(id=id).first() 
    url.status = status
    session.commit()
    session.close()
