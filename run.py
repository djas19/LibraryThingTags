import sys
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import argparse

class Book:
    pass


class Tag:
    pass


INPUT = "input.txt"
OUTPUT = "output.xlsx"
NUMBEROFTAGS = 6


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source", help="file location of sourcefile (list of ISBN separated with newlines)", default=INPUT
    )
    parser.add_argument(
        "--destination", help="Name of the output file", default=OUTPUT
    )
    parser.add_argument(
        "--numberOfTags", help="number of n most used tags to save", default=NUMBEROFTAGS
    )
    args = parser.parse_args()
    source = args.source
    destination = args.destination
    numberOfTags = args.numberOfTags
    workIds = getIDs(source)
    books = getBooks(workIds, numberOfTags)
    # books = getBooks([5403381, 92619, 1118065, 1888520, 880777, 8300098, 8384326, 8461488, 8024489], numberOfTags)
    writeToExcel(books, destination)


def getBooks(isbns, numberOfTags):
    books = []
    for i, isbn in enumerate(isbns):
        print("looking for work: {}".format(isbn))
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
        book.tags = getTags(book.workId, numberOfTags)
        books.append(book)
    return books


def getTags(workID, numberOfTags):
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
        if tag.content != '':
            tagCollection.append(tag)
        tagCollection.sort(key=lambda x: x.count, reverse=True)
    tagCollection = tagCollection[:numberOfTags]

    return tagCollection


def writeToExcel(books, output):
    print("excel parsing")
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "title")
    worksheet.write(0, 1, "ISBN")
    worksheet.write(0, 2, "workID")
    worksheet.write(0, 3, "tags")
    for i, book in enumerate(books):
        # Write some numbers, with row/column notation.
        worksheet.write(i + 1, 0, book.title)
        worksheet.write(i + 1, 1, book.isbn)
        worksheet.write(i + 1, 2, book.workId)
        tagcontentlist = []
        for tag in book.tags:
            tagcontentlist.append(tag.content)
        worksheet.write(i + 1, 3, ','.join(tagcontentlist))

    print("Writing to excel...")
    workbook.close()


def getIDs(source):
    ids = []
    with open(source, "rt") as f:
        for line in f:
            ids.append(line.strip())
    print(ids)
    return ids


if __name__ == "__main__":
    sys.exit(main())
