import sys

def max_width(pattern):
    lps, j = [0] * len(pattern), 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return max(lps)

# driver
PATTERN = sys.stdin.readline().rstrip()
res = 0
for i in range(len(PATTERN)):
    res = max(res, max_width(PATTERN[i:]))
print(res)
