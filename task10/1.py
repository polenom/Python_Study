class Library:
    def __init__(self):
        from collections import defaultdict
        self._books = defaultdict(list)

    def addbook(self, name , author= 'unknown'):
        self._books[author].append(name)
        return True

    def delbook(self,name = None , author = None):
        if author and self._books.get(author, False):
            del self._books[author]
            return True
        elif name:
            for k,v in self._books.items():
                if name in v:
                    self._books[k].remove(name)
                    return True
        return False

    def showBooks(self):
        res = []
        for i in self._books.values():
            res+=i
        return res

    def findAuthor(self,author):
        return self._books[author] if self._books.get(author, False) else False

    def findName(self, name ):
        res = [(k,v) for k,v in self._books.items() if name in v ]
        return res if res else False
