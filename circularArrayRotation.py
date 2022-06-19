import collections
n, k, q = map(int, input().split())

list = tuple(map(int, input().split()))
list1 = []


d = collections.deque(list)
d.rotate(k)

for i in range(q):
    list1.append(d[int(input())])

for i in list1:
    print(i)