// suggestion just look for the first and last match only

pub mod day1 {
    use std::collections::HashMap;
    
    extern crate aoc;
    use aoc::utils;

    pub fn part1(input: &Vec<String>) {
        let mut codes = Vec::<u16>::with_capacity(1000);
        for line in input {
            let l = line.as_bytes();
            let mut i = 0;
            let mut digits = Vec::<u8>::new();
            while i < l.len() {
                if l[i] >= b'0' && l[i] <= b'9' {
                    digits.push(l[i]-b'0');
                }
                i += 1;
            }
            if digits.len() == 0 {
                continue;
            } else if digits.len() == 1 {
                codes.push((digits[0]*10+digits[0]) as u16);
            } else {
                codes.push((digits[0]*10+digits.last().unwrap()).into());
            }
        }
        println!("{} {}", utils::santa(1, 1), codes.iter().sum::<u16>());
    }

    pub fn part2(input: &Vec<String>) {
        let mut codes = Vec::<u16>::with_capacity(1000);
        
        for line in input {
            let new_line = line.replace("five", "f5e")
                .replace("one", "o1e")
                .replace("two", "t2o")
                .replace("three", "t3e")
                .replace("four", "f4r")
                .replace("five", "f5e")
                .replace("six", "s6x")
                .replace("seven", "s7n")
                .replace("eight", "e8t")
                .replace("nine", "n9e");
            
            let l = new_line.as_bytes();
            let mut i = 0;
            let mut digits = Vec::<u8>::new();
            while i < l.len() {
                if l[i] >= b'0' && l[i] <= b'9' {
                    digits.push(l[i]-b'0');
                }
                i += 1;
            }
            if digits.len() == 0 {
                continue;
            } else if digits.len() == 1 {
                codes.push((digits[0]*10+digits[0]) as u16);
            } else {
                codes.push((digits[0]*10+digits.last().unwrap()).into());
            }
        }
        println!("{} {}", utils::christmas_tree(1, 2), codes.iter().sum::<u16>());
    }
}
