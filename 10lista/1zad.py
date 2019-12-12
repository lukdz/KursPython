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

# engine = create_engine('sqlite://')
# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///test.db')#, echo=True)

Base.metadata.create_all(engine)

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


parser = argparse.ArgumentParser(description="edit library database")

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
    print( 'add_user', args.name, args.fullname, args.email)
    add_user(args.name, args.fullname, args.email)
elif args.add_book:
    print( 'add_book', args.title, args.author, args.year)
    add_book(args.title, args.author, args.year)
elif args.borrow:
    print( 'borrow', args.title, args.name)
    borrow(args.title, args.name)
elif args.back:
    print( 'return', args.title, args.name)
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
rm test.db
clear

python 1zad.py --add_user --name Bill --fullname Gates --email bill@msd.com
python 1zad.py --add_user --name Steve --fullname Jobs --email steve@mac.com
python 1zad.py --list_users

python 1zad.py --add_book --title Narnia --author Lewis --year 1943
python 1zad.py --add_book --title Rings --author Tolkien --year 1983

python 1zad.py --borrow --title Narnia --name Steve
python 1zad.py --list_books

python 1zad.py --back --title Narnia --name Steve
python 1zad.py --list_books

'''