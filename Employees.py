import json


def employees_rewrite(sort_type):
    with open('employees.json', 'r') as file:
        json_data = json.load(file)  # -> dict
        sort_data = sorted(json_data['employees'], key=lambda x: x[sort_type])
        if type(json_data['employees'][0][sort_type]) is int:
            sort_data = sorted(json_data['employees'], key=lambda x: x[sort_type], reverse=True)
        elif sort_type not in json_data['employees'][0]:
            raise ValueError('key not found')

        with open(f'employees_{sort_type}_sorted.json', 'w') as out_file:
            json.dump(sort_data, out_file, indent=2)


employees_rewrite('salary')
employees_rewrite('firstName')
employees_rewrite('lastName')
employees_rewrite('any')
