import collections
bamboo = [1,1,1,2]

# if bamboo [1,1,1,1]
n = len(bamboo)
count = collections.Counter(bamboo)
list_set = list(set(bamboo))

list_set.sort(reverse = True)
res = [n]
i = len(list_set) - 1
while i > 0:
    res.append(n-count[list_set[i]])
    n -= count[list_set[i]]
    i -= 1

print(res)


