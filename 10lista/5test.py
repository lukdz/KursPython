import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")

group = parser.add_mutually_exclusive_group()
group.add_argument("-a", "--add", action="store_true")
group.add_argument("-b", "--borrow", action="store_true")
# group.add_argument("-r", "--return", action="store_true")
group.add_argument("-r", "--back", action="store_true")

parser.add_argument("--name")
parser.add_argument("--fullname")
parser.add_argument("--email")
parser.add_argument("--title")
parser.add_argument("--author")
parser.add_argument("--year")


args = parser.parse_args()

if args.add:
    print( 'add' )
    print( args.title )
    print( args.author )
    print( args.year )
elif args.borrow:
    print( 'borrow' )
    print( args.title )
    print( args.name )
elif args.back:
    print( 'return' )
    print( args.title )
    print( args.name )
else:
    print( 'else' )
    print( args )

'''
python 5test.py --add --title narnia --author Lewis --year 1943
python 5test.py --borrow --title narnia --name Olek
python 5test.py --return --title narnia --name Olek
'''