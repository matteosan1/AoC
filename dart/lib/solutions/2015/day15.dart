import '../../../base/day.dart';
import '../../utils/utils.dart';

class Ingredient {
  final String name;
  final int capacity;
  final int durability;
  final int flavor;
  final int texture;
  final int calories;

  const Ingredient(
    this.name,
    this.capacity,
    this.durability,
    this.flavor,
    this.texture,
    this.calories
  );
}

class Day15 extends Day {
  Day15() : super(2015, 15);

  @override
  List<Ingredient> parser(dynamic rawInput) {
    List<Ingredient> ingredients = [];
    for (final line in rawInput) {
      final parts = line.split(" ");      
      ingredients.add(Ingredient(trimmed(parts[0], [":"]), 
        int.parse(trimmed(parts[2], [","])),
        int.parse(trimmed(parts[4], [","])),
        int.parse(trimmed(parts[6], [","])),
        int.parse(trimmed(parts[8], [","])),
        int.parse(trimmed(parts[10], [","]))));
    }

    return ingredients;
  }

  void search(List<Ingredient> ingredients, int idx, int remaining, int cap, int dur, 
              int fla, int tex, int cal, int maxScore, {int? exactCalories}) {
    final ing = ingredients[idx];
  
    if (idx == ingredients.length - 1) {
      final finalCal = cal + remaining * ing.calories;
      if (exactCalories != null && finalCal != exactCalories) return;

      final finalCap = cap + remaining * ing.capacity;
      final finalDur = dur + remaining * ing.durability;
      final finalFla = fla + remaining * ing.flavor;
      final finalTex = tex + remaining * ing.texture;

      if (finalCap <= 0 || finalDur <= 0 || finalFla <= 0 || finalTex <= 0) return;

      final score = finalCap * finalDur * finalFla * finalTex;
      if (score > maxScore) {
        maxScore = score;
      }
      return;
    }

    for (int amount = 0; amount <= remaining; amount++) {
      search(ingredients, idx + 1, remaining - amount, cap + amount * ing.capacity, dur + amount * ing.durability,
             fla + amount * ing.flavor, tex + amount * ing.texture, cal + amount * ing.calories, maxScore);
    }
  }

  @override
  Object? part1(covariant List<Ingredient> input) {
    int totalTeaspoons = 100;
    int maxScore = 0;
    search(input, 0, totalTeaspoons, 0, 0, 0, 0, 0, maxScore);
    return maxScore;
  }

  @override
  Object? part2(covariant List<Ingredient> input) {
    int totalTeaspoons = 100;
    int exactCalories = 500;
    int maxScore = 0;
    search(input, 0, totalTeaspoons, 0, 0, 0, 0, 0, maxScore, exactCalories: exactCalories);
    return maxScore;
  }
}
