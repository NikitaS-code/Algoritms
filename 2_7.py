n, l = map(int, input().split())
seqs = [list(map(int, input().split())) for _ in range(n)]


medians = []

for i in range(n):
    for j in range(i + 1, n):
        merged = sorted(seqs[i] + seqs[j])
        medians.append(merged[l - 1])

for m in medians:
    print(m)