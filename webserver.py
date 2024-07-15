from flask import Flask, jsonify, request
app = Flask(__name__)
# Sample data
books = [
{"id": 1, "title": "Book 1", "author": "Author 1"},
{"id": 2, "title": "Book 2", "author": "Author 2"},
{"id": 3, "title": "Book 3", "author": "Author 3"}
]
# Endpoint to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)
# Endpoint to get a specific book by id

14

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book['id'] == id),
    None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Endpoint to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = {
    "id": len(books) + 1,
    "title": data['title'],
    "author": data['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201
if __name__ == '__main__':
    app.run(debug=True)