import wikipediaapi as wiki
import wikipedia


class wikiCrawler:
    """Manages the the wikipedia side of this twitter bot application"""

    def __init__(self):
        self.wikiClient = wiki.Wikipedia("en")

    def findPath(self, inputString):
        """Takes a string in the form <start_page> -> <end_page>
        and returns a string of the list of the page titles between"""

        pages = self.getPages(inputString)
        result = self.removeDuplicates([pages[0].title] + self.twoWayCloudSearch(pages[0], pages[1]) + [pages[1].title])
        return self.format(result)

    def getPages(self, userInput):
        """Gets the start and end pages.
        
        Returns a List of WikipediaPages, where the first element is the start page and the
        second is the end page."""

        userInput = userInput.split("->")

        startPageInput = userInput[0].strip()
        endPageInput = userInput[1].strip()

        startPage = self.wikiClient.page(startPageInput) 
        if not startPage.exists():
            startPage = self.wikiClient.page(wikipedia.search(startPageInput, results = 1)[0])

        endPage = self.wikiClient.page(endPageInput) 
        if not endPage.exists():
            endPage = self.wikiClient.page(wikipedia.search(endPageInput, results = 1)[0])
        return [startPage, endPage]


    def twoWayCloudSearch(self, startPage, endPage):
        """
        Takes two wikipedia pages, returns a list of pages that link from the first
        to the last. Will likely contain duplicates.
        """

        if (endPage.title in startPage.links.keys()):
            return [startPage.title, endPage.title]

        forwardSet = set(startPage.links.keys())
        backwardSet = self.filterBacklinks(endPage.backlinks)

        intersection = forwardSet.intersection(backwardSet)

        if len(intersection) > 0:
            return [startPage.title, intersection.pop(), endPage.title]
        
        else:
            while True:
                newSet = set()
                for item in forwardSet:
                    page = self.wikiClient.page(item)
                    newSet.update(page.links.keys())
                    for link in page.links.keys():
                        if link in backwardSet:
                            return self.twoWayCloudSearch(startPage, self.wikiClient.page(link)) + self.twoWayCloudSearch(self.wikiClient.page(link), endPage)
                forwardSet.update(newSet)

                newSet = set()
                for item in backwardSet:
                    page = self.wikiClient.page(item)
                    for backlink in self.filterBacklinks(page.backlinks):
                        newSet.add(backlink)
                        if backlink in forwardSet:
                            return self.twoWayCloudSearch(startPage, self.wikiClient.page(backlink)) + self.twoWayCloudSearch(self.wikiClient.page(backlink), endPage)
                backwardSet.update(newSet)
            

    def filterBacklinks(self, backlinks):
        """Takes an interable (set? list?) of back links, removes
        anything with "user" or "wikipedia:" to hopefully only leave titles of real articles.
        returns a new set"""

        results = set()
        for val in backlinks:
            if not ("User" in val or "Wikipedia" in val or "Talk:" in val):
                results.add(val)
        return results

    def removeDuplicates(self, list):
        """Takes a list, removes duplicates while preserving order"""
        res = []
        [res.append(x) for x in list if x not in res]
        return res


    def format(self, list):
        """Takes a list, returs a string of the items of the list seperated by ->"""
        string = ''
        for i in list:
            string += i + ' -> '
        return string[:-4]
    

def main():
    crawler = wikiCrawler()
    print(crawler.findPath(input("Enter text: ")))

if __name__ == '__main__':
    main()