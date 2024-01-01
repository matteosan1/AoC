pub mod day16 {
    use std::collections::HashMap;
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    fn preprocess() -> (HashMap::<String, i32>, Vec::<HashMap::<String, i32>>) {
        let scan = HashMap::<String, i32>::from([
            (String::from("children"), 3), (String::from("cats"), 7),
            (String::from("samoyeds"), 2), (String::from("pomeranians"), 3),
            (String::from("akitas"), 0),   (String::from("vizslas"), 0),
            (String::from("goldfish"), 5), (String::from("trees"), 3),
            (String::from("cars"), 2),     (String::from("perfumes"), 1)]);
        
        let mut list = Vec::<HashMap::<String, i32>>::with_capacity(500);
        let lines = utils::read_input("../instructions16a.txt");
        for l in lines {
            let data = l.split_once(": ").unwrap().1.replace(",", " ");
            let mut temp = HashMap::<String, i32>::new();
            for part in data.split("  ") {
                let (name, val) = part.split_once(": ").unwrap();
                temp.insert(name.to_string(), val.parse::<i32>().unwrap());
            }
            list.push(temp);
        }
        (scan, list)
    }

    pub fn solve () {
        let (scan, list) = preprocess();
        
        let now = Instant::now();
        let res1 = part1(&scan, &list);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::santa(16, 1), res1, elapsed);
        
        let res2 = part2(&scan, &list);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(16, 2), res2, elapsed);
    }

    fn part1(scan: &HashMap::<String, i32>, list: &Vec::<HashMap::<String, i32>>) -> usize {
        for (i, l) in list.iter().enumerate() {
            let mut her = true;
            for (k, v) in l {
                if scan.get(k).unwrap() != v {
                    her = false;
                }
            }
            if her {
                return i+1;
            }
        }
        0
    }
    
    fn part2(scan: &HashMap::<String, i32>, list: &Vec::<HashMap::<String, i32>>) -> usize {
        for (i, l) in list.iter().enumerate() {
            let mut her = true;
            for (k, v) in l {
                if k == "cats" || k == "trees" {
                    if scan.get(k).unwrap() >= v {
                        her = false;
                    }
                } else if k == "goldfish" || k == "pomeranians" {
                    if scan.get(k).unwrap() <= v {
                        her = false;
                    }
                } else {
                    if scan.get(k).unwrap() != v {
                        her = false;
                    }
                }
            }
            if her {
                return i+1;
            }
        }
        0
    }    
}
    


