import requests

book_name = "yes"

updated_book = {
    "author": "Updated Author",
    "country": "Updated Country",
    "imageLink": "Updated Image Link",
    "language": "Updated Language",
    "link": "Updated Link",
    "pages": 1000,
    "title": "Updated Title",
    "year": 2000
}

response = requests.put(f'http://localhost:5000/books/{book_name}', json=updated_book)

if response.status_code == 200:
    updated_book = response.json()
    
    print(f"Book updated: {updated_book['title']} ({updated_book['year']})")
else:
    print(f"An error occurred: {response.status_code}")
