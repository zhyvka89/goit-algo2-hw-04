class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def put(self, word, value=None):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_symbol] = value

    def __iter__(self):
        return self._iterate(self.root, "")

    def _iterate(self, node, prefix):
        for char, child in node.items():
            if char == self.end_symbol:
                yield prefix
            else:
                yield from self._iterate(child, prefix + char)