class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.book_list = []
        
    def add_book(self, book):
        self.book_list.append(book)
    def get_books(self):
        return self.book_list
    
    def search_books(self,author=None, title=None):
        if author != None:
            result = []
            for book in self.book_list:
               if author == book.author:
                   result.append(book)
            return result
                   
        else:
            result =[]
            for book in self.book_list:
                if title.lower() in book.title.lower():
                    result.append(book)
            return result
        


class Author(object):
    def __init__(self,name, nationality):
        self.name = name
        self.nationality = nationality
        self.book_list = []

    def add_books(self, book):
        self.book_list.append(book)
        
    def get_books(self):
        return self.book_list 
    


class Book(object):
    def __init__(self,title,author):
        self.title = title
        self.author = author
        author.add_books(self)