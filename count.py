text = "Avni"

count = {}

for ch in text:
    if ch in count: #check if that word in dictionary or not
        count[ch] += 1
    else:
        count[ch] = 1

print(count)