class TrieNode(object):
    children = None
    is_word = False

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_word = False


class WordDictionary(object):
    root = None

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        cur = self.root
        for w in word:
            index = ord(w) - ord('a')
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.is_word = True

    def addWord(self, word):
        return self.add_word(word)

    def search(self, word):
        return self.help(word, self.root)

    def help(self, word, node):
        """对于正则表达式进行递归查找"""
        if not node:
            return False
        for i in range(len(word)):
            if word[i] == ".":
                print("point->.")
                for j in range(26):
                    if node.children[j]:
                        res = self.help(word[i + 1:], node.children[j])
                        if res:
                            return True
                return False
            elif 'a' <= word[i] <= 'z':
                index = ord(word[i]) - ord('a')
                print("word->", word[i], "index->", index)
                if not node.children[index]:
                    return False
                node = node.children[index]
            else:
                return False
        return True if node.is_word else False


if __name__ == '__main__':
    t = WordDictionary()
    t.addWord("bad")
    t.addWord("dad")
    t.addWord("mad")
    # print(t.search("pad"))

    # print(t.search("bad"))
    print(t.search("mad"))
    print(t.search(".ad"))
    # print(t.search("b.."))
