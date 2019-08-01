# Constructing `feet` 
feet = [128608.92408000001, 119750.65635, 122375.32826999998, 124015.74822]
feet = [int(x) for x in feet]

# Print `feet`
print(feet)

# Get all uneven distances
uneven = [x for x in feet if x%2 != 0]

# Print `uneven`
print(uneven)

# #print uneven numbers
# un_n = [feet[num] for num in uneven if num != 0]
# print(un_n)