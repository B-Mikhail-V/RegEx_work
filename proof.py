# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from pprint import pprint

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  # print(contacts_list)
  print()


contacts_list_correct = []
for r in range(len(contacts_list)):
  # print(f'исходный {contacts_list[r]}')
  sss = str(contacts_list[r])
  # print(sss)
  pattern_phone = r"(\+7|8)\s*?\(?(\d{3})\)?(\s*|\-*)?(\d{3})(-*|\s*)?(\d{2})(-*|\s*)?(\d{2})(\s*)?\(?(доб\.)?(\s*)?(\d*)\)?"
  substitution = r"+7(\2)\4-\6-\8 \10\12"
  contacts_list_corr_temp = re.sub(pattern_phone, substitution, sss)
  pattern_phone2 = r"(\[\')(\w*)(,|\s|\',?\s?'?)(\w*)(\'?\s?,?)(\w*)(\'?,?)(\s\'\',)(\s\'\',)"
  substitution2 = r"\1\2','\4','\6',"
  contacts_list_corr_temp_2 = re.sub(pattern_phone2, substitution2, contacts_list_corr_temp)
  # print(contacts_list_corr_temp_2)
  str_for_write = f'{contacts_list_corr_temp_2}\n'
  # print(contacts_list_corr_temp_2.split(',')[3])

  with open("phonebook.csv", "a") as f:
    f.write(str_for_write)

with open("phonebook.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list_corr = list(rows)
  print(contacts_list_corr[1])
  print()


