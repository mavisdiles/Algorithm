n = int(input())
nodes = list(map(int,input().split()))
target = int(input())
tree ={}

class Node:
    def __init__ (self,item):
        self.item = item
        self.left = None
        self.right = None

tree[0] = Node(0)

for i in range(1,len(nodes)):
    parent = nodes[i]
    tree[i] = Node(i)
    if tree[parent].left == None:
        tree[parent].left = i
    elif tree[parent].right == None:
        tree[parent].right =i

def delete(target):
    if tree[target].left:
        delete(tree[target].left)
    if tree[target].right:
        delete(tree[target].right)
    del(tree[target])

delete(target)

count =0
for i in tree:
    if tree[i].left == None and tree[i].right == None:
        count+=1
print(count)