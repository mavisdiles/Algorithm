import sys

n = int(sys.stdin.readline())
s ={}

for i in range(n):
    name, state = sys.stdin.readline().split()
    s[name]=state

sorted_dic = sorted(s.items(),reverse=True)

for t in sorted_dic:
    if t[1]=="enter":
        print(t[0])
