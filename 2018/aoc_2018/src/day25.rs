pub mod day25 {
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    pub fn solve () {
        //let lines = utils::read_input("../prova.txt");
        let now = Instant::now();
        let res1 = part1(2981, 3075);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::santa(25, 1), res1, elapsed);
    }

    fn part1(row: usize, column: usize) -> i64 {
        let mut code = 20151125;
        let factor = 252533;
        let divisor = 33554393;
        for y in 1..=column*row {
            for x in 1..=y {
                if x == 1 && y == 1 {
                    continue;
                }
                code = (code*factor)%divisor;

                if y-x+1 == row && x == column {
                    return code;
                }
            }
        }
        code
    }
}
