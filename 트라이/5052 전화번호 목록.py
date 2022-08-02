import sys
import collections

from sqlalchemy import false
t = int(sys.stdin.readline())
    
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

for i in range(t):
    n = int(sys.stdin.readline())
    s=[]
    t = Trie()
    for j in range(n):
        number = sys.stdin.readline().strip()
        t.insert(number)
        s.append(number)
    
    flag =True
    for num in s:
        if t.search(num) == False:
            flag = False
            break
    if flag == True:
        print('YES')
    else:
        print('NO')