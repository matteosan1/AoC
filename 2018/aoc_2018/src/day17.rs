pub mod day17 {
    use itertools::Itertools;
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    fn preprocess() -> Vec<i32> {
        let lines = utils::read_input("../instructions17a.txt");
        lines.iter().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>()
    }

    pub fn solve () {
        let bottles = preprocess();
        
        let now = Instant::now();
        let res1 = part1(&bottles);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::santa(17, 1), res1, elapsed);
        
        let res2 = part2(&bottles);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(17, 2), res2, elapsed);
    }

    fn part1(bottles: &Vec<i32>) -> i32 {
        let liters = 150;
        let mut combos = 0;
        for i in 1..=bottles.len() {
            for comb in bottles.into_iter().combinations(i) {
                let val = comb.into_iter().sum::<i32>();
                if val == liters {
                    combos += 1;
                }
            }
        }
         
        combos
    }
    
    fn part2(bottles: &Vec<i32>) -> i32 {
        let liters = 150;
        let mut combos = 0;
        
        for i in 1..=bottles.len() {
            for comb in bottles.into_iter().combinations(i) {
                let val = comb.into_iter().sum::<i32>();
                if val == liters {
                    combos += 1;
                }
            }
            if combos > 0 {
                break;
            }
        }
        combos
    }    
}
    


