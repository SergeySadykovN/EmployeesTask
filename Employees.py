import json
from operator import itemgetter


def employees_rewrite(sort_type):
    with open('employees.json', 'r') as file:
        json_data = json.load(file)
        print(json_data)
        sorted_data = sorted(json_data['employees'], key=itemgetter(sort_type))
        data_indent = json.dumps(sorted_data, indent=4)
        print(data_indent)

        with open(f'employees_[sort_type]_sorted.json', 'w') as outfile:
            json.dump(data_indent, outfile)


employees_rewrite('salary')
employees_rewrite('firstName')
employees_rewrite('lastName')



