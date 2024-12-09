pub mod day24 {
    use itertools::Itertools;
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    fn preprocess() -> Vec<i64> {
        let lines = utils::read_input("../instructions24a.txt");
        lines.iter().map(|x| x.parse::<i64>().unwrap()).collect()
    }
    
    pub fn solve () {
        let pkgs = preprocess();
        
        let now = Instant::now();
        let res1 = part1(&pkgs);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::santa(24, 1), res1, elapsed);

        let res2 = part2(&pkgs);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(24, 2), res2, elapsed);
    }

    fn vec_mul(v: &Vec<&i64>) -> i64 {
        let mut val: i64 = 1;
        for item in v {
            val *= *item;
        }
        val
    }

    fn vec_sum(v: &Vec<&i64>) -> i64 {
        let mut val: i64 = 0;
        for item in v {
            val += *item;
        }
        val
    }

    fn skim(lst: &mut Vec<i64>, z: &Vec<&i64>) {
        for item in z {
            lst.retain(|x| *x != **item);
        }
    }
    
    fn get_groups(lst: &Vec<i64>, parts: i64, tot: i64, ng: i64, g1: &mut [i64; 3]) -> i64 {
        let mut y = 1;
        if *g1 != [0, 0, 0] {
            y = (g1[0]+1) as usize;
        }
        
        while y <= lst.len() {
            for z in lst.into_iter().combinations(y) {
                if vec_sum(&z) == tot {
                    if ng == parts {
                        let entanglement = vec_mul(&z);
                        if *g1 != [0, 0, 0] {
                            if entanglement < g1[1] {
                                *g1 = [z.len() as i64, entanglement, 0];
                            } else {
                                continue;
                            }
                        } else {
                            *g1 = [z.len() as i64, entanglement, 0];
                        }
                    } else if ng == 1 {
                        g1[2] = 1;
                    }
                    let mut new_lst: Vec<i64> = lst.clone();
                    skim(&mut new_lst, &z);
                    get_groups(&mut new_lst, parts, tot, ng - 1, g1);
                }
            }
            if g1[2] == 1 {
                break;
            }
            y += 1;
        }
        g1[1]
    }    

    fn run(inputs: &Vec<i64>, parts: i64) -> i64 {
        let tot = inputs.iter().sum::<i64>()/parts;
        let mut g1 = [0 as i64, 0 as i64, 0 as i64];
        get_groups(inputs, parts, tot, parts, &mut g1)
    }
    
    fn part1(inputs: &Vec<i64>) -> i64 {
        run(inputs, 3)
    }

    fn part2(inputs: &Vec<i64>) -> i64 {
        run(inputs, 4)
    }
}
