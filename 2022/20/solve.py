with open("input", "r") as f:
    data = f.read().strip()

# data = """1
# 2
# -3
# 3
# -2
# 0
# 4"""

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    def __repr__(self):
        return str(self.value)

numbers = list(map(int,data.split()))
N = len(numbers)

def print_ll(ll):
    start = ll[0]
    for _ in range(N):
        print(start,end=" ")
        start = start.next
    print()

DECRYPTION_KEY = 811589153
NUM_ROUNDS = 10

# PART 1
# DECRYPTION_KEY = 1
# NUM_ROUNDS = 1

linked_list = [Node(i*DECRYPTION_KEY) for i in numbers]
for i in range(N):
    linked_list[i].prev = linked_list[(i-1)%N]
    linked_list[i].next = linked_list[(i+1)%N]

for round_num in range(NUM_ROUNDS):
    for curr in linked_list:
        # print_ll(linked_list)
        if curr.value == 0:
            continue
        pointer = curr
        if curr.value >0:
            for i in range(curr.value % (N-1)):
                pointer = pointer.next
        else:
            for i in range((-curr.value+1)%(N-1)):
                pointer = pointer.prev
        if curr == pointer:
            print("haddippa")
            continue
        curr.next.prev = curr.prev
        curr.prev.next = curr.next
        pointer.next.prev = curr
        curr.next = pointer.next
        pointer.next = curr
        curr.prev = pointer

for node_0 in linked_list:
    if node_0.value==0:
        break

thous, two_thous, three_thous = node_0, node_0, node_0
for i in range(1000%(N)):
    thous = thous.next

for i in range(2000%(N)):
    two_thous = two_thous.next
for i in range(3000%(N)):
    three_thous = three_thous.next

print(sum(i.value for i in [thous, two_thous, three_thous]))


