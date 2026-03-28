T = int(input())

for _ in range(T):
    s = input()
    a = s[0::2]   # even index
    b = s[1::2]   # odd index
    print(a, b)
