class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or name.strip() == "":
            raise Exception("Name must be a non-empty string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return list({c.book for c in self.contracts()})

    def sign_contract(self, book, date, royalties):  # FIXED name
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str) or title.strip() == "":
            raise Exception("Title must be a non-empty string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        return list({c.author for c in self.contracts()})


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # AUTHOR
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance")
        self._author = value

    # BOOK
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be a Book instance")
        self._book = value

    # DATE
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise Exception("date must be a non-empty string")
        self._date = value

    # ROYALTIES
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]