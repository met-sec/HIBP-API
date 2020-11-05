import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", help="SHA-1 Hash", type=str)

args = parser.parse_args()

hash = args.s.upper()
first = hash[:5]
last = hash[5:]

def shash(first, last):
    url = "https://api.pwnedpasswords.com/range/"+(first)

    response = requests.request("GET", url)

    pog=str((response.text).find(last))
    if pog == -1:
        print ("no hits")
    else:
        print (pog + " hits")


if hash == None:
    print("no hash, please try again with the -s flag")
    pass

if (hash != None):
    shash(first, last)
    pass