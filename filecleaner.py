import os, sys
import datetime
import argparse

parser = argparse.ArgumentParser(description='File Cleaner')
parser.add_argument('-p', required=True, type=str, help = 'Input the directory you want to clean')

args = parser.parse_args()

print("Superduper File Remover v1.0 (C) Stefan")
path = args.p

filesInClaes = os.listdir(args.p)

for filNamn in filesInClaes:
   result = filNamn.find('copy')
   if result == False:
        os.remove(path + "\\" + filNamn)
        f = open("c:\\kurser\\executionlog.txt", "a")
        datetime_object = datetime.datetime.now()
        f.write(f"{datetime_object} Filen {filNamn} togs bort\n")
        f.close()