pub mod day4 {
    use md5;
    
    extern crate aoc;
    use aoc::utils;

    pub fn part1() {
     let input = String::from("bgvyzdsv");
     let mut idx = 0;
     while idx < 1000000 {
         let s = format!("{}{:0>6}", input, idx);
         let digest = md5::compute(s);
         let hash = format!("{:x}", digest);
         if hash.starts_with("00000") {
             break;
         }
         idx += 1;
     }
     println!("{} {}", utils::santa(4, 1), idx); 
    }


    pub fn part2() {
        let input = String::from("bgvyzdsv");
        let mut idx = 0;
        while idx < 10000000 {
            let s = format!("{}{:0>6}", input, idx);
            let digest = md5::compute(s);
            let hash = format!("{:x}", digest);
            if hash.starts_with("000000") {
                break;
            }
            idx += 1;
        }
        println!("{} {}", utils::christmas_tree(4, 2), idx);
    }
}
