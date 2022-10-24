assertList = [[{"id": 1, "parent": "root"}, {"id": 2, "parent": 1, "type": "test"},
                 {"id": 3, "parent": 1, "type": "test"}, {"id": 4, "parent": 2, "type": "test"},
                 {"id": 5, "parent": 2, "type": "test"}, {"id": 6, "parent": 2, "type": "test"},
                 {"id": 7, "parent": 4, "type": None}, {"id": 8, "parent": 4, "type": None}],
              {"id": 7, "parent": 4, "type": None},
              [{"id": 7, "parent": 4, "type": None}, {"id": 8, "parent": 4, "type": None}],
              [],
              [{"id": 4, "parent": 2, "type": "test"}, {"id": 2, "parent": 1, "type": "test"},
               {"id": 1, "parent": "root"}]
              ]


class TreeStore:

    def __init__(self, items):
        self.items = items
        self.index = {}
        self.indexChildren = {}
        for item in items:
            parent = item['parent']
            current = item['id']
            try:
                self.indexChildren[parent].extend([current])
            except KeyError:
                self.indexChildren[parent] = [current]
            self.index[item['id']] = item

    def getAll(self):
        return self.items

    def getItem(self, id_):
        return self.index[id_]

    def getChildren(self, id_):
        children = []
        try:
            for i in self.indexChildren[id_]:
                children.append(self.index[i])
            return children
        except KeyError:
            return []


    def getAllParents(self, id_):
        current_id = self.index[id_]['parent']
        chain = []
        while current_id != 'root':
            chain.append(self.index[current_id])
            current_id = self.index[current_id]['parent']
        return chain



itemss = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(itemss)
print(ts.indexChildren)

assert ts.getAll() == assertList[0]
print('1:👍')
assert ts.getItem(7) == assertList[1]
print('2:👍')
assert ts.getChildren(4) == assertList[2]
print('3:👍')
assert ts.getChildren(5) == assertList[3]
print('4:👍')
assert ts.getAllParents(7) == assertList[4]
print('5:👍')




