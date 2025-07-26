from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise ValueError("Input must be a list of strings")

        if not strings:
            return ""

        for i, word in enumerate(strings):
            self.put(word, i)

        prefix = ""
        node = self.root

        while True:
            keys = [k for k in node.keys() if k != self.end_symbol]

            if len(keys) != 1 or self.end_symbol in node:
                break

            char = keys[0]
            prefix += char
            node = node[char]

        return prefix
    
if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""