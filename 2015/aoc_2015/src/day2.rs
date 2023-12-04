pub mod day2 {
    extern crate aoc;
    use aoc::utils;

    pub fn part1(input: &Vec<String>) {
        let area = input.iter()
            .map(|line| {
                let x: Vec<_> = line.split("x")
                    .map(|val| val.parse::<i32>().unwrap())
                    .collect();
                let a = [x[0]*x[1], x[1]*x[2], x[0]*x[2]];
                2*a.iter().sum::<i32>()+*a.iter().min().unwrap()
            }).sum::<i32>();    
        println!("{} {}", utils::santa(2, 1), area);
    }

    pub fn part2(input: &Vec<String>) {
     let length = input.iter()
         .map(|line| {
             let x: Vec<_> = line.split("x")
                 .map(|val| val.parse::<i32>().unwrap())
                 .collect();
             let a = [x[0]+x[1], x[1]+x[2], x[0]+x[2]];
             x[0]*x[1]*x[2] + *a.iter().min().unwrap()*2
         }).sum::<i32>();

        println!("{} {}", utils::christmas_tree(2, 2), length);
    }
}
