import requests

new_book = {
    "author": "00",
    "country": "00 00",
    "imageLink": "00",
    "language": "00",
    "link": "00",
    "pages": 69,
    "title": "yes",
    "year": 1939
}

response = requests.post('http://localhost:5000/books', json=new_book)

if response.status_code == 201:
    new_book = response.json()
    
    print(f"New book added: {new_book['title']} ({new_book['year']})")
else:
    print(f"An error occurred: {response.status_code}")
