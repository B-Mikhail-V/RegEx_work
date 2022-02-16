def process_doubles(self):
    # short execution time
    double_name_dict = {}
    for row in self.contacts_list:
        if not double_name_dict.get(row[0] + row[1]):
            double_name_dict[row[0] + row[1]] = [row]
        else:
            double_name_dict[row[0] + row[1]].append(row)
    self.contacts_list.clear()
    for key, value in double_name_dict.items():
        while len(value) != 1:
            value.append([x or y for x, y in zip(value.pop(0), value.pop(0))])
        self.contacts_list.append(*value)
    self.contacts_list.sort()


def process_doubles_v2(self):
    # short code
    fixed_info_list = []
    for i in range(len(self.contacts_list)):
        for j in range(len(self.contacts_list)):
            if self.contacts_list[i][:2] == self.contacts_list[j][:2]:
                self.contacts_list[i] = [x or y for x, y in zip(self.contacts_list[i], self.contacts_list[j])]
        if self.contacts_list[i] not in fixed_info_list:
            fixed_info_list.append(self.contacts_list[i])
    fixed_info_list.sort()
    self.contacts_list = fixed_info_list