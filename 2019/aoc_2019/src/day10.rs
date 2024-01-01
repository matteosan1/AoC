pub mod day10 {
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;
    
    pub fn solve () {
        let now = Instant::now();

        let (a, b) = run();
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::santa(10, 1), a, elapsed);

        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(10, 2), b, elapsed);
    }
    
    fn run() -> (usize, usize) {
        let big_num = 1000000;
        let goal = 34000000;
        let mut houses_a = vec![0 as i64; big_num];
        let mut houses_b = vec![0 as i64; big_num];
        
        for elf in 1..big_num {
            for idx in (elf..big_num).step_by(elf) {
                houses_a[idx] += 10 * elf as i64;
            }
            
            for idx in (elf..usize::min(big_num, (elf+1)*50)).step_by(elf) {
                houses_b[idx] += 11 * elf as i64;
            }
        }   
        let val = houses_a.iter().enumerate().filter(|(_i,x)| *x >= &goal).collect::<Vec<_>>()[0];
        let val2 = houses_b.iter().enumerate().filter(|(_i,x)| *x >= &goal).collect::<Vec<_>>()[0];
        
        (val.0, val2.0)
    }
}
