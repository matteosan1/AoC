pub mod day12 {
    extern crate aoc;
    use aoc::utils;

    fn preprocess(lines: &Vec<String>) -> Vec::<(String, Vec<i64>)> {
        let mut inputs: Vec<_> = Vec::<(String, Vec<i64>)>::new();
        for l in lines {
            let parts: Vec<_> = l.split_whitespace().collect();
            inputs.push((parts[0].to_string(), parts[1].split(",").map(|c| c.parse::<i64>().unwrap()).collect()));
        }
        inputs
    }

    fn numlegal(s, c) -> i64 {
        s = s.lstrip('.');
    }
    
    pub fn part1(lines: &Vec<String>) {
        preprocess(lines);
        //println!("{} {}", utils::santa(12, 1), );
    }


    pub fn part2(lines: &Vec<String>) {
        
        //println!("{} {}", utils::christmas_tree(12, 2), );
    }
}
