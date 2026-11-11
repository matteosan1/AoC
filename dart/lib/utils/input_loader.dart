import "dart:io";
import "package:path/path.dart" as path;

const String aocInputPath = r"lib\inputs\";

T loadInput<T>(String filePath, T Function(String fileContent) parser) {
    try {
  String currentPath = Directory.current.path;
  print("Path corrente: $currentPath");
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

