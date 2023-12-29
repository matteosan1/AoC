use std::collections::HashMap;
use itertools::Itertools;

fn main() {
    let lines = vec!["Alice would gain 54 happiness units by sitting next to Bob.",
"Alice would lose 79 happiness units by sitting next to Carol.",
"Alice would lose 2 happiness units by sitting next to David.",
"Bob would gain 83 happiness units by sitting next to Alice.",
"Bob would lose 7 happiness units by sitting next to Carol.",
"Bob would lose 63 happiness units by sitting next to David.",
"Carol would lose 62 happiness units by sitting next to Alice.",
"Carol would gain 60 happiness units by sitting next to Bob.",
"Carol would gain 55 happiness units by sitting next to David.",
"David would gain 46 happiness units by sitting next to Alice.",
"David would lose 7 happiness units by sitting next to Bob.",
"David would gain 41 happiness units by sitting next to Carol."];

    let mut hosts = Vec::<&str>::new();
    let mut opinions = HashMap::<(String, String), i32>::new();
    for l in lines {
        let parts = l[0..l.len()-1].split_whitespace().collect::<Vec<&str>>();
        let mut val = parts[3].parse::<i32>().unwrap();
        if l.contains("lose") {
            val *= -1;
        }
        let host = parts[0];
        if !hosts.contains(&host) {
            hosts.push(host);
        }
        opinions.insert((host.to_string(), parts.last().unwrap().to_string()), val);
    }
        
    let mut happinesses = Vec::<i32>::new();
    for perm in hosts.iter().permutations(hosts.len()) {
        let mut h = 0;
        println!("{:?}", perm);
        for i in 0..perm.len() {
            let (pair1, pair2) = match i {
                0 => ((*perm[i], **perm.last().unwrap()), (*perm[i], *perm[i+1])),
                n if n == perm.len()-1 => ((*perm[i], *perm[0]), (*perm[i], *perm[i-1])),
                _ => ((*perm[i], *perm[i+1]), (*perm[i], *perm[i-1])) 
            };
            
            h += opinions.get(&(pair1.0.to_string(), pair1.1.to_string())).unwrap();
            h += opinions.get(&(pair2.0.to_string(), pair2.1.to_string())).unwrap();
        }
        happinesses.push(h)
    }
    
    println!("{:?}", happinesses);
}