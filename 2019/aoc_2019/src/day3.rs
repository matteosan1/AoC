pub mod day3 {
    use std::collections::HashMap;
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;
    use aoc::search::Coord;

    pub fn solve() {
        let input = utils::read_input("../instructions3a.txt");
        
        let now = Instant::now();
        
        let res1 = part1(&input);
        let elapsed = now.elapsed();                
        println!("{} {} ({:.2?})", utils::santa(3, 1), res1, elapsed);
        
        let res2 = part2(&input);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(3, 2), res2, elapsed);        
    }
    
    
    pub fn part1(input: &Vec<String>) -> usize {
        let mut houses = HashMap::<Coord, i32>::new();
        let directions = &input[0];
        let mut pos = Coord::new(0, 0, 0);
        houses.insert(Coord::new(0, 0, 0), 1);
        
        for d in directions.chars() {
            if d == '^' {
                pos.y += 1;
            } else if d == 'v' {
                pos.y -= 1;
            } else if d == '<' {
                pos.x -= 1;
            } else {
                pos.x += 1;
            }
            
            match houses.get_mut(&pos) {
                Some(_x) => {
                    let x = houses.get_mut(&pos).unwrap();
                    *x += 1;
                },
                None => { houses.insert(pos, 1); },
            };
        }
        houses.len()
    }

    pub fn part2(input: &Vec<String>) -> usize {
        let mut houses = HashMap::<Coord, i32>::new();
        let directions = &input[0];
        let mut pos = Coord::new(0, 0, 0);
        let mut pos_robo = Coord::new(0, 0, 0);
        houses.insert(Coord::new(0, 0, 0), 2);
        
        for (i, d) in directions.chars().enumerate(){
            let var;
            if d == '^' {
                var = (0, 1);
            } else if d == 'v' {
                var = (0, -1);
            } else if d == '<' {
                var = (-1, 0);
            } else {
                var = (1, 0);
            }
            
            if i % 2 == 0 {
                pos.x += var.0;
                pos.y += var.1;
                match houses.get_mut(&pos) {
                    Some(_x) => {
                        let x = houses.get_mut(&pos).unwrap();
                        *x += 1;
                    },
                    None => { houses.insert(pos, 1); },
                };    
            } else {
                pos_robo.x += var.0;
                pos_robo.y += var.1;
                match houses.get_mut(&pos_robo) {
                    Some(_x) => {
                        let x = houses.get_mut(&pos_robo).unwrap();
                        *x += 1;
                    },
                    None => { houses.insert(pos_robo, 1); },
                };    
            }
        }
        houses.len()
    }
}
