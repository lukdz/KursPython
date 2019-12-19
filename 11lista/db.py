from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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
    def to_list(self):
        return [self.id, self.name, self.fullname, self.email]

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
    holder = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return "<Book(title='%s', author='%s', year='%d', holder='%s')>" % (
            self.title, self.author, self.year, self.holder)
    def to_list(self):
        return [self.id, self.title, self.author, self.year, self.holder]
         
class Database():
    def __init__(self): 
        # engine = create_engine('sqlite://')
        # engine = create_engine('sqlite:///:memory:', echo=True)
        self.engine = create_engine('sqlite:///test.db')#, echo=True)
        Base.metadata.create_all(self.engine)

    def add_user(self, name, fullname, email):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        new_user = User(name=name, fullname=fullname, email=email)
        session.add(new_user)
        session.commit()

    def add_book(self, title, author, year):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        new_book = Book(title=title, author=author, year=year)
        session.add(new_book)
        session.commit()

    def list_books(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return list(session.query(Book))

    def list_users(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return list(session.query(User))

    def borrow(self, title, name):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        user = session.query(User).filter_by(name=name).first() 
        book = session.query(Book).filter_by(title=title).first() 
        book.holder = user.id
        session.commit()

    def back(self, title, name):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        # user = session.query(User).filter_by(name=name).first() 
        book = session.query(Book).filter_by(title=title).first() 
        book.holder = None#user.id
        session.commit()
