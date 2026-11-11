from utils import readInput

class Decoder:
    def __init__(self):
        self.decoded_msg = {}
        self.main_loop = True

#    def lv(self):
#        n = ""
#        while True:
#            pack = self.scroll(5)
#            n += pack[1:]
#            if pack[0] == "0":
#                break
#        return n
#
#

    def hexToBin(self, msg):
        binary = ""
        for c in msg:
            binary += bin(int(c, 16))[2:].zfill(4)
        return binary

    def scroll(self, req, offset, binary):
        return binary[offset:offset+req]

    def decode(self, msg):
        binary = self.hexToBin(msg)
        self.payload(binary)
        print (self.decoded_msg)

    def litteral(self, b):
        idx = 0
        n = ""
        while True:
            pack = b[idx:idx+5]
            n += pack[1:]
            idx += 5
            if pack[0] == "0":
                break
        print ("val:", int(n, 2))
        return idx

#    def skip(self, b, offset):
#        diff = 0
#        while True:
#            if offset == len(b):
#                self.main_loop = False
#                break
#            val = int(self.scroll(4, offset, b), 2)
#            if val == 0:
#                diff += 4
#                offset += diff
#            else:
#                break
#        return diff

    def payload(self, b, oper=False):
        print("total length:", len(b))
        offset = 0
        for ib in range(len(ib)):
        while True:
            if len(b) == 0:
                print ("PIPPO")
                break
            print ("a"+b[offset:]+"a")
            if offset % 4 != 0:
                diff = 4 - offset%4
                if "1" not in b[offset:offset+diff]:
                    offset += diff
            print (offset, len(b))
            print (b[offset:offset+4])
            while b[offset:] != "":
                if "1" not in b[offset:offset+4]:
                    offset += 4
                else:
                    break
            print (offset, len(b))
            
            print (b[offset:])
            if offset == len(b):
                break
            header = self.scroll(6, offset, b)
            version = int(header[:3], 2)
            id = int(header[3:6], 2)
            print (version, id)
            offset += 6
            if id == 4:
                self.decoded_msg.setdefault("LV", []).append((version, id))
                
                offset += self.litteral(b[offset:])
                #if not oper:
                #    offset += 4 - offset % 4
                #    offset += self.skip(b, offset)
                #    print (offset)
                #if offset == len(b):
                #    break
            else:
                typ = self.scroll(1, offset, b)
                offset += 1
                if typ == "0":
                    self.decoded_msg.setdefault("OP0", []).append((version, id))
                    print (self.decoded_msg)
                    length = int(self.scroll(15, offset, b), 2)
                    offset += 15
                    self.payload(b[offset:offset+length], True)
                    offset += length
                    print ("DOPO", b[offset:])
                    #
                    #offset += 4 - offset % 4
                    #offset += self.skip(b, offset)
                    #print (offset)
                    #if offset == len(b):
                    #    break
                elif typ == "1":
                    self.decoded_msg.setdefault("OP1", []).append((version, id))
                    npacks = int(self.scroll(11, offset, b), 2)
                    offset += 11
                    self.payload(b[offset:offset*11*npacks], True)
                    offset += 11*npacks
            if len(b) == 0:
                break

lines = readInput("test.txt")

d = Decoder()
for l in lines[0:2]:
    d.decode(l)
    #dec = d.decoded_msg
    #
    #ver = 0
    #for k, v in dec.items():
    #    for o in v:
    #        ver += o[0]
    #
    #print (ver)
#print (d.decoded_msg)

