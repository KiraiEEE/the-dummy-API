from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open('books.json', 'r') as file:
    books = json.load(file)

@app.route('/books', methods=['GET'])
def get_books_by_author():
    author_name = request.args.get('author')
    if author_name:
        author_books = [book for book in books if book['author'] == author_name]
        return jsonify(author_books)
    else:
        return jsonify(books)
    
# @app.route('/books', methods=['PUT'])
# def add_book():
#     new_book = request.json
#     books.append(new_book)
#     with open('books.json', 'w') as file:
#         json.dump(books, file, indent=4)
#     return jsonify(new_book), 201

@app.route('/books', methods=['POST'])
def add_book():
    book = request.json
    book_id = len(books) + 1
    book['id'] = book_id
    books.append(book)
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)
    return jsonify(book), 201

@app.route('/books', methods=['DELETE'])
def delete_book_by_name():
    book_name = request.args.get('name')
    if book_name:
        for book in books:
            if book['title'] == book_name:
                books.remove(book)
                with open('books.json', 'w') as file:
                    json.dump(books, file, indent=4)
                return jsonify(book), 200
        return 'Book not found', 404
    else:
        return 'No book name provided', 400
    
@app.route('/books/<string:book_title>', methods=['PUT'])
def update_book(book_title):
    updated_book = request.get_json()

    for book in books:
        if book['title'] == book_title:
            book.update(updated_book)
            with open('books.json', 'w') as file:
                json.dump(books, file, indent=4)
            return jsonify(book)

    return jsonify({'message': 'Book not found.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
