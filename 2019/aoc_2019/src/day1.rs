pub mod day1 {
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    pub fn solve() {
        let input = utils::read_input("../instructions1a.txt");
        
        let now = Instant::now();
        
        let res1 = part1(&input);
        let elapsed = now.elapsed();                
        println!("{} {} ({:.2?})", utils::santa(1, 1), res1, elapsed);
        
        let res2 = part2(&input);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(1, 2), res2, elapsed);        
    }
    
    fn part1(input: &Vec<String>) -> usize {
        let line = &input[0];
        let up = line.chars().filter(|x| *x == '(').count();     
        let down = line.chars().filter(|x| *x == ')').count();
        up-down
    }
    
    fn part2(input: &Vec<String>) -> usize {
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
        nchar
    }
}
