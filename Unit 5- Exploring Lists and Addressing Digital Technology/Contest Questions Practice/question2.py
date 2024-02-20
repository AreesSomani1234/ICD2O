p = int(input())
c = int(input())
total_points = 0
if p > c:
    total_points += 500

p = 50*p
c = 10*c

total_points = total_points + p - c

print(total_points)



