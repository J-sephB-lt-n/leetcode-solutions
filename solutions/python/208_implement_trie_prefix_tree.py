"""A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""


class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    """
    Example Usage
    -------------
    trie = Trie()
    trie.insert("word")
    trie.search("word") # True
    trie.search("words") # True
    trie.startsWith("wo") # True
    trie.startsWith("wu") # False
    trie.insert("wo")
    trie.search("wo") # True
    """

    def __init__(self):
        self.root_node = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root_node
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode()
            current_node = current_node.children[letter]
        current_node.children["_end_marker_"] = TrieNode()

    def search(self, word: str) -> bool:
        current_node = self.root_node
        for letter in list(word) + ["_end_marker_"]:
            current_node = current_node.children.get(letter)
            if current_node is None:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root_node
        for letter in prefix:
            current_node = current_node.children.get(letter)
            if current_node is None:
                return False
        return True
