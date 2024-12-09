pub mod day1 {
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    pub fn solve() {
        let input = utils::read_input("../input_1.txt");
        let ships:Vec<i32> = input.iter().map(|x| x.parse::<i32>().unwrap()).collect(); 
        
        let now = Instant::now();
        
        let res1 = part1(&ships);
        let elapsed = now.elapsed();                
        println!("{} {} ({:.2?})", utils::santa(1, 1), res1, elapsed);
        
        let res2 = part2(&ships);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(1, 2), res2, elapsed);        
    }

    fn get_fuel(mass: i32, mut tot_fuel: i32) -> i32 {
        let new_mass = (mass/3) - 2;
        if new_mass > 0 {
            tot_fuel += new_mass;
            return get_fuel(new_mass, tot_fuel);
        } else {
            return tot_fuel;
        }
    }
    
    fn part1(ships: &Vec<i32>) -> i32 {
        let mut fuel = 0i32;
        for s in ships {
            fuel += (s/3) - 2;
        }
        fuel
    }
    
    fn part2(ships: &Vec<i32>) -> i32 {
        let mut fuel = 0i32;
        for s in ships {
            fuel += get_fuel(*s, 0);
        }
        fuel
    }
}
