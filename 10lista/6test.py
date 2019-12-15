import argparse
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

# ed_user = User(name='Bill', fullname='Gates', email='bill@ms.com')
# print( ed_user.name )
# print( ed_user.fullname )
# print( ed_user.email )
# print(  str(ed_user.id) )

# engine = create_engine('sqlite://')
# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///test.db')#, echo=True)

# Session = sessionmaker()
# Session = sessionmaker(bind=engine)
# session = Session()
# session.add(ed_user)

Base.metadata.create_all(engine)
# session.commit()

# our_user = session.query(User).filter_by(name='Bill').first() 
# print( our_user )
# print( our_user.id )


# na_book = Book(title='Narnia', author='Lewis', year='1943', holder=our_user.id)
# session.add( na_book )
# session.commit()

# our_book = session.query(Book).filter_by(title='Narnia').first() 
# print( our_book )


def add_user(name, fullname, email):
    Session = sessionmaker(bind=engine)
    session = Session()
    new_user = User(name=name, fullname=fullname, email=email)
    session.add(new_user)
    session.commit()

def add_book(title, author, year):
    Session = sessionmaker(bind=engine)
    session = Session()
    new_book = Book(title=title, author=author, year=year)
    session.add(new_book)
    session.commit()

def list_books():
    Session = sessionmaker(bind=engine)
    session = Session()
    for book in session.query(Book):
        print( book )

def list_users():
    Session = sessionmaker(bind=engine)
    session = Session()
    for user in session.query(User):
        print( user )

def borrow(title, name):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = session.query(User).filter_by(name=name).first() 
    book = session.query(Book).filter_by(title=title).first() 
    book.holder = user.id
    session.commit()

def back(title, name):
    Session = sessionmaker(bind=engine)
    session = Session()
    # user = session.query(User).filter_by(name=name).first() 
    book = session.query(Book).filter_by(title=title).first() 
    book.holder = None#user.id
    session.commit()


# PARSER
parser = argparse.ArgumentParser(description="calculate X to the power of Y")

group = parser.add_mutually_exclusive_group()
group.add_argument("--add_user", action="store_true")
group.add_argument("--add_book", action="store_true")
group.add_argument("--borrow", action="store_true")
# group.add_argument("--return", action="store_true")
group.add_argument("--back", action="store_true")
group.add_argument("--list_books", action="store_true")
group.add_argument("--list_users", action="store_true")


parser.add_argument("--name")
parser.add_argument("--fullname")
parser.add_argument("--email")
parser.add_argument("--title")
parser.add_argument("--author")
parser.add_argument("--year")


args = parser.parse_args()

if args.add_user:
    print( 'add_user' )
    print( args.name )
    print( args.fullname )
    print( args.email )
    add_user(args.name, args.fullname, args.email)
elif args.add_book:
    print( 'add_book' )
    print( args.title )
    print( args.author )
    print( args.year )
    add_book(args.title, args.author, args.year)
elif args.borrow:
    print( 'borrow' )
    print( args.title )
    print( args.name )
    borrow(args.title, args.name)
elif args.back:
    print( 'return' )
    print( args.title )
    print( args.name )
    back(args.title, args.name)
elif args.list_books:
    print( 'list_books' )
    print( list_books() )
elif args.list_users:
    print( 'list_users' )
    print( list_users() )
else:
    print( 'else' )
    print( args )

'''
python 6test.py --add_user --name Bill --fullname Gates --email bill@ms.com
python 6test.py --add_book --title narnia --author Lewis --year 1943
python 6test.py --borrow --title narnia --name Olek
python 6test.py --back --title narnia --name Olek
python 6test.py --list_books
python 6test.py --list_users
'''