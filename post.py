import requests

# Define the new book data
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

# Send a PUT request to add the new book
response = requests.post('http://localhost:5000/books', json=new_book)

# Check if the request was successful
if response.status_code == 201:
    # Get the newly added book returned by the API
    new_book = response.json()
    
    # Print the title and year of the new book
    print(f"New book added: {new_book['title']} ({new_book['year']})")
else:
    print(f"An error occurred: {response.status_code}")
