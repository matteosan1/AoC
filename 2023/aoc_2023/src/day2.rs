// is it possible to improve the regex extraction ?

pub mod day2 {
    use std::collections::HashMap;
    use regex::Regex;
    
    extern crate aoc;
    use aoc::utils;

    pub fn part1(input: &Vec<String>) {
        let mut tot = 0;
        let colors = ["red", "green", "blue"];
        let game = HashMap::from([("red",12), ("green",13), ("blue", 14)]);
        let r_game = Regex::new(r"Game\s(\d+)").unwrap();
        let r = HashMap::from([("red", Regex::new(r"(\d+) red").unwrap()),
                               ("green", Regex::new(r"(\d+) green").unwrap()),
                               ("blue", Regex::new(r"(\d+) blue").unwrap())]);
        
        for l in input {
            let id = r_game.captures(l).unwrap().get(1).unwrap().as_str()
                .parse::<u16>().unwrap();
            let mut possible = true;
            for c in &colors {
                let matches = r.get(c).unwrap().captures_iter(l).map(|c| c.get(1).unwrap().as_str().parse::<u16>().unwrap()).max().unwrap();
                if matches > *game.get(c).unwrap() {
                    possible = false;
                    break;
                }
            }
            if possible {
                tot += id;
            }
        }
        println!("{} {}", utils::santa(2, 1), tot);
    }

    pub fn part2(input: &Vec<String>) {
        let r = HashMap::from([("red", Regex::new(r"(\d+) red").unwrap()),
                               ("green", Regex::new(r"(\d+) green").unwrap()),
                               ("blue", Regex::new(r"(\d+) blue").unwrap())]);

        let colors = ["red", "green", "blue"];
        let mut powers = Vec::<u32>::with_capacity(100);
        for l in input {
            let mut p = 1;
            for c in &colors {
                p *= r.get(c).unwrap().captures_iter(l).map(|c| c.get(1).unwrap().as_str().parse::<u16>().unwrap()).max().unwrap();
            }
            powers.push(p as u32);
        }
       println!("{} {}", utils::christmas_tree(2, 2), powers.iter().sum::<u32>());
    }
}
