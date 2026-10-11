students = [
    ['Pang', 4],
    ['Bear', 6],
    ['Rabbit', 8],
]

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)

intervals = [
    [3,5],
    [2,4],
    [1,6],
]

sorted_intervals = sorted(intervals, key=lambda x: x[0])
print(sorted_intervals)