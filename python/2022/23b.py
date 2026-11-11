import time
start_time = time.time()

class LinkedListNode:
    def __init__(self, value):
        self.next = self.prev = None
        self.value = value


class CircularHashLinkedList:
    def __init__(self, values):
        self.lookup = {}
        head = prev = None
        for value in values:
            node = LinkedListNode(value)
            if not head:
                head = node
            if prev:
                prev.next = node
                node.prev = prev
            self.lookup[value] = prev = node
        head.prev = prev
        prev.next = head

    def get(self, key):
        return self.lookup[key]

    def move(self, key, destination):
        item, destination = self.lookup[key], self.lookup[destination]
        prev_next = destination.next
        item.prev.next = item.next
        item.next.prev = item.prev
        destination.next.prev = item
        destination.next = item
        item.prev = destination
        item.next = prev_next

def simulate(cups, iterations):
    chll = CircularHashLinkedList(cups)
    item = chll.get(cups[0])
    for _ in range(iterations):
        pickup = [item.next.value, item.next.next.value, item.next.next.next.value]
        destination = len(cups) if item.value == 1 else item.value - 1
        while destination in pickup:
            destination = len(cups) if destination == 1 else destination - 1
        while pickup:
            chll.move(pickup.pop(), destination)
        item = item.next
    return chll.get(1)

def part2(cups):
    one = simulate(cups + list(range(10, 10 ** 6 + 1)), 10 ** 7)
    return one.next.value * one.next.next.value


cups = "872495136"
cups = list(map(int, cups))

print('🎄 Part 2: {} 🎄'.format(part2(cups)))
print("\n--- %.7s secs ---" % (time.time() - start_time))