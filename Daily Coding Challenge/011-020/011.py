# autocomplete system
class node(self, value):
    self.value = value
    self.nodes = {}
    self.isWordEnd = False

    def addWord(word):

        for char in word:
            if self.nodes[char] == None:
                self.nodes[char] = {}


def create_tree(words):
    root = node(words[0])


all_words = ["an", "auto", "artic", "banana", "boar", "bored",
             "clear", "can", "cool", "david", "deer", "deal", "dog"]


def autocomplete(s, words):
    words = dict[s[0].lower()]
    result = []
    for word in words:
        if word.startswith(s):
            result.append(word)
    return result


print(autocomplete("a"))
print(autocomplete("b"))
print(autocomplete("ba"))
print(autocomplete("bor"))
print(autocomplete("c"))
print(autocomplete("d"))
print(autocomplete("de"))
