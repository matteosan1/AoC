import 'dart:convert';
import 'package:crypto/crypto.dart';
import 'dart:typed_data';
import '../../../base/day.dart';
import '../../utils/input_loader.dart';


class Day04 extends Day {
  Day04() : super(2015, 4);

  @override
  dynamic loadInputData() {
    return loadInput(inputFilePath, (lines) => lines);
  }

  int findMinNumber(String secret, int zeroCount) {
    final baseBytes = utf8.encode(secret);
    int number = 1;
    
    while (true) {
      final numStr = number.toString();
      
      final dataBytes = Uint8List(baseBytes.length + numStr.length);
      dataBytes.setRange(0, baseBytes.length, baseBytes);
      
      for (int i = 0; i < numStr.length; i++) {
        dataBytes[baseBytes.length + i] = numStr.codeUnitAt(i);
      }

      final digest = md5.convert(dataBytes);
      final bytes = digest.bytes;

      if (zeroCount == 5) {
        if (bytes[0] == 0 && bytes[1] == 0 && (bytes[2] & 0xF0) == 0) return number;
      } else {
        if (bytes[0] == 0 && bytes[1] == 0 && bytes[2] == 0) return number;
      }

      number++;
    }
  }

  @override
  Object? part1(covariant String input) {
    return findMinNumber(input, 5);
    // int number = 1;
  
    // while (true) {
    //   String data = '$input$number';
    
    //   var bytes = utf8.encode(data);
    //   var digest = md5.convert(bytes);
    
    //   String hash = digest.toString();
     
    //   if (hash.startsWith('00000')) {
    //     return number;
    //   }
    
    //   number++;
    // }
  }

  @override
  Object? part2(covariant String input) {
    return findMinNumber(input, 6);
    // int number = 1;
  
    // while (true) {
    //   String data = '$input$number';
    
    //   var bytes = utf8.encode(data);
    //   var digest = md5.convert(bytes);
    
    //   String hash = digest.toString();
     
    //   if (hash.startsWith('000000')) {
    //     return number;
    //   }
    
    //   number++;
    // }
  }
}
