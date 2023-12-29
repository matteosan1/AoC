pub mod day20 {
    extern crate aoc;
    use aoc::utils;

    pub solve() {
    }

    fn run() -> i64 {
        let big_num = 1000000;
        let goal = 34000000;
        let mut houses_a = vec![0 as i64; big_num];
        let mut houses_b = vec![0 as i64; big_num];

        for elf in 1..big_num {
            for idx in (elf..big_num).step_by(elf) {
                houses_a[idx] += 10 * elf as i64;
            //houses_b[elf..--:(elf+1)*50:elf] += 11 * elf
            }
            
            for idx in (elf..(elf+1)*50).step_by(elf) {
                houses_b[idx] += 11 * elf as i64;
            }
        }   
        let val = houses_a.iter().enumerate().filter(|(_i,x)| *x >= &goal).collect::<Vec<_>>()[0];
        println!("{}", val.0);
        
        let val2 = houses_b.iter().enumerate().filter(|(_i,x)| *x >= &goal).collect::<Vec<_>>()[0];
        println!("{}", val2.0);
    }

    fn part1(input: &Vec<String>) {
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
