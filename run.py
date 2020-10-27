import sys
import requests
from bs4 import BeautifulSoup
import xlsxwriter


class Book:
    pass


class Tag:
    pass


def main():
    books = getBooks([5403381, 92619, 1118065, 1888520, 880777])
    writeToExcel(books)


def getBooks(isbns):
    books = []
    for isbn in isbns:
        # work: 5403381     isbn: 9789076174082
        # url = "https://www.librarything.com/isbn/{}".format(isbn)
        url = "https://www.librarything.com/work/{}".format(isbn)
        page = requests.get(url, verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find("meta", property="og:title")
        isbn = soup.find("meta", property="books:isbn")
        workID = soup.find("meta", property="og:url")
        workIDContent = workID["content"]
        workIDContentSplit = workIDContent.split("/")[4]
        book = Book()
        book.title = title["content"]
        book.isbn = isbn["content"]
        book.workId = workIDContentSplit

        print("workID: " + book.workId)
        print("isbn: " + book.isbn)
        print("title: " + book.title)
        book.tags = getTags(book.workId)
        books.append(book)
    return books


def getTags(workID):
    url = "http://www.librarything.com/ajaxinc_showbooktags.php?work={}&all=1&print=1&doit=1&lang=\"+lang".format(
        workID)
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    tags = soup.find_all("span", class_="tag")
    tagCollection = []
    for unparsedTag in tags:
        tag = Tag()
        tag.content = unparsedTag.find("a").text
        tagcounttext = unparsedTag.find("span", class_="count").text
        countString = tagcounttext[tagcounttext.find("(") + 1:tagcounttext.find(")")]
        tag.count = int(countString.replace(',', ''))
        if tag.count > 20:
            print(vars(tag))
            tagCollection.append(tag)

    return tagCollection


def writeToExcel(books):
    print("excel parsing")
    workbook = xlsxwriter.Workbook('test.xlsx')
    worksheet = workbook.add_worksheet()

    for i, book in enumerate(books):
        # Write some numbers, with row/column notation.
        worksheet.write(i, 0, book.title)
        worksheet.write(i, 1, book.isbn)
        for p, tag in enumerate(book.tags):
            worksheet.write(i, p + 2, tag.content)

    print("Writing to excel...")
    workbook.close()


if __name__ == "__main__":
    sys.exit(main())
