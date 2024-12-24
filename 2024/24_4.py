from dataclasses import dataclass
from enum import Enum
from typing import Callable


class Operation(Enum):
    AND = 1
    OR = 2
    XOR = 3

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


@dataclass
class Gate:
    left: str
    right: str
    output_wire: str
    operation: Operation

    def perform_operation(self, wires: dict[str, int]) -> int:
        left, right = wires.get(self.left), wires.get(self.right)
        if left is None:
            return -1

        if right is None:
            return -2

        if self.operation == Operation.AND:
            return left & right
        elif self.operation == Operation.OR:
            return left | right
        elif self.operation == Operation.XOR:
            return left ^ right
        else:
            raise ValueError(f"Invalid operation: {self.operation}")


def find_value(value: str, wires: dict[str, int], gates: list[Gate]) -> int:
    if value.isdigit():
        return int(value)

    for g in gates:
        if g.output_wire == value:
            result = g.perform_operation(wires)
            if result == -1:
                left_value = find_value(g.left, wires, gates)
                wires[g.left] = left_value
                return find_value(value, wires, gates)

            elif result == -2:
                right_value = find_value(g.right, wires, gates)
                wires[g.right] = right_value
                return find_value(value, wires, gates)

            return result

    return -1


def gates_wires(file_name: str) -> tuple[dict[str, int], list[Gate]]:
    wires, g = open(file_name).read().split("\n\n")
    wires = {w.split(":")[0]: int(w.split(":")[1]) for w in wires.strip().split("\n")}
    gates = []
    for gate in [wire for wire in g.strip().split("\n")]:
        left, operation, right, _, output_wire = gate.split(" ")
        gates.append(Gate(left, right, output_wire, Operation[operation.upper()]))
    #print (wires, gates)
    return wires, gates


def get_number(
    filt: Callable[[str], bool], wires: dict[str, int], gates: list[Gate]
) -> int:
    for gate in gates:
        result = gate.perform_operation(wires)
        if result == -1 or result == -2:
            result = find_value(gate.output_wire, wires, gates)
            if result == -1 or result == -2:
                assert False, f"Should never happen: {result}"

        wires[gate.output_wire] = result

    num = 0

    for key in sorted(filter(filt, wires.keys()), reverse=True):
        num = (num << 1) | wires[key]

    return num


def part_1() -> int:
    wires, gates = gates_wires("input.txt")
    return get_number(lambda x: x.startswith("z"), wires, gates)

def find_output_wire(
    left: str, right: str, operation: Operation, gates: list[Gate]
) -> str | None:
    for g in gates:
        if g.left == left and g.right == right and g.operation == operation:
            return g.output_wire

        if g.left == right and g.right == left and g.operation == operation:
            return g.output_wire

    return None


def full_adder_logic(
    x: str, y: str, c0: str | None, gates: list[Gate], swapped: list
) -> tuple[str | None, str | None]:
    """
    Full Adder Logic:
    A full adder adds three one-bit numbers (X1, Y1, and carry-in C0) and outputs a sum bit (Z1) and a carry-out bit (C1).
    The logic for a full adder is as follows:
    - X1 XOR Y1 -> M1 (intermediate sum)
    - X1 AND Y1 -> N1 (intermediate carry)
    - C0 AND M1 -> R1 (carry for intermediate sum)
    - C0 XOR M1 -> Z1 (final sum)
    - R1 OR N1 -> C1 (final carry)

    Args:
    - x: input wire x
    - y: input wire y
    - c0: input carry
    - gates: list of gates
    - swapped: list of swapped wires

    Returns:
    - z1: final sum
    - c1: final carry

    References:
    - https://www.geeksforgeeks.org/full-adder/
    - https://www.geeksforgeeks.org/carry-look-ahead-adder/
    - https://en.wikipedia.org/wiki/Adder_(electronics)#Full_adder
    """

    # X1 XOR Y1 -> M1 (intermediate sum)
    m1 = find_output_wire(x, y, Operation.XOR, gates)

    # X1 AND Y1 -> N1 (intermediate carry)
    n1 = find_output_wire(x, y, Operation.AND, gates)

    assert m1 is not None, f"m1 is None for {x}, {y}"
    assert n1 is not None, f"n1 is None for {x}, {y}"

    if c0 is not None:
        # C0 AND M1 -> R1 (carry for intermediate sum)
        r1 = find_output_wire(c0, m1, Operation.AND, gates)
        if not r1:
            n1, m1 = m1, n1
            swapped.append(m1)
            swapped.append(n1)
            r1 = find_output_wire(c0, m1, Operation.AND, gates)

        # C0 XOR M1 -> Z1 (final sum)
        z1 = find_output_wire(c0, m1, Operation.XOR, gates)

        if m1 and m1.startswith("z"):
            m1, z1 = z1, m1
            swapped.append(m1)
            swapped.append(z1)

        if n1 and n1.startswith("z"):
            n1, z1 = z1, n1
            swapped.append(n1)
            swapped.append(z1)

        if r1 and r1.startswith("z"):
            r1, z1 = z1, r1
            swapped.append(r1)
            swapped.append(z1)

        assert r1 is not None, f"r1 is None for {c0}, {m1}"
        assert n1 is not None, f"n1 is None for {c0}, {m1}"

        # R1 OR N1 -> C1 (final carry)
        c1 = find_output_wire(r1, n1, Operation.OR, gates)
    else:
        z1 = m1
        c1 = n1

    return z1, c1


def part_2() -> str:
    wires, gates = gates_wires("input_24.txt")
    # Risultato finale
    get_number(lambda x: x.startswith("z"), wires, gates)

    c0 = None  # carry
    swapped = []  # list of swapped wires

    bits = len([wire for wire in wires if wire.startswith("x")])
    for i in range(bits):
        n = str(i).zfill(2)
        x = f"x{n}"
        y = f"y{n}"

        z1, c1 = full_adder_logic(x, y, c0, gates, swapped)

        if c1 and c1.startswith("z") and c1 != "z45":
            c1, z1 = z1, c1
            swapped.append(c1)
            swapped.append(z1)

        # update carry
        c0 = c1 if c1 else find_output_wire(x, y, Operation.AND, gates)

    return ",".join(sorted(swapped))

print(part_2())