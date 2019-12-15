from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    email = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.email)

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
    holder = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return "<Book(=title'%s', author='%s', year='%d', holder='%d')>" % (
            self.title, self.author, self.year, self.holder)

ed_user = User(name='Bill', fullname='Gates', email='bill@ms.com')
print( ed_user.name )
print( ed_user.fullname )
print( ed_user.email )
print(  str(ed_user.id) )

# engine = create_engine('sqlite://')
engine = create_engine('sqlite:///test.db')#, echo=True)

# Session = sessionmaker()
Session = sessionmaker(bind=engine)
session = Session()
session.add(ed_user)

Base.metadata.create_all(engine)
session.commit()

our_user = session.query(User).filter_by(name='Bill').first() 
print( our_user )
print( our_user.id )


na_book = Book(title='Narnia', author='Lewis', year='1943', holder=our_user.id)
session.add( na_book )
session.commit()

our_book = session.query(Book).filter_by(title='Narnia').first() 
print( our_book )
