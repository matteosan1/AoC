// Semplificare le funzioni per trovare le parts

pub mod day3 {
    extern crate aoc;
    use aoc::utils;

    fn find_part(lines: &Vec<String>, x: usize, y: usize) -> Vec<i64> {
        let mut parts = Vec::<i64>::new();
        if lines[y].chars().nth(x-1).unwrap().is_digit(10) {
            let mut idx = x;
            while idx > 0 { 
                idx -= 1;
                if !lines[y].chars().nth(idx).unwrap().is_digit(10) {
                    idx += 1;
                    break;
                }                
            }
            let mut part = lines[y][idx..x].parse::<i64>().unwrap();
            if !parts.contains(&part) {
                parts.push(part);
            }
        }

        if lines[y].chars().nth(x+1).unwrap().is_digit(10) {
            let mut idx = x+1;
            while idx <= lines[y].len()-1 && lines[y].chars().nth(idx).unwrap().is_digit(10) {
                idx += 1;
            }
            let part = lines[y][x+1..idx].parse::<i64>().unwrap();
            if !parts.contains(&part) {
                parts.push(part);
            }
        }

        let steps: [usize; 3] = [0, 1, 2];
        for i in steps {
            let idx = (x + i - 1);
            if y > 0 && lines[y-1].chars().nth(idx).unwrap().is_digit(10) {
                let mut llim = idx;
                let mut rlim = idx;
                let mut changed = false;
                loop {
                    changed = false;
                    if llim > 0 && lines[y-1].chars().nth(llim-1).unwrap().is_digit(10) {
                        llim -= 1;
                        changed = true;
                    }
                    
                    if  rlim < lines[y-1].len()-1 && lines[y-1].chars().nth(rlim+1).unwrap().is_digit(10) {
                        rlim += 1;
                        changed = true;
                    }
                    
                    if !changed {
                        break;
                    }
                }
                let part = lines[y-1][llim..rlim+1].parse::<i64>().unwrap();
                if !parts.contains(&part) {
                    parts.push(part);
                }
            }

            let idx = (x + i - 1);
            if y < lines.len()-1 && lines[y+1].chars().nth(idx).unwrap().is_digit(10) {
                let mut llim = idx;
                let mut rlim = idx;
                let mut changed = false;
                loop {
                    changed = false;
                    if llim > 0 && lines[y+1].chars().nth(llim-1).unwrap().is_digit(10) {
                        llim -= 1;
                        changed = true;
                    }
                    
                    if  rlim < lines[y+1].len()-1 && lines[y+1].chars().nth(rlim+1).unwrap().is_digit(10) {
                        rlim += 1;
                        changed = true;
                    }
                    
                    if !changed {
                        break;
                    }
                }
                let part = lines[y+1][llim..rlim+1].parse::<i64>().unwrap();
                if !parts.contains(&part) {
                    parts.push(part);
                }
            }
        }
        parts
    }
    
    pub fn part1(lines: &Vec<String>) {
        let mut parts = Vec::<i64>::new();
        for (y, l) in lines.iter().enumerate() {
            for (x, c) in l.chars().enumerate() {
                if !c.is_digit(10) && c != '.' {
                    parts.append(&mut find_part(lines, x, y));
                }
            }
            
        }
        println!("{} {}", utils::santa(3, 1), parts.iter().sum::<i64>());
    }


    pub fn part2(lines: &Vec<String>) {
        let mut parts = Vec::<i64>::new();
        for (y, l) in lines.iter().enumerate() {
            for (x, c) in l.chars().enumerate() {
                if c == '*' {
                    let temp = find_part(lines, x, y);
                    if temp.len() == 2 {
                        parts.push(temp[0]*temp[1]);
                    }
                }
            }
            
        }
        println!("{} {}", utils::christmas_tree(3, 2), parts.iter().sum::<i64>());
    }
}
