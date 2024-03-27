class Book:
    title: str
    author: str
    price: int
    def __init__(self, title = "a", author = "b", price = 100):
        self.title = title
        self.author = author 
        self.price = price
    
    def get_information(self):
        print(f'title: {self.title}')
        print(f'author: {self.author}')
        print(f'price: {self.price}')
    
    def total_price(self, n=10):
        total = self.price * n
        print(f'total price: {total}')

book = Book()
book.get_information()
book.total_price()