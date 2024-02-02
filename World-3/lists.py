num = [1, 10, 15, 25, 40, 75]

num[2] = 30
# Now the list is [1, 10, 30, 25, 40, 75]

num.append(7)
# Now the list is [1, 10, 30, 25, 40, 75, 7]

num.sort(reverse=True)
# Now the list is [75, 40, 30, 25, 10, 7, 1]

num.insert(2, 0)
# Now the list is [75, 40, 0, 30, 25, 10, 7, 1]

num.pop()
# Now the list is [75, 40, 0, 30, 25, 10, 7]

print(num)
print(f'This list have {len(num)} elements.')
