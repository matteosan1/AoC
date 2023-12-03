pub mod day1 {
    extern crate aoc;
    use aoc::utils;

    pub fn part1(input: &Vec<String>) {
        let line = &input[0];
        let up = line.chars().filter(|x| *x == '(').count();     
        let down = line.chars().filter(|x| *x == ')').count();
        
        println!("{} {}", utils::santa(1, 1), up - down);
    }


    pub fn part2(input: &Vec<String>) {
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
