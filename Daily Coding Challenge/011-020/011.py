# autocomplete system
class node(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


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
print(autocomplete("c"))
print(autocomplete("d"))
print(autocomplete("de"))
