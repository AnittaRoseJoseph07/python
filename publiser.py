class Publisher:
    def _init_(self, pubname):
        self.pubname = pubname

    def display(self):
        print("Publisher :", self.pubname)


class Book(Publisher):
    def _init_(self, pubname):
        Publisher._init_(self, pubname)

    def bookdetails(self):
        self.title = input("Book Name :")
        self.author = input("Book Author :")

    def display(self):
        print("Title :", self.title)
        print("Authur :", self.author)


class Python(Book):
    def _init_(self, pubname):
        Book._init_(self, pubname)

    def moredetails(self):
        self.__price = int(input("Book Price :"))
        self.__pages = int(input("Book Pages :"))

    def display(self):
        print("Publisher :", self.pubname)
        print("Title :", self.title)
        print("Author :", self.author)
        print("Price :", self.__price)
        print("Pages :", self.__pages)


o1 = Python("DC BOOKS")
o1.bookdetails()
o1.moredetails()
o1.display()
