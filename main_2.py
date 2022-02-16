# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from pprint import pprint

from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint((contacts_list))
print()

for r in range(1, len(contacts_list)):
  # print(contacts_list[r])
  sss = contacts_list[r]
  # print(str(sss).strip())
  # p = re.compile(r'(\+7|8)\s*?\(?(\d{3})\)?(\s*|\-*)?(\d{3})(-*|\s*)?(\d{2})(-*|\s*)?(\d{2})(\s*)?\(?(доб\.)?(\s*)?(\d*)\)?')
  # print(p.sub(r'+7(\2) \4-\6-\8 \10\12', str(sss)))

for r in range(1, len(contacts_list)):
  print(contacts_list[r])
  sss = contacts_list[r]
  # print(str(sss).strip())
  p = re.compile(r'(\[\')(\w*)(,|\s)*(\w*)(,|\s)(\w*)(,*|\s)*(\w*)')
  lll = p.sub(r'\1\2,\4,\6', str(sss))
  t = re.compile(r'(\+7|8)\s*?\(?(\d{3})\)?(\s*|\-*)?(\d{3})(-*|\s*)?(\d{2})(-*|\s*)?(\d{2})(\s*)?\(?(доб\.)?(\s*)?(\d*)\)?')
  ttt = t.sub(r'+7(\2)\4-\6-\8\9\10\12', str(lll))
  # ttt = t.findall(str(sss))
  # print(p.findall(str(sss)))
  # print(lll)



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
