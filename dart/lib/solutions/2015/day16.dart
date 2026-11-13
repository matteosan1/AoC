import '../../../base/day.dart';
import '../../utils/utils.dart';

typedef Sue = Map<String, int>;
const Sue mfcsam = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
                        'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1};    

class Day16 extends Day {
  Day16() : super(2015, 16);

  @override
  List<Sue> parser(dynamic rawInput) {
    List<Sue> aunts = [];
    for (final line in rawInput) {
      final parts = line.split(" ");
      final Sue aunt = {};
      for (int i=1; i<parts.length; i++) {
        final compound = parts[i].split(": ");
        aunt[compound[0]] = int.parse(trimmed(compound[1], [","]));
      }
      aunts.add(aunt);
    }

    return aunts;
  }

  @override
  Object? part1(covariant List<Sue> input) {    
    final gifter = input.indexWhere((aunt) {      
      for (final key in aunt.keys) {
        if (aunt[key] != mfcsam[key]) return false;
      }
      return true;
    });

    return gifter + 1;  
  }

  @override
  Object? part2(covariant List<Sue> input) {
    final gifter = input.indexWhere((aunt) {      
      for (final key in aunt.keys) {
        if (key == "cats" || key == "trees") {
          if (aunt[key]! <= mfcsam[key]!) return false;
        } else if (key == "pomeranians" || key == "goldfish") {
          if (aunt[key]! >= mfcsam[key]!) return false;
        } else {
          if (aunt[key] != mfcsam[key]) return false;
        }
      }
      return true;
    });

    return gifter + 1;  
  }
}
