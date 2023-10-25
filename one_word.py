import re

def one_name(sent_list, line):
    my_dict = {}
    my_dict['firstname'] = sent_list[0]
    if len(re.findall(r'[\w]+', line[1])) ==2:

        words = re.findall(r'[\w]+', line[1])
        my_dict['lastname'] = words[0]
        my_dict['surname'] = words[1]
        my_dict['organization'] = line[3]
        my_dict['position'] = line[4]
        my_dict['phone'] = line[5]
        my_dict['email'] = line[6]

        return my_dict
    else:
        my_dict['lastname'] = line[0]
        my_dict['firstname'] = line[1]
        my_dict['surname'] = line[2]
        my_dict['organization'] = line[3]
        my_dict['position'] = line[4]
        my_dict['phone'] = line[5]
        my_dict['email'] = line[6]

        return my_dict