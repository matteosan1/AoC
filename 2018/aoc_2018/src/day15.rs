pub mod day15 {
    use rand::Rng;
    use itertools::Itertools;
    use regex::Regex;
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    fn preprocess() -> Vec::<Vec<i32>> {
        let lines = utils::read_input("../instructions15a.txt");

        let pattern = r"(-?\d)+";       
        let regex = Regex::new(pattern).unwrap();

        let mut ingredients = Vec::<Vec<i32>>::new();
        for l in lines {
            let vals = regex.find_iter(&l).map(|x| x.as_str().parse::<i32>().unwrap()).collect::<Vec<i32>>();
            ingredients.push(vals);           
        }

        ingredients
    }

    pub fn solve () {
        let ingredients = preprocess();
        
        let now = Instant::now();
        let res1 = part1(&ingredients);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::santa(15, 1), res1, elapsed);
        
        let res2 = part2(&ingredients);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(15, 2), res2, elapsed);
    }


    fn calories(ingredients: &Vec<Vec<i32>>, perm: &Vec<usize>) -> bool {
        let mut tot = 0;
        for i in 0..ingredients.len() {
            tot += (perm[i] as i32)*ingredients[i][4];
        }
        tot == 500
    }

    fn score(ingredients: &Vec<Vec<i32>>, perm: &Vec<usize>) -> i32 {
        let mut tot = 1;
        for q in 0..4 {
            let mut temp = 0;
            for i in 0..ingredients.len() {
                temp += (perm[i] as i32)*ingredients[i][q];
            }
            tot *= i32::max(0, temp);
        }
        tot
    }

    fn starting_solution(n: usize) -> Vec<usize> {
        let mut rng = rand::thread_rng();
        let mut norm = 100;
        let mut solution = vec![0; n];
     
        for i in 0..(n-1) {
            solution[i] = rng.gen_range(0..norm) as usize;
            norm -= solution[i];
        }
        solution[n-1] = norm;
        solution
    }

    fn shift_solution(ingredients: &Vec<Vec<i32>>, solution: &mut Vec<usize>,
                      c: &Vec<usize>, max_score: &mut i32) -> bool {
        if solution[c[0]] > 0 && solution[c[1]] < 100 {
            solution[c[0]] -= 1;
            solution[c[1]] += 1;
            let new_score = score(ingredients, solution);
            if new_score > *max_score {
                *max_score = new_score;
                return true;                
            } else {
                solution[c[0]] += 1;
                solution[c[1]] -= 1;
            }
        }
        false
    }
    
    fn part1(ingredients: &Vec<Vec<i32>>) -> i32 {
        let mut max_score = 0;
        for _ in 0..10 {
            let mut solution = starting_solution(ingredients.len());
            let score = score(ingredients, &solution);
            max_score = i32::max(score, max_score);
            let mut indices = vec![0; ingredients.len()];
            for i in 0..ingredients.len() {
                indices[i] = i;
            }

            let mut no_improve = false;
            while !no_improve {
                no_improve = true;
                for c in indices.clone().into_iter().combinations(2) {
                    if shift_solution(ingredients, &mut solution, &c, &mut max_score) {
                        no_improve = false;
                        break;
                    } else {
                        let c_bis = vec![c[1], c[0]];
                        if shift_solution(ingredients, &mut solution, &c_bis, &mut max_score) {
                            no_improve = false;
                            break;
                        }
                    }
                }
            }
        }
        max_score
    }
    
    fn part2(ingredients: &Vec<Vec<i32>>) -> i32 {
        let mut max_score = 0;
        let mut spoons = vec![0; 101];
        for i in 0..=100 {
            spoons[i] = i;
        }
        
        for comb in spoons.into_iter().combinations_with_replacement(ingredients.len()) {
            if comb.iter().sum::<usize>() != 100 {
                continue;
            }

            for perm in comb.into_iter().permutations(ingredients.len()).unique() {
                if !calories(ingredients, &perm) {
                    continue;
                }
                max_score = i32::max(max_score, score(ingredients, &perm));
            }
        }
        max_score
    }
}
    


