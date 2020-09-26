import argparse
book = {"Masha": 89778881539, "Pasha": 89778081476, "Natasha": 89771231536}


parser = argparse.ArgumentParser(description='Telephon book')
parser.add_argument('-a', "--add", dest="param1")
parser.add_argument('-d', "--delete", dest="param2")
parser.add_argument('-s', "--show", dest="param3", default="all")

args = parser.parse_args()
#print(args)
if args.param1:
    name, tele = args.param1.split(":")
    if name in book:
        book[name] = [book.get(name), int(tele)]
        print("contact with name ", name, " has been updated")
        print(name, ":", book[name])
    else:
        book[name] = int(tele)
        print("contact with name ", name, "added")
        print(name, ":", book[name])

if args.param2:
    if (args.param2 in book):
        book.pop(args.param2)
        print("contact with name", args.param2, "has been deleted")
        print(book)
    else:
        print("no such contact exists")
if args.param3:
    print(book)
else: pass