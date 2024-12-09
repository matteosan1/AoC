pub mod day13 {
    use std::collections::HashMap;
    use itertools::Itertools;
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    fn preprocess() -> (Vec<String>, HashMap::<(String, String), i32>) {
        let lines = utils::read_input("../instructions13a.txt");
        let mut hosts = Vec::<String>::new();
        let mut opinions = HashMap::<(String, String), i32>::new();
        for l in lines {
            let parts = l[0..l.len()-1].split_whitespace().collect::<Vec<&str>>();
            let mut val = parts[3].parse::<i32>().unwrap();
            if l.contains("lose") {
                val *= -1;
            }
            let host = parts[0].to_string();
            if !hosts.contains(&host) {
                hosts.push(host.clone());
            }
            opinions.insert((host.to_string(), parts.last().unwrap().to_string()), val);
        }
        (hosts, opinions)
    }
    
    pub fn solve () {
        let (mut hosts, mut opinions) = preprocess();
        
        let now = Instant::now();
        let res1 = part1(&hosts, &opinions);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::santa(13, 1), res1, elapsed);

        let res2 = part2(&mut hosts, &mut opinions);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(13, 2), res2, elapsed);
    }

    fn compute_happiness(hosts: &Vec<String>, opinions: &HashMap::<(String, String), i32>) -> i32 {
        let mut happinesses = Vec::<i32>::new();
        for perm in hosts.iter().permutations(hosts.len()) {
            let mut h = 0;
            for i in 0..perm.len() {
                let (pair1, pair2) = match i {
                    0 => ((perm[i].to_string(), perm.last().unwrap().to_string()), (perm[i].to_string(), perm[i+1].to_string())),
                    n if n == perm.len()-1 => ((perm[i].to_string(), perm[0].to_string()), (perm[i].to_string(), perm[i-1].to_string())),
                    _ => ((perm[i].to_string(), perm[i+1].to_string()), (perm[i].to_string(), perm[i-1].to_string())) 
                };
            
                h += opinions.get(&pair1).unwrap();
                h += opinions.get(&pair2).unwrap();
            }
            happinesses.push(h)
        }
    
        *happinesses.iter().max().unwrap()
    }
    
    fn part1(hosts: &Vec<String>, opinions: &HashMap::<(String, String), i32>) -> i32 {
        compute_happiness(hosts, opinions)
    }

    fn part2(hosts: &mut Vec<String>, opinions: &mut HashMap::<(String, String), i32>) -> i32 {
        for i in 0..hosts.len() {
            opinions.insert((String::from("Matteo"), (*hosts[i]).to_string()), 0);
            opinions.insert(((*hosts[i]).to_string(), String::from("Matteo")), 0);            
        }
        hosts.push(String::from("Matteo"));
        compute_happiness(hosts, opinions)
    }   
}
