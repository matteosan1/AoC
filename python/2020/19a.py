import re
import time
start_time = time.time()

class Check():
    def __init__(self, filename):
        self.rules = {}
        self.lines = {}
        with open(filename) as f:
            for l in f:
                l = l.split("\n")[0]
                if ":" in l:
                    items = l.split(":")
                    if '"' in items[1]:
                        self.rules[items[0]] = items[1].replace('"', '').replace(" ", "")
                    elif '|' in items[1]:
                        self.lines[items[0]] = [i.split(" ") for i in items[1][1:].split(" | ")]
                    else:
                        self.lines[items[0]] = items[1][1:].split(" ")

        #noinsert = False
        #while not noinsert:
        #    noinsert = True
        for _ in range(2):
            for k, v in self.lines.items():
                new_v = []
                for i in v:
                    if isinstance(i, list):
                        temp = []
                        for j in i:
                            try:
                                temp.append(self.rules[j])
                                noinsert = False
                            except:
                                pass
                        new_v.append(temp)
                    else:
                        try:
                            new_v.append(self.rules[i])
                            noinsert = False
                        except:
                            pass

                self.rules[k] = new_v

            #         if ":" in l:
            #             items = l.split(":")
            #             if '"' in items[1]:
            #                 self.rules[items[0]] = items[1].replace('"', '').replace(" ", "")
            #             else:
            #
            #     else:
            #         insert = False

d = Check("test_18a.txt")
print (d.rules)
#print('🎄 Part 1: {} 🎄'.format(sum(d.memory.values())))
#print("\n--- %.7s secs ---" % (time.time() - start_time))