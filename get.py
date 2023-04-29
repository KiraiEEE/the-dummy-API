import requests
response = requests.get('http://localhost:5000/books', params={'author': 'Dante Alighieri'})

if response.status_code == 200:

    books = response.json()

    for book in books:
        print(f"{book['title']} ({book['year']})")
else:
    print(f"An error occurred: {response.status_code}")
