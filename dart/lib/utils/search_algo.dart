import 'dart:collection';
import 'geometry.dart';

class FloodFill {
  final Map<Point, int> grid;

  FloodFill(this.grid);

  int getBasinSize(Point start, bool Function(Point neighbor) isValid) {
    if (!grid.containsKey(start) || !isValid(start)) return 0;

    final queue = Queue<Point>();
    final visited = <Point>{start};
    queue.add(start);

    int size = 0;

    while (queue.isNotEmpty) {
      final current = queue.removeFirst();
      size++; 

      for (final dir in directions) {
        final neighbor = current + dir;

        if (grid.containsKey(neighbor) &&
            !visited.contains(neighbor) &&
            isValid(neighbor)) {          
          visited.add(neighbor);
          queue.add(neighbor);
        }
      }
    }

    return size;
  }

  Set<Point> getBasinPoints(Point start, bool Function(Point neighbor) isValid) {
    if (!grid.containsKey(start) || !isValid(start)) {
      return {};
    }

    final queue = Queue<Point>();
    final visited = <Point>{start};
    queue.add(start);

    while (queue.isNotEmpty) {
      final current = queue.removeFirst();

      for (final dir in directions) {
        final neighbor = current + dir;
        if (grid.containsKey(neighbor) &&
            !visited.contains(neighbor) &&
            isValid(neighbor)) {
          visited.add(neighbor);
          queue.add(neighbor);
        }
      }
    }

    return visited;
  }
}


class PathFindingBFS {
  static List<Point>? findPath(Point start, 
                               Point goal, 
                               bool Function(Point current, Point neighbor) isWalkable, 
                               {List<Point> allowedDirections=directions}) 
  {
    //if (!isWalkable(start) || !isWalkable(goal)) return null;
    if (start == goal) return [start];

    final queue = Queue<Point>();
    queue.add(start);

    final visited = <Point>{start};
    final cameFrom = <Point, Point>{};
    bool found = false;

    while (queue.isNotEmpty) {
      final current = queue.removeFirst();

      if (current == goal) {
        found = true;
        break;
      }
  
      for (final dir in allowedDirections) {
        final neighbor = current + dir;

        if (isWalkable(current, neighbor) && !visited.contains(neighbor)) {
          visited.add(neighbor);
          cameFrom[neighbor] = current;
          queue.add(neighbor);
        }
      }
    }

    if (!found) return null;

    final path = <Point>[];
    Point? current = goal;
    while (current != null) {
      path.add(current);
      current = cameFrom[current];
    }

    return path.reversed.toList();
  }
}