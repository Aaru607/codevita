from collections import defaultdict

def office_rostering(n, m, friendships, k):
    # Create adjacency list to represent friendships
    friends = defaultdict(list)
    for a, b in friendships:
        friends[a].append(b)
        friends[b].append(a)

    # Initialize all employees to work from office on Day 1
    attendance = [1] * n
    total_rostering = n
    day = 1

    while total_rostering < k:
        # Compute next day's attendance based on current day's status
        next_attendance = attendance[:]
        for i in range(n):
            wfo_count = sum(attendance[friend] for friend in friends[i])
            if attendance[i] == 1:
                next_attendance[i] = 1 if wfo_count == 3 else 0
            else:
                next_attendance[i] = 1 if wfo_count < 3 else 0

        # Update attendance and calculate rostering value for the day
        attendance = next_attendance
        total_rostering += sum(attendance)
        day += 1

    return day

# Input Parsing
n, m = map(int, input().split())
friendships = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())

# Output the result
print(office_rostering(n, m, friendships, k))
