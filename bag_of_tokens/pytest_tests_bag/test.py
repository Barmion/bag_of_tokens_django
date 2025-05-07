# import requests

# response = requests.post(url='http://127.0.0.1:8000/api/v1/jwt/create/',
#                          data={'username': 'admin', 'password': 'admin'})
# print(response.json())
# jwt = response.json().get('access')

# response_2 = requests.get(url='http://127.0.0.1:8000/api/v1/bag/',
#                           headers={'Authorization': f'Bearer {jwt}'})

# print(response_2.status_code)
