# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the actual return date
d1, m1, y1 = map(int, input().split())

# Read the expected return date (due date)
d2, m2, y2 = map(int, input().split())

fine = 0

if y1 > y2:
    # Case 4: Returned after the expected year
    fine = 10000
elif y1 == y2:
    if m1 > m2:
        # Case 3: Same year, but returned after the expected month
        fine = 500 * (m1 - m2)
    elif m1 == m2:
        if d1 > d2:
            # Case 2: Same year and month, but returned after the expected day
            fine = 15 * (d1 - d2)
        # If d1 <= d2, fine remains 0
    # If m1 < m2, fine remains 0
# If y1 < y2, fine remains 0

print(fine)
