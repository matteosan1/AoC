pub mod day6 {
    use std::collections::{HashMap, BinaryHeap};
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    pub fn solve() {
        let lines = utils::read_input("../input_6.txt");
        let mut orbits = HashMap::<String, Vec<String>>::new();
        for l in lines.iter() {
            let parts = l.split_once(")").unwrap();
            if orbits.contains_key(parts.0) {
                orbits.get_mut(parts.0).unwrap().push(parts.1.to_string());
            } else {
                let temp = vec![parts.1.to_string()];
                orbits.insert(parts.0.to_string(), temp);
            }
            if orbits.contains_key(parts.1) {
                orbits.get_mut(parts.1).unwrap().push(parts.0.to_string());
            } else {
                let temp = vec![parts.0.to_string()];
                orbits.insert(parts.1.to_string(), temp);
            }
        }
        
        let now = Instant::now();
        
        let res1 = part1(&orbits);
        let elapsed = now.elapsed();                
        println!("{} {} ({:.2?})", utils::santa(6, 1), res1, elapsed);
        
        let res2 = part2(&orbits);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(6, 2), res2, elapsed);        
    }

    fn find_paths(orbits: &HashMap::<String, Vec<String>>) -> usize {
        let mut paths = Vec::<Vec::<String>>::new();
        let mut temp = Vec::<String>::new();
        temp.push("COM".to_string());
        let mut queue = Vec::<Vec::<String>>::new();
        queue.push(temp);
        while queue.len() != 0 {
            let path = queue.pop().unwrap();
            let pos = path.last().unwrap();
            let dests = orbits.get(pos).unwrap();
            let mut grow = false;
            for d in dests {
                if path.contains(d) {
                    continue;
                }
                grow = true;
                let mut new_path = path.clone();
                new_path.push(d.clone());
                queue.push(new_path);
            }
            if !grow {
                paths.push(path);
            }
        }

        let mut tot_orbits = 0usize;
        for k in orbits.keys() {
            if k == "COM" {
                continue;
            }
            for path in &paths {
                let mut found = false;
                for (i, p) in path.iter().enumerate() {
                    if p == k {
                        tot_orbits += i;
                        found = true;
                    }
                }
                if found {
                    break;
                }
            }
        }
        tot_orbits
    }
    
    fn part1(orbits: &HashMap::<String, Vec<String>>) -> usize {
        find_paths(orbits)
    }

    fn transfers(orbits: &HashMap::<String, Vec<String>>) -> i32 {
        let start = String::from("YOU");
        let target = String::from("SAN");
        let mut visited = Vec::<String>::new();

        let mut heap = BinaryHeap::<(i32, String)>::new();
        heap.push((0, start));
        while heap.len() > 0 {
            let (steps, pos) = heap.pop().unwrap();
            visited.push(pos.clone());
            if pos == target {
                return -steps-2;
            }
            for new_pos in orbits.get(&pos).unwrap() {
                if !visited.contains(new_pos) {
                    heap.push((steps-1, new_pos.clone()));
                }
            }
        }
        0
    }

    fn part2(orbits: &HashMap::<String, Vec<String>>) -> i32 {
        transfers(orbits)
    }
}
