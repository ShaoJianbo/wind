class TrieNode(object):
    is_word = False
    children = None

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_word = False


class Trie:

    root = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord("a")
            # print("index->", index)
            if cur.children[index] is None:
                cur.children[index] = TrieNode()
            # 执行当前的节点
            cur = cur.children[index]
        cur.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for w in word:
            index = ord(w) - ord('a')
            if cur.children[index]:
                cur = cur.children[index]
            else:
                return False
        return cur and cur.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given
        prefix.
        """
        cur = self.root
        for pre in prefix:
            index = ord(pre) - ord('a')
            if cur.children[index]:
                cur = cur.children[index]
            else:
                return False
        return True


if __name__ == '__main__':
    trie = Trie()

    res = trie.insert("apple")
    print(res)

    res = trie.search("apple")
    print(res)

    res = trie.search("app")
    print(res)

    res = trie.startsWith("app")
    print(res)

    res = trie.insert("app")
    print(res)

    res = trie.search("app")
    print(res)

