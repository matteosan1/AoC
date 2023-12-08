// Cannot be so much slower than python

pub mod day8 {
    extern crate aoc;
    use aoc::utils;

    #[derive(Debug)]
    struct Node {
        id: String,
        left: String,
        right: String,
    }

    fn preprocess(input: &Vec<String>) -> (Vec<i64>, Vec<Node>) {
        let dirs: Vec<_> = input[0].chars().map(|c| match c {
            'L' => 0,
            'R' => 1,
            _ => -1,
        }).collect();

        let mut nodes = Vec::<Node>::with_capacity(1000);
        for i in 1..input.len() {
            if input[i] == "" { continue; }
            let parts = input[i].split_once(" = ").unwrap();
            let (left, right) = parts.1[1..parts.1.len()-1].split_once(", ").unwrap();
            nodes.push(Node{ id: parts.0.to_string(), left: left.to_string(), right: right.to_string() });
        }

        (dirs, nodes)
    }
    
    pub fn part1(input: &Vec<String>) {
        let (dirs, nodes) = preprocess(input);

        let mut steps = 0;
        let mut pos = "AAA";
        while pos != "ZZZ" {
            let dir = dirs[steps%(dirs.len())];
            let new_pos = nodes.iter().find(|x| x.id == pos).unwrap();
            pos = match dir {
                1 => &new_pos.right,
                0 => &new_pos.left,
                _ => "MATTEO"
            };

            steps += 1;
        }
        
        println!("{} {}", utils::santa(8, 1), steps);
    }

    fn find_lcm(arr: &[i64]) -> i64 {
        if arr.is_empty() {
            return 0;
        }

        let mut result = arr[0];
        for i in 1..arr.len() {
            let current_lcm = result * arr[i] / gcd(result, arr[i]);
            result = current_lcm;
        }
        
        result
    }
    
    fn gcd(a: i64, b: i64) -> i64 {
        if b == 0 {
            a
        } else {
            gcd(b, a % b)
        }
    }
    
    pub fn part2(input: &Vec<String>) {
        let (dirs, nodes) = preprocess(input);
        let mut pos = Vec::<String>::new();
        let mut steps = Vec::<i64>::new();
        
        for i in 0..nodes.len() { 
            if nodes[i].id.ends_with("A") {
                pos.push(nodes[i].id.clone());
                steps.push(0);
            }
        }
        for p in 0..pos.len() {
            loop {
                let dir = dirs[(steps[p]%(dirs.len() as i64)) as usize];
                let new_pos = nodes.iter().find(|x| x.id == pos[p]).unwrap();
                pos[p] = match dir {
                    1 => new_pos.right.clone(),
                    0 => new_pos.left.clone(),
                    _ => "MATTEO".to_string()
                };
                steps[p] += 1;

                if pos[p].ends_with("Z") {
                    break;
                }
            }
        }

        println!("{} {}", utils::christmas_tree(8, 2), find_lcm(&steps));
    }
}


