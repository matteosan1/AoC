import 'dart:collection';
import '../../../base/day.dart';

typedef Graph = Map<String, List<String>>;
typedef MemoKey = ({String start, String end});
typedef MemoTable = HashMap<MemoKey, int>;

class Day11 extends Day {
  Day11() : super(2025, 11);

  @override  
  Graph parser(dynamic rawInput) {
    final nodes = Graph();

    for (final line in rawInput) {
      if (line.trim().isEmpty) continue;
      final parts = line.split(":");
      if (parts.length < 2) continue;
      final source = parts[0].trim();
      final destinations = parts[1].trim().split(RegExp(r'\s+'));
      nodes[source] = destinations;
    }
    return nodes;
  } 

// List<List<String>> dfs(Graph nodes, {String start = "you", String end = "out"}) {
//      final allPaths = <List<String>>[];
//     void dfsHelper(String currentNode, List<String> currentPath) {
//      final newPath = List<String>.from(currentPath)..add(currentNode);   
//      if (currentNode == end) {
//              allPaths.add(newPath);
//              return;
//      }
//      if (nodes.containsKey(currentNode)) {
//              for (final neighbor in nodes[currentNode]!) {
//              if (!newPath.contains(neighbor)) {
//                      dfsHelper(neighbor, newPath);
//              }
//              }
//      }
//      }
//      dfsHelper(start, []);
//      return allPaths;
// }

  int dfsMemoized(Graph graph, String startNode, String endNode, MemoTable memo) {
    final memoKey = (start: startNode, end: endNode);

    if (memo.containsKey(memoKey)) {
        return memo[memoKey]!;
    }  

    if (startNode == endNode) {
        return 1;
    }

    if (!graph.containsKey(startNode)) {
        return 0;
    }

    int count = 0;
    for (final neighbor in graph[startNode]!) {
        count += dfsMemoized(graph, neighbor, endNode, memo);
    }

    memo[memoKey] = count;
    return count;
  }

  @override
  Object? part1(covariant Graph input) {
    final memo = MemoTable();
    final paths = dfsMemoized(input, "you", "out", memo);
    return paths;
  }

  @override
  Object? part2(covariant Graph input) {    
    final memo = MemoTable();

    final psrToDac = dfsMemoized(input, "svr", "dac", memo);
    final pdacToFft = dfsMemoized(input, "dac", "fft", memo);
    final pfftToDac = dfsMemoized(input, "fft", "dac", memo);
    final pdacToOut = dfsMemoized(input, "dac", "out", memo);
    final psrToFft = dfsMemoized(input, "svr", "fft", memo);
    final pfftToOut = dfsMemoized(input, "fft", "out", memo);

    final totalPaths = (psrToDac * pdacToFft * pfftToOut) + (psrToFft * pfftToDac * pdacToOut);
    return totalPaths;
  }
}
