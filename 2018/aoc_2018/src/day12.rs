pub mod day12 {
    use std::time::Instant;
    use regex::Regex;
    use itertools::Itertools;

    extern crate num;
    use num::Integer;
    
    extern crate aoc;
    use aoc::utils;

    fn preprocess() -> Vec::<[i32; 6]> {
        let lines = utils::read_input("../input_12.txt");

        let pattern = r"\w=(-?\d+)";
        let regex = Regex::new(pattern).unwrap();
        
        let mut moons = Vec::<[i32; 6]>::new(); 
        for l in lines {
            let mut temp = [0i32; 6];
            let mut i = 0;
            for val in regex.captures_iter(&l).map(|c| {
                                                        let group = c.get(1);
                                                        match group {
                                                            Some(val) => val.as_str(),
                                                            _ => "",
                                                        }}) {
                temp[i] = val.parse::<i32>().unwrap();
                i += 1;
            }
            moons.push(temp);
        }
        moons
    }

    pub fn solve () {
        let moons = preprocess();
        let now = Instant::now();

        let res1 = part1(moons.clone());
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::santa(12, 1), res1, elapsed);
        
        let res2 = part2(moons);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(12, 2), res2, elapsed);
    }

    fn move_moons(moons: &mut Vec<[i32; 6]>) {
        let index: [usize; 4] = [0, 1, 2, 3];
        for c in index.iter().combinations(2) {
            for i in 0..3 {
                let mut dv = 0;
                if moons[*c[0]][i] > moons[*c[1]][i] {
                    dv = -1;
                } else if moons[*c[0]][i] < moons[*c[1]][i] {
                    dv = 1;
                }
                moons[*c[0]][i+3] += dv;
                moons[*c[1]][i+3] -= dv;
            }
        }

        for m in moons {
            for i in 0..3 {
                m[i] += m[i+3];
            }
        }
    }

    fn energy(moon: &[i32; 6]) -> i32 {
        let mut val1 = 0;
        let mut val2 = 0;
        for i in 0..3 {
            val1 += i32::abs(moon[i]);
            val2 += i32::abs(moon[i+3]);
        }
        val1*val2
    }         

    fn part1(mut moons: Vec<[i32; 6]>) -> i32 {
        for _ in 0..1000 {
            move_moons(&mut moons);
        }

        let mut tot_energy = 0;
        for m in moons {
            tot_energy += energy(&m);
        }

        tot_energy
    }

    fn part2(mut moons: Vec::<[i32; 6]>) -> i64 {
        let init = moons.clone();
        let mut period: [i64; 3] = [0, 0, 0];
        let mut cycles = 1;
        loop {
            move_moons(&mut moons);
            cycles += 1;
            for coord in 0..3 {
                if period[coord] == 0 {
                    if moons.iter().enumerate().all(|(i, m)| m[coord] == init[i][coord]) {
                        period[coord] = cycles;
                    }
                }
            }
            if period.iter().all(|&x| x != 0) {
                break;
            }
        }
        
        period[0].lcm(&period[1].lcm(&period[2]))
    }
}


    
