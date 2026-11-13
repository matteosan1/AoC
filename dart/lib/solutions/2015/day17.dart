import '../../../base/day.dart';

const int target = 150;

class Day17 extends Day {
  Day17() : super(2015, 17);

  @override
  List<int> parser(dynamic rawInput) {
    return rawInput.map(int.parse).toList();
  }

  @override
  Object? part1(covariant List<int> input) {
    final n = input.length;
    final dp = List.generate(n + 1, 
                             (_) => List.generate(n + 1,
                             (_) => List<int>.filled(target + 1, 0),),);

    dp[0][0][0] = 1;
    for (int i=1; i<=n; i++) {
      final c = input[i-1];
      for (int k=0; k<=i; k++) {
        for (int s=0; s<=target; s++) {
          dp[i][k][s] = dp[i-1][k][s];
          if (k >= 1 && s >= c) {
            dp[i][k][s] += dp[i-1][k-1][s-c];
          }
        }
      }
    }

    int howManyWays = 0;
    int minContainersWays = 0;
    for (int k=0; k<=n; k++) {
      if (minContainersWays == 0 && dp[n][k][target] != 0) minContainersWays = dp[n][k][target];
      howManyWays += dp[n][k][target];
    }

    part1Result = minContainersWays;
    return howManyWays;
  }

  @override
  Object? part2(covariant List<int> input) {
    return part1Result as int;
  }
}
