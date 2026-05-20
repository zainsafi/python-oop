class book:
    # dunder method 1: __init__ 
    # triggered automatically a new object or instance of the class is created
    # used to initialize object attributes.
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # dunder method 2: __str__ 
    # triggered automatically when you pass the object to print() or str().
    # controls what is displayed when print(object) is used.
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # dunder method 3: __len__
    # triggered automatically when you wrap your object inside len().
    # allows the object to be used with len().
    def __len__(self):
        return self.pages

    # dunder method 4: __eq__ 
    # triggered automatically when you use the '==' operator.
    # by default, python checks memory addresses. we override it to check
    # if the actual book details match.
    # here we compare books based on title and author.
    def __eq__(self, other):
        # we ensure the other object is actually a book before comparing
        if isinstance(other, book):
            return self.title == other.title and self.author == other.author
        return False


# using the class (testing dunder methods)
# creating objects (calls __init__ automatically)
book_one = book("the hobbit", "j.r.r. tolkien", 310)
book_two = book("the hobbit", "j.r.r. tolkien", 310)
book_three = book("1984", "george orwell", 328)

print("\n--- 1. testing __str__ ---")
# instead of writing book_one.__str__(), we write print(book_one)
print(book_one)
# output: 'the hobbit' by j.r.r. tolkien

print("\n--- 2. testing __len__ ---")
# instead of writing book_a.__len__(), we use len(book_a)
print(f"the book is {len(book_one)} pages long.")
# output: the book is 310 pages long.

print("\n--- 3. testing __eq__ ---")
# instead of writing book_a.__eq__(book_b), we use the regular == operator
print(f"are book_one and book_two equal? {book_one == book_two}")
# output: true

print(f"are book_one and book_three equal? {book_one == book_three}")
# output: false
