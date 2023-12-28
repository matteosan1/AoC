pub mod day1 {
    use std::time::Instant;

    //extern crate aoc;
    //use aoc::utils;
    use crate::utils;

    pub fn solve() {
        let now = Instant::now();
        let input = utils::read_input("input_13.txt");
        
        part1(&input);
        let elapsed = now.elapsed();
        println!("Elapsed: {:.2?}", elapsed); 

        part2(&input);
        let elapsed = now.elapsed();
        println!("Elapsed: {:.2?}", elapsed); 
        
    }

    fn part1(input: &Vec<String>) {
        let line = &input[0];
        let up = line.chars().filter(|x| *x == '(').count();     
        let down = line.chars().filter(|x| *x == ')').count();
        
        println!("{} {}", utils::santa(1, 1), up - down);
    }

    fn part2(input: &Vec<String>) {
        let line = &input[0];
        
        let mut floor = 0;
        let mut nchar = 1;
        for c in line.chars() {
            if c == '(' {
                floor += 1;
            } else {
                floor -= 1;
            };
            
            if floor == -1 {
                break;
            }
            nchar += 1;
        }
        
        println!("{} {}", utils::christmas_tree(1, 2), nchar);
    }
}
