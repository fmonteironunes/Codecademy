class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {} # {Book(Obj) ; #this user rating}
        
    def get_email(self):
        return self.email
    
    def change_email(self, address):
        self.email = address
        print("Your email was changed to", str(address))
    
    def __repr__(self):
        print("User {}, email: {}, books read : n".format(self.name, self.email))
    
    def __eq__(self, other_user):
        if (self.name == other_user.name and self.email == other_user.email):
            return 1

    def read_book(self, book, rating = None):
        self.books[book] = rating
        
    def get_average_rating(self):
        total_val = 0
        total_num = 0
        for val in self.books.values():
            if val != None:
                total_val += val
                total_num += 1
        return total_val / total_num
        
        
class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        print("This book’s ISBN has been updated to {}".format(new_isbn))
        self.isbn = new_isbn
    
    def add_rating(self, rating):
        if (rating >= 0 and rating <= 4):
            self.ratings.append(rating)
        else:
            print("Invalid rating")
    
    def __eq__(self, other_book):
        if (self.title == other_book.title and self.isbn == other_book.isbn):
            return 1
        
    def get_average_rating(self):
        total_ratings = 0
        for rating in self.ratings:
            total_ratings += rating
        return total_ratings / len(self.ratings)
    
    def __hash__(self):
        return hash((self.title, self.isbn))
    
    
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    def get_author(self):
        return self.author
    def __repr__(self):
        print("{} by {}".format(self.title, self.author))

class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
    def __repr__(self):
         print("{}, a {} manual on {}".format(self.title, self.level, self.subject))            
    
class TomeRater:
    def __init__(self):
        self.users = {} #k:v is email:User(obj)
        self.books = {} #k:v is Book(obj) : #times read
    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book
    def create_novel(self, title, author, isbn):
        new_fiction = Fiction(title, author, isbn)
        return new_fiction
    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = NonFiction(title, subject, level, isbn)
        return new_non_fiction
    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
        else:
            print("No user with email {}!".format(email))
        if book in self.books.keys():
            self.books[book] += 1
        else:
            self.books[book] = 1
        
    def add_user(self, name, email, user_books = None):
        self.users[email] = User(name, email)
        if user_books != None:
            for books in user_books:
                self.add_book_to_user(books, email)
    
    def print_catalog(self):
        for key in self.books.keys():
            print(key.title)
    
    def print_users(self):
        for value in self.users.values():
            print(value.name)
    
    def most_read_book(self):
        most_read_num = 0
        lst_book_name = ''
        for key, value in self.books.items():
            if value > most_read_num:
                most_read_num = value
                lst_book_name = key.title
        return ("The most read book was {} that was read for {} times".format(lst_book_name, most_read_num ))
    
    def highest_rated_book(self):
        highest = 0
        lst = ''
        for key in self.books.keys():
            if highest < key.get_average_rating():
                highest = key.get_average_rating()
                lst = key.title
        return ("The highest rated book was {} with a rating of {}".format(lst, highest))
    
    def most_positive_user(self):
        user_name = ''
        highest_avg = 0
        for user in self.users.values():
            if highest_avg < user.get_average_rating():
                highest_avg = user.get_average_rating()
                user_name = user.name
        return ("The highest rater user was {} with a rating of {}".format(user_name, highest_avg))
        