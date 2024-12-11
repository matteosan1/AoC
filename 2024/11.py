import time

from math import log10

from utils import readInput, DoublyLinkedList

def loadInput():
    #lines = readInput("input_11_prova.txt")
    lines = readInput("input_11.txt")

    l = list(map(int, lines[0].split(" ")))
    stones = DoublyLinkedList()
    for s in l:
        stones.append(s)
    return stones

dirs = {0:complex(0, -1), 1:complex(1, 0),
        2:complex(0, 1), 3:complex(-1, 0)}

def rules(s):
    #print ("val: ", s)
    if s == 0:
        return 1
    oom = int(log10(s)+1)
    #print ("oom ", oom)
    if oom != 0 and oom%2 == 0:
        s1 = s//10**(oom/2)
        s2 = s - s1*10**(oom/2)
        #print (s1, s2)
        return  int(s1), int(s2)
    else:
        #print ("2024")
        return int(s*2024)

def part1(stones):
    length = 0
    for blink in range(25):
        stone = stones.head
        while True:
            new_stone = rules(stone.data)
            if type(new_stone) == int:
                stone.data = new_stone
            else:
                stone.data = new_stone[1]
                stones.before(stone, new_stone[0])
            if stone.next:
                stone = stone.next
            else:
                break
    #stones.print_list()
    return stones.length()

def part2(stones):
    length = 0
    orig_stone = stones.head
    while True:
        stone_evo = DoublyLinkedList()
        stone_evo.append(orig_stone.data)
        for blink in range(75):
            print (blink)
            s = stone_evo.head
            while True:
                new_stone = rules(s.data)
                if type(new_stone) == int:
                    s.data = new_stone
                else:
                    s.data = new_stone[1]
                    stone_evo.before(s, new_stone[0])
                if s.next:
                    s = s.next
                else:
                    break
            length += stone_evo.length()
        if orig_stone.next:
            orig_stone = orig_stone.next
        else:
            break
        
    return length
    
if __name__ == '__main__':
    title = "Day 11: Plutonian Pebbles"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")
