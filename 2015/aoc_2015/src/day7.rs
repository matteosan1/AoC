pub mod day6 {
    use std::collections::HashMap;
    
    extern crate aoc;
    use aoc::utils;

    pub fn part1(input: &Vec<String>) {
        let mut wires = HashMap::<String, i16>::new();

        for line in input.iter() {
            let parts: Vec<_> = line.split(" -> ").collect();
            
        }
            
        //println!("{} {}", utils::santa(7, 1), tot);
    }
    
    pub fn part2(input: &Vec<String>) {
        //println!("{} {}", utils::christmas_tree(7, 2), tot);
    }
}
