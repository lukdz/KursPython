import argparse
from db import Database

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

db = Database()

if args.add_user:
    print( 'add_user', args.name, args.fullname, args.email)
    db.add_user(args.name, args.fullname, args.email)
elif args.add_book:
    print( 'add_book', args.title, args.author, args.year)
    db.add_book(args.title, args.author, args.year)
elif args.borrow:
    print( 'borrow', args.title, args.name)
    db.borrow(args.title, args.name)
elif args.back:
    print( 'return', args.title, args.name)
    db.back(args.title, args.name)
elif args.list_books:
    print( 'list_books' )
    print( db.list_books() )
elif args.list_users:
    print( 'list_users' )
    print( db.list_users() )
else:
    print( 'else' )
    print( args )

'''
rm test.db
clear

python db_test.py --add_user --name Bill --fullname Gates --email bill@msd.com
python db_test.py --add_user --name Steve --fullname Jobs --email steve@mac.com
python db_test.py --list_users

python db_test.py --add_book --title Narnia --author Lewis --year 1943
python db_test.py --add_book --title Rings --author Tolkien --year 1983

python db_test.py --borrow --title Narnia --name Steve
python db_test.py --list_books

python db_test.py --back --title Narnia --name Steve
python db_test.py --list_books


'''