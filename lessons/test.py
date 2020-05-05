from requests import post, get, delete

# корректный
print(post('http://localhost:5000/api/users',
           json={'name': 'sdf',
                 'surmame': 'asd',
                 'email': 'asdf',
                 'password': '123'}).json())
# name int
print(post('http://localhost:5000/api/users',
           json={'name': 1,
                 'surmame': 'asef',
                 'email': 'sdv',
                 'password': '1, 2, 3'}).json())

# получить все
print(get('http://localhost:5000/api/v2/users').json())

# получить 999 пользователя - такого нет
print(get('http://localhost:5000/api/v2/users/999').json())

# получить 1 пользователя
print(get('http://localhost:5000/api/v2/users/1').json())

# удаление 1 пользователя
print(delete('http://localhost:5000/api/v2/users/1').json())

# удаление 999 пользователя - такого нет
print(delete('http://localhost:5000/api/v2/users/999').json())
