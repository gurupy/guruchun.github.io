def sortBooks(books):
    for i in range(len(books)):
        temp = ""
        for j in range(len(books)-1-i):
            if books[j] > books[j+1]:
                temp = books[j]
                books[j] = books[j+1]
                books[j+1] = temp
    return books

def extractBook(sortedBooks, basicPeriod):
    extractBooks = []
    for i in range(len(sortedBooks)):
        index = sortedBooks[i].find("_") + 1 
        year = int(sortedBooks[i][index:])
        if year > basicPeriod:
            print(year, basicPeriod)
            extractBooks.append(sortedBooks[i])

    return extractBooks


def loadData():
    bookList = [
        "Deep Learning_2018",
        "Weapons of ... _2011",
        "Computer ... _2018",
        "Bitcoin and ..._2016",
        "Code com..._2017"
    ]
    return bookList

def printBooks(books, caption):
    print("------", caption, "------")
    for index in range(0, len(books)):
        print(index+1, books[index])
    
period = 2016
books = loadData()
printBooks(books, "initial data")
books = sortBooks(books)
printBooks(books, "sorted data")
extBooks = extractBook(books, period)
printBooks(extBooks, "extracted data")
