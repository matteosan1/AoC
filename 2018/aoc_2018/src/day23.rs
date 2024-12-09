pub mod day23 {
    use std::collections::HashMap;
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    pub fn solve () {
        let lines = utils::read_input("../input_23.txt");
        
        let now = Instant::now();
        let res1 = part1(&lines);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::santa(23, 1), res1, elapsed);

        let res2 = part2(&lines);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(23, 2),res2, elapsed);
    }

    fn compiler(line: &str, counter: &mut isize, register: &mut HashMap<char, i32>) {
        if line.starts_with("hlf") {
            let key = line.chars().last().unwrap();
            *register.entry(key).or_insert(0) /= 2;
            *counter += 1;
            //println!("{}", line.to_string());
        } else if line.starts_with("tpl") {
            let key = line.chars().last().unwrap();
            *register.entry(key).or_insert(0) *= 3;
            *counter += 1;
            //println!("{}", line.to_string());
        } else if line.starts_with("inc") {
            let key = line.chars().last().unwrap();
            *register.entry(key).or_insert(0) += 1;
            *counter += 1;
            //println!("{}", line.to_string());
        } else if line.starts_with("jmp") {
            let (_, val) = line.split_once(" ").unwrap();
            *counter += val.parse::<isize>().unwrap();
            //println!("{}", line.to_string());
        } else if line.starts_with("jie") {            
            let parts: Vec<_> = line.split_whitespace().collect();
            let val = *register.entry(parts[1].chars().nth(0).unwrap()).or_insert(0) % 2;
            if val == 0 {
                *counter += parts[2].parse::<isize>().unwrap();
                //println!("{}", line.to_string());
            } else {
                *counter += 1;
            }
        } else if line.starts_with("jio") {
            let parts: Vec<_> = line.split_whitespace().collect();
            let val = *register.entry(parts[1].chars().nth(0).unwrap()).or_insert(0);
            if val == 1 {
                *counter += parts[2].parse::<isize>().unwrap();
                //println!("{}", line.to_string());
            } else {
                *counter += 1;
            }
        } else {
            panic!("Wrong command {}", line);
        }
    }
    
    fn part1(input: &Vec<String>) -> i32 {
        let mut counter: isize = 0;
        let mut register = HashMap::<char, i32>::from([('a', 0), ('b', 0)]);

        while (counter as usize) < input.len() {
            compiler(&input[counter as usize], &mut counter, &mut register);
        }
        *register.get(&'b').unwrap()
    }

    fn part2(input: &Vec<String>) -> i32 {
        let mut counter: isize = 0;
        let mut register = HashMap::<char, i32>::from([('a', 1), ('b', 0)]);
        
        while (counter as usize) < input.len() {
            compiler(&input[counter as usize], &mut counter, &mut register);
        }
        *register.get(&'b').unwrap()
    }
}
