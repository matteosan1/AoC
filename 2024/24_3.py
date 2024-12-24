with open('input_24.txt') as f:
    initials,connections = f.read().split('\n\n')

initials = [line.split(': ') for line in initials.splitlines()]
wires = {name:bool(int(num)) for name,num in initials}

connections = [line.split(' -> ') for line in connections.splitlines()]
connections = [inputs.split(' ')+[output] for inputs,output in connections]

swap_mapping = {'mnq':('XOR', frozenset({'x11', 'y11'})), 'dkt':('AND', frozenset({'x11', 'y11'})),
                'nkg':('XOR', frozenset({'x10', 'y10'})), 'qvt':('AND', frozenset({'x10', 'y10'})),
                'mrt':('XOR', frozenset({'x09', 'y09'})), 'cdw':('AND', frozenset({'x09', 'y09'})),
                'hwq':('XOR', frozenset({'x08', 'y08'})), 'vtj':('AND', frozenset({'x08', 'y08'})),
                'hjb':('XOR', frozenset({'x07', 'y07'})), 'jrv':('AND', frozenset({'x07', 'y07'})),
                'kmj':('XOR', frozenset({'x06', 'y06'})), 'wnm':('AND', frozenset({'x06', 'y06'})),
                'rvt':('XOR', frozenset({'x05', 'y05'})), 'wkt':('AND', frozenset({'x05', 'y05'})),
                'tpf':('AND', frozenset({'x04', 'y04'})), 'ptw':('XOR', frozenset({'x04', 'y04'})),
                'ngv':('XOR', frozenset({'x03', 'y03'})), 'thd':('AND', frozenset({'x03', 'y03'})),
                'vhv':('AND', frozenset({'x02', 'y02'})), 'gwm':('XOR', frozenset({'x02', 'y02'})),
                'gcq':('AND', frozenset({'y01', 'x01'})), 'wnt':('XOR', frozenset({'y01', 'x01'})),
                'z00':('XOR', frozenset({'x00', 'y00'})), 'gct':('AND', frozenset({'x00', 'y00'})),}
def swap(output):
    if output in swap_mapping:
        return swap_mapping[output]
    else:
        return output

connections = {(gate,frozenset({input1,input2})):swap(output) for input1,gate,input2,output in connections}

max_value = max(int(input_name[1:]) for gate,inputs in connections for input_name in inputs if input_name.startswith('x'))

def x(num):
    return 'x'+str(num).zfill(2)

def y(num):
    return 'y'+str(num).zfill(2)

def z(num):
    return 'z'+str(num).zfill(2)

def carry(num):
    return 'carry'+str(num).zfill(2)

def ixor(num):
    return 'xor'+str(num).zfill(2)

def iand(num):
    return 'iand'+str(num).zfill(2)

def jand(num):
    return 'jand'+str(num).zfill(2)

def XOR(i,j):
    return connections[('XOR',frozenset({i,j}))]

def AND(i,j):
    return connections[('AND',frozenset({i,j}))]

def OR(i,j):
    return connections[('OR',frozenset({i,j}))]

def get_connections(item):
    return [[connection,value] for connection,value in connections.items() if item in connection[1]]
    
mapping = {}
try:
    for i in range(max_value+1):
        if i==0:
            assert XOR(x(i),y(i)) == z(i)
            mapping[carry(i)] = AND(x(i),y(i))
        else:
            mapping[ixor(i)] = XOR(x(i),y(i))
            mapping[iand(i)] = AND(x(i),y(i))
            assert XOR(mapping[carry(i-1)],mapping[ixor(i)]) == z(i)
            mapping[jand(i)] = AND(mapping[carry(i-1)],mapping[ixor(i)])
            mapping[carry(i)] = OR(mapping[iand(i)],mapping[jand(i)])
    assert mapping[carry(max_value)] == z(max_value+1)
    
    answer = ','.join(sorted(swap_mapping))
    print(answer)
except:
    print(i)
    print (get_connections("x"+str(i-1).zfill(2)))

