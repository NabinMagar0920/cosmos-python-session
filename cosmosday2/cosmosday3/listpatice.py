grades = [85,92,78]
grades.append(95)
grades.remove(78)
if 92 in grades:
 total_count = len(grades)
total_sum = sum(grades)
lowest = min(grades)
highest = max(grades)

print(total_count)
print(total_sum)
print(lowest)
print(highest)