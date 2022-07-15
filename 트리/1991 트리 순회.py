n = int(input())
tree = {}
pre_str =''
in_str =''
post_str =''
class node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
        
for i in range(n):
    a,b,c = input().split()
    if b=='.':
        b=None
    if c=='.':
        c=None
    tree[a] = node(a,b,c)

def preorder(root):
    global pre_str
    pre_str += root.data
    if root.left:
        preorder(tree[root.left])    
    if root.right:
        preorder(tree[root.right])

def inorder(root): 
    global in_str  
    if root.left:
        inorder(tree[root.left])  
    in_str += root.data
    if root.right:
        inorder(tree[root.right])
        
def postorder(root):    
    global post_str
    if root.left:
        postorder(tree[root.left])    
    if root.right:
        postorder(tree[root.right])
    post_str += root.data

head = tree['A']  

preorder(head)
print(pre_str)
inorder(head)
print(in_str)
postorder(head)
print(post_str)