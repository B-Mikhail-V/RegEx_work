# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from pprint import pprint

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  # pprint(contacts_list)
  print()
for n in range(1, len(contacts_list)):
  # print(contacts_list[n])

  for p in range(2):
    # print(n, p)
    if len(contacts_list[n][p].split()) == 3:
      for i in range(2, -1, -1):
        # print(n, p, i)
        contacts_list[n][i] = contacts_list[n][p].split()[i]
      # print(contacts_list[n][p])
    elif len(contacts_list[n][p].split()) == 2:
      for i in range(1, -1, -1):
        # print(n, p, i)
        contacts_list[n][i] = contacts_list[n][p].split()[i]
    #   print(contacts_list[n][p])
    # else:
    #   print('-----')
      # print(contacts_list[n][p])

contacts_list_correct = []
for r in range(1, len(contacts_list)):
  # print(contacts_list[r])
  sss = str(contacts_list[r])
  pattern_phone = r"(\+7|8)\s*?\(?(\d{3})\)?(\s*|\-*)?(\d{3})(-*|\s*)?(\d{2})(-*|\s*)?(\d{2})(\s*)?\(?(доб\.)?(\s*)?(\d*)\)?"
  substitution = r"+7(\2)\4-\6-\8 \10\12"
  contacts_list_corr_temp = re.sub(pattern_phone, substitution, sss)
  pprint(contacts_list_corr_temp)
  with open("phonebook.csv", "w") as f:
    f.write(contacts_list_corr_temp)
    # datawriter = csv.writer(f, delimiter=',')
    # datawriter = csv.writer(f)
    # Вместо contacts_list подставьте свой список
    # datawriter.writerow(contacts_list_corr_temp)
# print(type(contacts_list_correct))
#   contacts_list_correct.append(contacts_list_corr_temp.split(','))
# pprint(contacts_list_)
# pattern_phone = r"(\+7|8)\s*?\(?(\d{3})\)?(\s*|\-*)?(\d{3})(-*|\s*)?(\d{2})(-*|\s*)?(\d{2})(\s*)?\(?(доб\.)?(\s*)?(\d*)\)?"
# pattern_phone = r"1"
# substitution = r"99999"
# contacts_list_correct = re.sub(pattern_phone, substitution, contacts_list[0])
# substitution = r"+7(\2)\4-\6-\8 \10\12"

# text_proof = "Лагунцов Иван Алексеевич,,,Минфин,,+7 (495) 913-11-11 доб. 0792"


# contacts_list[1][2] = contacts_list[1][0].split()[2]
# contacts_list[1][1] = contacts_list[1][0].split()[1]
# contacts_list[1][0] = contacts_list[1][0].split()[0]
# pprint(contacts_list)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # datawriter = csv.writer(f)
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list_correct)