import requests

# Get the name of the book to update from the user
book_name = "yes"

# Define the updated book data
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

# Send a PUT request to update the book
response = requests.put(f'http://localhost:5000/books/{book_name}', json=updated_book)

# Check if the request was successful
if response.status_code == 200:
    # Get the updated book returned by the API
    updated_book = response.json()
    
    # Print the title and year of the updated book
    print(f"Book updated: {updated_book['title']} ({updated_book['year']})")
else:
    print(f"An error occurred: {response.status_code}")
