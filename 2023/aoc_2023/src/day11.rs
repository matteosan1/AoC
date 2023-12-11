// COMPILA MA NON TORNANO LE DISTANZE

pub mod day11 {
    use std::time::Instant;
    use itertools::Itertools;
    
    extern crate aoc;
    use aoc::utils;
    use aoc::search::Coord;
    
    fn preprocess(lines: &Vec<String>) -> (Vec::<Coord>, Vec::<i32>, Vec::<i32>) {
        let mut new_lines = Vec::<Vec::<char>>::new();
        for l in lines {
            new_lines.push(l.chars().collect());
        }
        
        let mut grow = Vec::<i32>::new();
        let mut gcol = Vec::<i32>::new();
        
        for y in 0..new_lines[0].len() {
            if new_lines[y].iter().all(|c| *c == '.') {
                grow.push(y as i32)
            }
        }

        for x in 0..new_lines[0].len() {
            let mut empty = false;
            for y in 0..new_lines.len() {
                if new_lines[y][x] != '.' {
                    empty = true;
                    break;
                }
            }
            if !empty {
                gcol.push(x as i32);
            }
        }

        let mut galaxies = Vec::<Coord>::new();
        for x in 0..new_lines[0].len() {
            for y in 0..new_lines.len() {
                if new_lines[y][x] == '#' {
                    galaxies.push(Coord { x: x as i32, y: y as i32, dist:-1 });
                }
            }
        }

        (galaxies, grow, gcol)
    }

    fn count_rowcol(perm: &Vec<&Coord>, grow: &Vec::<i32>, gcol: &Vec::<i32>) -> i64 {
        let mut n: i64 = 0;
        
        for x in grow {
            if (perm[1].x > perm[0].x && perm[0].x < *x && *x < perm[1].x) ||
                (perm[0].x > perm[1].x && perm[1].x < *x && *x < perm[0].x) {
                n += 1
            }
        }

        for y in grow {
            if (perm[1].y > perm[0].y && perm[0].y < *y && *y < perm[1].y) ||
                (perm[0].y > perm[1].y && perm[1].y < *y && *y < perm[0].y) {
                n += 1
            }
        }
        
        n
    }

    fn manhattan_distance(perm: &Vec<&Coord>) -> i64 {
        println!("{}", perm[0].x - perm[1].x);
        println!("{}", perm[0].y - perm[1].y);
        
        let d: i64 = (i32::abs(perm[0].x - perm[1].x) + i32::abs(perm[0].y - perm[1].y)).into();
        d
    }
    
    fn distances(galaxies: &Vec::<Coord>, grow: &Vec::<i32>, gcol: &Vec::<i32>, expansion_factor: &i64) -> i64 {
        let mut lengths: i64 = 0;
        for perm in galaxies.iter().combinations(2).unique() {
            let n = count_rowcol(&perm, &grow, &gcol);
            let d = manhattan_distance(&perm) + n*(*expansion_factor-1);
            println!("{:?} {}", perm, d);
            lengths += d;
        }
        lengths
    }

    
    fn part1(lines: &Vec<String>) {
    }

    fn part2(lines: &Vec<String>) {
    }
    
    pub fn run() {
        let lines = utils::read_input("../prova.txt");
        let (galaxies, grow, gcol) = preprocess(&lines);

        let now = Instant::now();
        let l1 = distances(&galaxies, &grow, &gcol, &mut 2);
        println!("{}", l1);
        let t1 = now.elapsed();
        
        //let now2 = Instant::now();
        //let l2 = distances(&galaxies, &grow, &gcol, &mut 1000000);
        //let t2 = now2.elapsed();
        //
        //println!("{} {} ({:.2?}) - {} {} ({:.2?})", utils::santa(11, 1), l1, t1,
        //         utils::christmas_tree(11, 2), l2, t2);
    }
}
