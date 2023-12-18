pub mod day18 {
    extern crate aoc;
    use aoc::utils;
     
    type Point = [i64; 2];
     
    fn preprocess1(lines: &Vec<String>) -> Vec::<Point> {
        let mut p = [0, 0];
        lines.iter().map(|line| {
            let parts: Vec<_> = line.split_whitespace().collect();
            let size = parts[1].parse::<i64>().unwrap();
            p = match parts[0] {
                "R" => [p[0]+size, p[1]], 
                "D" => [p[0], p[1]+size], 
                "L" => [p[0]-size, p[1]], 
                "U" => [p[0], p[1]-size],
                 _ => panic!()
            };
            p
        }).collect()
    }

    fn preprocess2(lines: &Vec<String>) -> Vec::<Point> {
        let mut p = [0, 0];
        lines.iter().map(|line| {
            let part = line.split_whitespace().last().unwrap();//.collect();
            let size = i64::from_str_radix(&part[2..part.len()-2], 16).unwrap();
            let code = part.chars().rev().nth(1).unwrap();
            p = match code {
                '0' => [p[0]+size, p[1]], 
                '1' => [p[0], p[1]+size], 
                '2' => [p[0]-size, p[1]], 
                '3' => [p[0], p[1]-size],
                 _ => panic!()
            };
            p
        }).collect()
    }

    fn manhattan_dist(p1: &Point, p2: &Point) -> i64 {
        i64::abs(p1[0]-p2[0]) + i64::abs(p1[1]-p2[1])
    }

    fn perimeter(vertices: &Vec::<Point>) -> i64 {
        let mut P = 0;
        for i in 0..vertices.len() {
            if i == vertices.len()-1 {
                P += manhattan_dist(&vertices[i], &vertices[0]);
            } else {
                P += manhattan_dist(&vertices[i], &vertices[i+1]);
            }
        }
        P
    }

    fn shoelace(vertices: &Vec::<Point>) -> i64 {
        let mut A = 0;
        for i in 0..vertices.len() {
            if i == vertices.len()-1 {
                A += vertices[i][0]*vertices[0][1] - vertices[i][1]*vertices[0][0];
            } else {
                A += vertices[i][0]*vertices[i+1][1] - vertices[i][1]*vertices[i+1][0];
            }
        }
        i64::abs(A/2 as i64)
    }

    pub fn part1(lines: &Vec<String>) {
        let vertices = preprocess1(&lines);
        let p = perimeter(&vertices);
        let A = shoelace(&vertices);
        let fill = A + 1 + p/2;
        println!("{} {}", utils::santa(18, 1), fill);
    }

    pub fn part2(lines: &Vec<String>) {
        let vertices = preprocess2(&lines);
        let p = perimeter(&vertices);
        let A = shoelace(&vertices);
        let fill = A + 1 + p/2;
        println!("{} {}", utils::christmas_tree(18, 2), fill);
    }
}
