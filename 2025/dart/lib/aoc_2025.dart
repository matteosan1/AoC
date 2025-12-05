import "dart:io";
import "package:path/path.dart" as path;

const String aocInputPath = "C:\\shared\\AoC\\2025";

T loadInput<T>(String filePath, T Function(String fileContent) parser) {
    try {
        final file = File(path.join(aocInputPath, filePath));
        final String content = file.readAsStringSync();

        return parser(content);
    } on FileSystemException catch (e) {
        print('🚨 File System Error on $filePath: ${e.message}');
        rethrow;
    } catch (e) {
        print('❌ An unexpected error occurred: $e');
        rethrow;
    }
}

T loadMultiLines<T>(String filePath, T Function(List<String> fileContent) parser) {
    try {
        final file = File(path.join(aocInputPath, filePath));
        final List<String> content = file.readAsLinesSync();

        return parser(content);
    } on FileSystemException catch (e) {
        print('🚨 File System Error on $filePath: ${e.message}');
        rethrow;
    } catch (e) {
        print('❌ An unexpected error occurred: $e');
        rethrow;
    }
}

class Point {
  final int x;
  final int y;

  const Point(this.x, this.y);

  Point operator +(Point other) => Point(x + other.x, y + other.y);
  Point operator -(Point other) => Point(x - other.x, y - other.y);

  Point scale(int scalar) => Point(x * scalar, y * scalar);

  @override
  bool operator ==(Object other) => other is Point && x == other.x && y == other.y;

  @override
  int get hashCode => Object.hash(x, y);

  @override
  String toString() => 'Point($x, $y)';
}

const List<Point> directions = [
  Point(0, -1), // 3: Up
  Point(1, 0),  // 0: Right
  Point(0, 1),  // 1: Down
  Point(-1, 0), // 2: Left
];

const Map<int, Point> allDirections = {
    0: Point(0, 1), 1: Point(1, 1), 2: Point(1, 0), 3: Point(1, -1), 
    4: Point(0, -1), 5: Point(-1 ,-1), 6: Point(-1, 0), 7: Point(-1, 1)};

