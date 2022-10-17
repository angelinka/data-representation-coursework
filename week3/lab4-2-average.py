from lab4bookApi import readAllBooks

books = readAllBooks()
total = 0
count = 0

for book in books:
    total += book["Price"]
    count += 1

print ('Average of ', count, " books ", total/count)