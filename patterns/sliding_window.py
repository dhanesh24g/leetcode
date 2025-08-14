# Length of the longest substring
s = "abcefdagbccdbaef"

l = 0
mset = set()
longest = 0
mmap = {}

for r in range(len(s)):
    while s[r] in mset:
        mset.remove(s[l])
        l += 1

    w = r - l + 1
    longest = max(longest, w)

    mset.add(s[r])

    if w not in mmap:
        mmap[w] = mset.copy()

print(f"Longest: {longest}")
print(f"Longest String: {mmap[longest]}")