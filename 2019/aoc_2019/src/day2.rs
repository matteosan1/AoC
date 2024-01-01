pub mod day2 {
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    pub fn solve() {
        let input = utils::read_input("../instructions2a.txt");
        
        let now = Instant::now();
        
        let res1 = part1(&input);
        let elapsed = now.elapsed();                
        println!("{} {} ({:.2?})", utils::santa(2, 1), res1, elapsed);
        
        let res2 = part2(&input);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(2, 2), res2, elapsed);        
    }

    fn part1(input: &Vec<String>) -> i32 {
        let area = input.iter()
            .map(|line| {
                let x: Vec<_> = line.split("x")
                    .map(|val| val.parse::<i32>().unwrap())
                    .collect();
                let a = [x[0]*x[1], x[1]*x[2], x[0]*x[2]];
                2*a.iter().sum::<i32>()+*a.iter().min().unwrap()
            }).sum::<i32>();
        area
    }

    pub fn part2(input: &Vec<String>) -> i32 {
     let length = input.iter()
         .map(|line| {
             let x: Vec<_> = line.split("x")
                 .map(|val| val.parse::<i32>().unwrap())
                 .collect();
             let a = [x[0]+x[1], x[1]+x[2], x[0]+x[2]];
             x[0]*x[1]*x[2] + *a.iter().min().unwrap()*2
         }).sum::<i32>();
        length
    }
}
