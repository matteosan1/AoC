import '../../../base/day.dart';
import '../../utils/utils.dart';

typedef Register = Map<String, int>;
typedef Instruction = ({String cmd, String param1, String? param2});

class Day23 extends Day {
  Day23() : super(2015, 23);

  @override
  List<Instruction> parser(dynamic rawInput) {
    List<Instruction> code = [];
    for (final line in rawInput) {
      final parts = line.split(" ");
      if (parts.length == 2) {
        code.add((cmd: parts[0], param1: parts[1], param2: null));
      } else {
        code.add((cmd: parts[0], param1: trimmed(parts[1], [',']), param2: parts[2]));
      }
    }
    return code;
  }

  void execution(List<Instruction> code, Register reg) {
    int index = 0;
    
    while (index >= 0 && index < code.length) {
      final instruction = code[index];
      int currentVal = reg[instruction.param1] ?? 0;
      switch(instruction.cmd) {
        case 'jio':
          if (currentVal == 1) {
            index += int.parse(instruction.param2!);
          } else {
            index += 1;
          }
          break;
        case 'hlf':
          reg[instruction.param1] = currentVal ~/ 2;
          index += 1;
          break;
        case 'tpl':
          reg[instruction.param1] = currentVal * 3;
          index += 1;
          break;
        case 'inc':
          reg[instruction.param1] = currentVal + 1;
          index += 1;
          break;
        case 'jmp':
          index += int.parse(instruction.param1);
          break;
        case 'jie':
          if ((currentVal % 2) == 0) {
            index += int.parse(instruction.param2!);
          } else {
            index += 1;
          }
          break;
        default:
          null;
      }
    }
  }  

  @override
  Object? part1(covariant List<Instruction> input) {
    Register reg = {'a': 0, 'b': 0};
    execution(input, reg);
    return reg['b'];
  }

  @override
  Object? part2(covariant List<Instruction> input) {
    Register reg = {'a': 1, 'b': 0};
    execution(input, reg);
    return reg['b'];
  }
}
