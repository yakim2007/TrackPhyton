pages = 100
line = 50
symbols = 25
symbol_size = 4
mesto = 1.44
books = int((mesto * (1024 ** 2)) / (pages * line * symbols * symbol_size))
print("Количество книг, помещающихся на дискету:", books)
