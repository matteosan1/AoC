import '../../../base/day.dart';

class Day01 extends Day {
  Day01() : super(2025, 1);

  // @override  
  // dynamic loadInputData() {
  //   return loadInput(inputFilePath, (content) {
  //     return content.split('\n\n'); 
  //   });
  // }

  int countZerosInRotation(int startPos, String direction, int distance) {
      int clicksToFirstZero;

      if (direction == 'R') {
          clicksToFirstZero = 100 - startPos;
      } else if (direction == 'L') {
          clicksToFirstZero = (startPos == 0) ? 100 : (startPos);
      } else {
          return 0;
      }

      if (distance == 0) {
          return 0;
      }
    
      if (distance >= clicksToFirstZero) {
          int zeroCount = 1;
          int remainingDistance = distance - clicksToFirstZero;

          zeroCount += remainingDistance ~/ 100;
          return zeroCount;
      }
    
      return 0;
  }

  @override
  Object? part1(covariant List<String> input) {
    int counts = 0;
    int pos = 50;

    for (String r in input) {
        String dir = r[0];
        int val = int.parse(r.substring(1));

        if (dir == "L") {
            pos -= val;
        } else {
            pos += val;
        }

        pos %= 100;

        if (pos == 0) {
            counts += 1;
        }
    }    
    return counts;
  }

  @override
  Object? part2(covariant List<String> input) {
    int currentPos = 50;
    int totalZeros = 0;

    for (String rotation in input) {
        String direction = rotation[0];
        int distance = int.parse(rotation.substring(1));

        int zerosHit = countZerosInRotation(currentPos, direction, distance);
        totalZeros += zerosHit;
    
        if (direction == 'R') {
            currentPos = (currentPos + distance) % 100;
        } else if (direction == 'L') {
            currentPos = (currentPos - distance) % 100;
        }
    }
    return totalZeros;
  }
}
