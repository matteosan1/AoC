pub mod day9 {
    use regex::Regex;
    use itertools::Itertools;
    use std::collections::HashMap;
    
    extern crate aoc;
    use aoc::utils;

    fn insert_location<'a>(locations: &mut HashMap::<&'a str, HashMap<&'a str, i32>>, start: &'a str, end: &'a str, dist: &str) {
        let km = dist.parse::<i32>().unwrap();
        
        if locations.contains_key(&start) {
            locations.get_mut(&start).unwrap().insert(end, km);
        } else {
            let mut temp = HashMap::<&str, i32>::new();
            temp.insert(end, km);
            locations.insert(start, temp);
        }        
    }

    pub fn part1(input: &Vec<String>) {
        let re = Regex::new(r"(\w+)\sto\s(\w+)\s=\s([0-9]+)").unwrap();
        let mut locations = HashMap::<&str, HashMap<&str, i32>>::new();
        for line in input.iter() {
            for (_, [from, to, dist]) in re.captures_iter(line).map(|c| c.extract()) {
                insert_location(&mut locations, from, to, dist);
                insert_location(&mut locations, to, from, dist);                
            }
        }
        let k: Vec<_> = locations.keys().collect();

        let mut min_distance = i32::MAX;
        for perm in k.iter().permutations(k.len()) {
            let mut dist = 0;
            for i in 0..perm.len()-1 {
                dist += locations.get(*perm[i]).unwrap().get(*perm[i+1]).unwrap();
            }
            if dist < min_distance {
                min_distance = dist;
            }
        }

        println!("{} {}", utils::santa(9, 1), min_distance);
    }
    
    pub fn part2(input: &Vec<String>) {
        let re = Regex::new(r"(\w+)\sto\s(\w+)\s=\s([0-9]+)").unwrap();
        
        let mut locations = HashMap::<&str, HashMap<&str, i32>>::new();
        for line in input.iter() {
            for (_, [from, to, dist]) in re.captures_iter(line).map(|c| c.extract()) {
                insert_location(&mut locations, from, to, dist);
                insert_location(&mut locations, to, from, dist);                
            }
        }
        let k: Vec<_> = locations.keys().collect();

        let mut max_distance = 0;
        for perm in k.iter().permutations(k.len()) {
            let mut dist = 0;
            for i in 0..perm.len()-1 {
                dist += locations.get(*perm[i]).unwrap().get(*perm[i+1]).unwrap();
            }
            if dist > max_distance {
                max_distance = dist;
            }
        }

        println!("{} {}", utils::christmas_tree(9, 2), max_distance);
    }
}
