import requests

# Send a GET request to retrieve books by author name
response = requests.get('http://localhost:5000/books', params={'author': 'Dante Alighieri'})

# Check if the request was successful
if response.status_code == 200:
    # Get the list of books returned by the API
    books = response.json()
    
    # Print the title and year of each book
    for book in books:
        print(f"{book['title']} ({book['year']})")
else:
    print(f"An error occurred: {response.status_code}")
