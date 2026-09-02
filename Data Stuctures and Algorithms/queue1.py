from collections import deque

support_tickets = deque()

support_tickets.append("ticket 01")
support_tickets.append("ticket 02")
support_tickets.append("ticket 03")

support_tickets.popleft()

for item in support_tickets:
    print(item)