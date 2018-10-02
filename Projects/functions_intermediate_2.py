import sys

x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

def iterate_dictionary(dict):
    for student in dict:
        for key, val in student.items():
            sys.stdout.write(f'{key} - {val}, ')
        sys.stdout.write('\n')
iterate_dictionary(students)


def iterate_dictionary2(dict, return_key):
    for student in dict:
        for key, val in student.items():
            if key == return_key:
                sys.stdout.write(f'{key} - {val}')
        sys.stdout.write('\n')
iterate_dictionary2(students, 'first_name')



dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def iterate_dojo():
    for location in dojo.keys():
        print(len(dojo[location]),  location.upper())
        for val in dojo[location]:
            print(val)
        print()
iterate_dojo()


