friend_bio = {

    'first_name': 'sean',
    'last name': 'molloy',
    'city': 'staten island'

    }

print(friend_bio)

favorite_nums = {'steve': 6, 'jeremy': 4, 'arnold': 9, 'jorge': 10, 'keith': 5}

print(favorite_nums)

for k, v in favorite_nums.items():
    print(k + ' ' + 'favorite number is: ' + str(v))



python_terms = {

    'variable': 'hold a value',
    'dictionary': 'glossary',
    'list': 'array',
    'while_loop': 'loops until condition is met',
    'integer': 'whole number',
    'string': 'string of text',
    'print': 'prints out user input'

    }

for name, definition in python_terms.items():
    print(name.title() + ' ' + definition.title() + '.')

rivers = {

    'nile': 'egypt',
    'sahara': 'africa',
    'hudson': 'staten island'

    }

for name, location in sorted(rivers.items()):
    print(name.title() + ', is located in ' + location.title())

