pub mod day18 {
    extern crate aoc;
    use aoc::utils;
     
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

    pub fn part1(lines: &Vec<String>) {
        let vertices = preprocess1(&lines);
        let p = utils::perimeter(&vertices);
        let a = utils::shoelace(&vertices);
        let fill = a + 1 + p/2;
        println!("{} {}", utils::santa(18, 1), fill);
    }

    pub fn part2(lines: &Vec<String>) {
        let vertices = preprocess2(&lines);
        let p = utils::perimeter(&vertices);
        let a = utils::shoelace(&vertices);
        let fill = a + 1 + p/2;
        println!("{} {}", utils::christmas_tree(18, 2), fill);
    }
}
