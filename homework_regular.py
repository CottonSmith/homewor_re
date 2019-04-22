import re
import csv
from pprint import pprint

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

name_pattern = re.compile('([а-яёА-ЯЁ]+)[\s,]*(а-яёА-ЯЁ]+)[\s,]*(а-яёА-ЯЁ]+)[,]')
contacts_list1 = re.sub(name_pattern, r'\1,\2,\3', contacts_list)

phone_pattern = re.compile('(\+7|8)?[\s]*\((\d+)\)\s*(\d+)[\s-]*(\d+)[\s-]*(\d+)(\d+)?')
if r'\6' in phone_pattern:
    new_contacts_list = re.sub(phone_pattern, r'+7(\2)\3-\4-\5 доб. \6', contacts_list1)
else:
    new_contacts_list = re.sub(phone_pattern, r'+7(\2)\3-\4-\5', contacts_list1)
pprint(new_contacts_list)

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contacts_list)
