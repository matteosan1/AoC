import '../../../base/day.dart';

class Day08 extends Day {
  Day08() : super(2015, 8);

  int countMemChar(String line) {
    const int backslash = 0x5C; // '\'
    const int quote = 0x22;     // '"'
    const int xChar = 0x78;     // 'x'

    int count = 0;

    for (int i = 0; i < line.length - 1; i++) {
      if (line.codeUnitAt(i) == backslash) {
        final next = line.codeUnitAt(i + 1);
        if (next == backslash || next == quote) {          
          i++;
        } else if (next == xChar) {          
          i += 3;
        }
      } else if (line.codeUnitAt(i) == quote) {
        i++;
      } 

      count += 1;      
    }

    return count;
  }

  @override
  Object? part1(covariant List<String> input) {
    int strLength = 0;
    int memLength = 0;
    for (var obj in input) {
      strLength += obj.length;
      memLength += countMemChar(obj);
    }
    return strLength - memLength;
  }

  int encodedLength(String line) {
    const int backslash = 0x5C; // '\'
    const int quote = 0x22;     // '"'    

    int count = line.length + 2;

    for (int i = 0; i < line.length - 1; i++) {
      final code = line.codeUnitAt(i);
      if (code == backslash || code == quote) {
        count += 1;
      }
    }
    return count;
  }

  @override
  Object? part2(covariant List<String> input) {
    int strLength = 0;
    int encLength = 0;
    for (var obj in input) {
      strLength += obj.length;
      encLength += encodedLength(obj);
    }
    return encLength - strLength;
  }
}
