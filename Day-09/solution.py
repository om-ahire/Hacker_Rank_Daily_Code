# Step 1: number of entries
n = int(input())

phoneBook = {}

# Step 2: store entries
for _ in range(n):
    name, number = input().split()
    phoneBook[name] = number

# Step 3: process queries
while True:
    try:
        query = input()
        if query in phoneBook:
            print(f"{query}={phoneBook[query]}")
        else:
            print("Not found")
    except:
        break
