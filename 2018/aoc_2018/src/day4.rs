pub mod day4 {
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    pub fn solve() {
        let now = Instant::now();
        
        let res1 = part1();
        let elapsed = now.elapsed();                
        println!("{} {} ({:.2?})", utils::santa(4, 1), res1, elapsed);

        let res2 = part2();
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(4, 2), res2, elapsed);        
    }

    fn check(n: u32, part: u8) -> bool {
        let r: String = n.to_string();
        let s: &str = &r;
        let mut repeat = 1;
        let mut old = s.chars().nth(0).unwrap();
        for i in 1..s.len() {
            if s.chars().nth(i).unwrap() == old {
                repeat += 1;
            } else {
                if (part == 1 && repeat >= 2) || (part == 2 && repeat == 2) {
                    return true;
                }
                old = s.chars().nth(i).unwrap();
                repeat = 1;
            }
        }
        if (part == 1 && repeat >= 2) || (part == 2 && repeat == 2) {
            return true;
        }
        false
    }
    
    fn main_loop(part: u8) -> u32 {
        let mut counter: u32 = 0;
        for i1 in 1..6 {
            for i2 in i1..10 {
                for i3 in i2..10 {
                    for i4 in i3..10 {
                        for i5 in i4..10 {
                            for i6 in i5..10 {
                                let n: u32 = i1*100000+i2*10000+i3*1000+i4*100+i5*10+i6;
                                if n > 576723 {
                                    return counter;
                                }
                                if check(n, part) {
                                    counter += 1;
                                }
                            }
                        }
                    }
                }
            }
        }
        0
    }
    
    fn part1() -> u32 {
        main_loop(1)
    }

    fn part2() -> u32 {
        main_loop(2)
    }
}


