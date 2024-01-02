import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

if (response.status_code != requests.codes.ok):
    print('cos poszlo nie tak')
else:
    print(response.json())


requestBody = {
    'title' : 'Nasz tytuł', 
    'body' : 'Treść posta',
    'userId' : 1
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=requestBody)

if (response.status_code != requests.codes.created):
    print('cos poszlo nie tak')
else:
    print(response.json())