pub mod day11 {
    use std::collections::HashSet;
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;
    
    pub fn solve() {
        let now = Instant::now();
        
        let res1 = part1();
        let elapsed = now.elapsed();                
        println!("{} {} ({:.2?})", utils::santa(11, 1), res1, elapsed);
        
        let res2 = part2(res1);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(11, 2), res2, elapsed);        
    }
    
    fn check_pairs(pwd: &[u8; 8]) -> bool {
        let mut pairs = HashSet::<u8>::new();
        for i in 0..pwd.len()-1 {
            if pwd[i] == pwd[i+1] {
                pairs.insert(pwd[i]);
            }
        }
        
        if pairs.len() < 2 {
            return false;
        }
        true
    }
    
    fn check_pwd(pwd: &[u8; 8]) -> bool {
        let mut ok = false;
        for i in 0..6 {
            if pwd[i+1]-1 == pwd[i] && pwd[i] == pwd[i+2]-2 {
                ok = true;
                break;
            }
        }
        
        if ok && check_pairs(pwd) {
            return true;            
        }
        false
    }

    fn increment(pwd: &mut [u8; 8]) {
        for i in (0..8).rev() {
            loop {
                pwd[i] += 1;
                if pwd[i] == b'i' || pwd[i] == b'o' || pwd[i] == b'l' {
                    continue;
                } else if pwd[i] != 123 {
                    return
                } else {
                    pwd[i] = b'a';
                    break
                }
            }
        }
    }

    fn run(pwd: &mut [u8; 8]) -> String {
        loop {
            if check_pwd(&pwd) {
                break;
            }
            increment(pwd);
        }
        
        let mut res = String::from("");
        for i in 0..8 {
            res += &format!("{}", pwd[i] as char);
        }
        res
    }
    
    fn part1() -> String {
        let mut pwd = [0u8; 8];
        for (i, c) in "vzbxkghb".chars().enumerate() {
            pwd[i] = c as u8;
        }
        run(&mut pwd)
    }
    
    pub fn part2(res2: String) -> String {
        let mut pwd = [0u8; 8];
        for (i, c) in res2.chars().enumerate() {
            pwd[i] = c as u8;
        }
        increment(&mut pwd);
        run(&mut pwd)
    }
}
