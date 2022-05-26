threshold = 2
point = [1,2,3]

# point是sort好的，只要找到第一个不inde[0] + threshold 的就可以了，但是为什么/2 呢

# corner case [-1] - [0] < threshold

if point[-1] - point[0] < threshold:
    print('No')

target = point[0] + threshold
l, r = 1, len(point)
while l < r:
    mid = l + (r-l)//2
    if point[mid] < target:
        l = mid + 1
    else:
        r = mid

print((l+1)//2+1)

res = 0
if l % 2 != 0:
    l += 1
for i in range(0,l+1,2):
    res += 1
print(res)