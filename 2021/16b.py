import sys, math

TYPE_LITERAL = 4
stack = []

def parse(stream, pos):
    global stack
    def readbits(stream, pos, num):
        out = 0
        while num > 0:
            idx = pos // 8
            bitidx = 8 - (pos & 7)
            nbits = 8 if (bitidx == 8 and num >= 8) else bitidx if num > bitidx else num
            out <<= nbits
            out += (stream[idx] & ((1 << bitidx) - 1)) >> (bitidx - nbits)
            pos += bitidx
            num -= bitidx
        return out

    origpos = pos
    ver = readbits(stream, pos, 3); pos += 3
    typ = readbits(stream, pos, 3); pos += 3
    if (typ == TYPE_LITERAL):
        literal = 0
        done = False
        while not done:
            l = readbits(stream, pos, 5); pos += 5
            done = (l & 16) == 0
            literal <<= 4
            literal += (l & 15)
        stack.append(literal)
        return {"type": "literal", "version": ver, "value": literal, "len": pos - origpos}
    else:
        ltyp = readbits(stream, pos, 1); pos += 1
        if ltyp:
            npack = readbits(stream, pos, 11); pos += 11
            literals = []
            for i in range(0, npack):
                p = parse(stream, pos); pos += p['len']
                literals.append(p)
        else:
            lenpack = readbits(stream, pos, 15); pos += 15
            literals = []
            prepos = pos
            while pos < (prepos + lenpack):
                p = parse(stream, pos); pos += p['len']
                literals.append(p)
        instructions = [
            (lambda x: sum(x)),
            (lambda x: math.prod(x)),
            (lambda x: min(x)),
            (lambda x: max(x)),
            (lambda x: 0),
            (lambda x: 1 if x[1] > x[0] else 0),
            (lambda x: 1 if x[1] < x[0] else 0),
            (lambda x: 1 if x[1] == x[0] else 0)
        ]
        stack.append(instructions[typ]([stack.pop() for i in literals]))
        return {"type": "op", "version": ver, "operator": typ, "literals": literals, "len": pos - origpos}

def process(content):
    stream = [int(content[i: i+2], 16) for i in range(0, len(content), 2)]
    parse(stream, 0)
    return stack[-1]
    
def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()[0].strip()))

if __name__ == '__main__':
    main()
