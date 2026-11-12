import 'dart:convert';
import 'package:crypto/crypto.dart';
import '../../../base/day.dart';
import '../../utils/input_loader.dart';


class Day04 extends Day {
  Day04() : super(2015, 4);

  @override
  dynamic loadInputData() {
    return loadInput(inputFilePath, (lines) => lines);
  }

  @override
  Object? part1(covariant String input) {
    int number = 1;
  
    while (true) {
      String data = '$input$number';
    
      var bytes = utf8.encode(data);
      var digest = md5.convert(bytes);
    
      String hash = digest.toString();
     
      if (hash.startsWith('00000')) {
        return number;
      }
    
      number++;
    }
  }

  @override
  Object? part2(covariant String input) {
    int number = 1;
  
    while (true) {
      String data = '$input$number';
    
      var bytes = utf8.encode(data);
      var digest = md5.convert(bytes);
    
      String hash = digest.toString();
     
      if (hash.startsWith('000000')) {
        return number;
      }
    
      number++;
    }
  }
}
