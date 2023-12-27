pub mod day10 {
    use std::collections::HashMap;
    
    extern crate aoc;
    use aoc::utils;
    
    fn preprocess (lines: &Vec<String>) -> ([i8; 2], HashMap::<[i8; 2], char>) {
        let mut pipes = HashMap::<[i8; 2], char>::new();
        let mut start;
        for (y, l) in lines.iter().enumerate() {
            for (x, c) in l.chars().enumerate() {
                pipes.insert([x as i8, y as i8], c);
                if c == 'S' {
                    start = [x as i8, y as i8];
                }
            }
        }
        (start, pipes)
    }
        
    pub fn part1(lines: &Vec<String>) {
        let mapping: HashMap::<char, [i8; 4]> = HashMap::<char, [i8; 4]>::from(
            [('J', [-1, 0, 3, -1]),
             ('|', [0, -1, 2, -1]),
             ('-', [-1, 1, -1, 3]),
             ('F', [1, -1, -1, 2]),
             ('7', [3, 2, -1, -1]),
             ('L', [-1, -1, 1, 0])]);

        let dirs = Vec::<[i8; 2]>::from([[0,-1], [1,0], [0,1], [-1,0]]);
        let (start, pipes) = preprocess(lines);
        let mut farthest = 0;
        let mut farthest_path;
        for (s, possible_moves) in mapping {
            pipes[&start] = s;
            for m in possible_moves.iter() {
                let mut path = Vec::<[i8; 2]>::new();
                if *m == -1 {
                    continue;
                }
                let dir = m;
                let mut pos = start;
                let mut steps = 0.;
                let mut loo = true;
                loop {
                    path.push(pos);
                    let new_pos = [pos[0] + dirs[*dir as usize][0], pos[1] + dirs[*dir as usize][1]];
                    //if new_pos not in sketch:
                    //loop = False
                    //break
                    let new_dir = mapping[&pipes[&new_pos]][*dir as usize];
                    if new_dir == -1 {
                        loo = false;
                        break;
                    }
                    if new_pos == start {
                        break;
                    }
                    steps += 1.;
                    pos = new_pos;
                    dir = &new_dir;
                }
                if loo {
                    let f = f64::ceil(steps/2.);
                    if farthest < (f as i64) {
                        farthest = f as i64;
                        let starting_point = pipes[&start];
                        farthest_path = path;
                    }
                }
            }
        }
        println!("{} {}", utils::santa(10, 1), farthest);
    }


    pub fn part2(_lines: &Vec<String>) {
        
        println!("{} {}", utils::christmas_tree(10, 2), 0);
    }
}
