# Store word in Dictionary
# Search for word in dictionary and return true if exist

# Time Complexity- Insert O(key_length)
#                  Search O(key_length)


class Trie:
    head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        # * denotes the Trie has this word as item
        # if * doesn't exist, Trie doesn't have this word but as a path to longer word
        cur['*'] = True

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if '*' in cur:
            return True
        else:
            return False


dictionary = Trie()

dictionary.add('hi')
dictionary.add('hello')
print(Trie.head)
print(dictionary.search('hi'))
print(dictionary.search('hello'))
print(dictionary.search('hel'))
print(dictionary.search('hey'))
