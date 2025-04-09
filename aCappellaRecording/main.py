n, d = map(int, input().split())
notes = sorted(set(int(input()) for _ in range(n)))

recordings = 0
i = 0
while i < len(notes):
    start = notes[i]
    recordings += 1
    while i < len(notes) and notes[i] - start <= d:
        i += 1

print(recordings)
