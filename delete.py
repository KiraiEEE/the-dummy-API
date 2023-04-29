import requests

# Delete a book by name using the API
def delete_book_by_name(book_name):
    response = requests.delete(f'http://localhost:5000/books?name={book_name}')
    if response.status_code == 200:
        deleted_book = response.json()
        print(f'Successfully deleted book: {deleted_book["title"]}')
    elif response.status_code == 404:
        print(f'Book not found: {book_name}')
    else:
        print(f'Error deleting book: {response.status_code}')

# Delete a book by name
delete_book_by_name('Updated Title')
