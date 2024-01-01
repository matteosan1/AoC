pub mod day14 {
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    fn preprocess() -> (Vec<String>, Vec::<[i32; 6]>) {
        let lines = utils::read_input("../instructions14a.txt");
        let mut names = Vec::<String>::new();
        let mut reindeers = Vec::<[i32; 6]>::new();
        for (i, l) in lines.iter().enumerate() {
            let parts = l[0..l.len()-1].split_whitespace().collect::<Vec<&str>>();
            let speed = parts[3].parse::<i32>().unwrap();
            let t1 = parts[6].parse::<i32>().unwrap();
            let rest = parts[13].parse::<i32>().unwrap();
            names.push(parts[0].to_string());
            reindeers.push([i as i32, speed, t1, rest, 0, 0]);
        }
        (names, reindeers)
    }

    pub fn solve () {
        let (names, mut reindeers) = preprocess();
        
        let now = Instant::now();
        let res1 = part1(&mut reindeers);
        let elapsed = now.elapsed();
        println!("{} {} {} ({:.2?})", utils::santa(14, 1), names[res1.0], res1.1, elapsed);
    
        let res2 = part2(&mut reindeers);
        let elapsed = now.elapsed();
        println!("{} {} {} ({:.2?})", utils::christmas_tree(14, 2), names[res2.0], res2.1, elapsed);
    }
    
    fn reset(reindeers: &mut Vec<[i32; 6]>) {
        for r in reindeers {
            r[4] = 0;
        }
    }

    fn assign_points(reindeers: &mut Vec<[i32; 6]>) {
        let mdist = reindeers.iter().map(|x| x[4]).max().unwrap();
        for r in reindeers {
            if r[4] == mdist {
                r[5] += 1;
            }
        }
    }

    fn part1(reindeers: &mut Vec::<[i32; 6]>) -> (usize, i32) {
        for t in 0..=2502 {
            for i in 0..reindeers.len() {
                let state = t % (reindeers[i][2]+reindeers[i][3]);
                if state < reindeers[i][2] {
                    reindeers[i][4] += reindeers[i][1];
                }
            }
        }
    
        reindeers.sort_by(|a, b| b[4].cmp(&a[4]));
        (reindeers[0][0] as usize, reindeers[0][4])
    }

    fn part2(reindeers: &mut Vec::<[i32; 6]>) -> (usize, i32) {
        reset(reindeers);

        for t in 0..=2502 {
            for i in 0..reindeers.len() {
                let state = t % (reindeers[i][2]+reindeers[i][3]);
                if state < reindeers[i][2] {
                    reindeers[i][4] += reindeers[i][1];
                }
            }
            
            reindeers.sort_by(|a, b| b[4].cmp(&a[4]));
            assign_points(reindeers);
        }
 
        reindeers.sort_by(|a, b| b[5].cmp(&a[5]));
        (reindeers[0][0] as usize, reindeers[0][5])
    }
}
