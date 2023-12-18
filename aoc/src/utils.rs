use std::fs;
use std::process;
use crate::search::Coord;

pub fn read_map(filename: &str) -> (Vec<Coord>, Coord, Coord) {
    let input = fs::read_to_string(filename).unwrap_or_else(|err| {
        println!("{} (map not found)", err);
        process::exit(1);
    });
    let mut dungeon = Vec::<Coord>::new();
    
    let mut start = Coord {..Default::default()};
    let mut end = Coord {..Default::default()};
    for (y, l) in input.lines().enumerate() {
        for (x, c) in l.chars().enumerate() {
            if c == ' ' {
                dungeon.push(Coord{x: x as i32, y: y as i32, dist: 1});
            } else if c >= '0' && c <= '9' {
                dungeon.push(Coord::new(x as i32, y as i32, c.to_digit(10).unwrap() as i32));
            } else if c == '@' {
                start.x = x as i32;
                start.y = y as i32;
                start.dist = 1;
                dungeon.push(start);
            } else if c == 'X' {
                end.x = x as i32;
                end.y = y as i32;
                end.dist = 1;
                dungeon.push(end);
            } 
        }
    }

    (dungeon, start, end)
}

pub fn read_input(filename: &str) -> Vec<String> {
    let lines = fs::read_to_string(filename) 
        .unwrap_or_else(|err| {
            println!("{}", err);
            process::exit(1);
        })
        .lines()
        .map(String::from)
        .collect();
    lines
}

pub fn print_map(arr: &Vec<Coord>, xlim: &(i32, i32), ylim: &(i32, i32)) {               
    for y in ylim.0..=ylim.1 {
        for x in xlim.0..=xlim.1 {
            match arr.iter().find(|coord| coord.x == x && coord.y == y) {
                Some(_x) => print!("."),
                None => print!("#"),
            }
        }
        println!("");
    }
}

pub fn print_path(arr: &Vec<Coord>, xlim: &(i32, i32), ylim: &(i32, i32), path: &Vec<Coord>) {

    for y in ylim.0..=ylim.1 {
        for x in xlim.0..=xlim.1 {
            let c = match arr.iter().find(|coord| coord.x == x && coord.y == y) {
                Some(_x) => ".",
                None => "#",
            };
            let c_true = match path.iter().find(|coord| coord.x == x && coord.y == y) {
                Some(_x) => "O",
                None => c,
            };
            print!("{}", c_true);
        }
        println!("");
    }
}

pub type Point = [i64; 2]; 

pub fn manhattan_dist(p1: &Point, p2: &Point) -> i64 {
    i64::abs(p1[0]-p2[0]) + i64::abs(p1[1]-p2[1])
}

pub fn perimeter(vertices: &Vec::<Point>) -> i64 {
    let mut perimeter = 0;
    for i in 0..vertices.len() {
        if i == vertices.len()-1 {
            perimeter += manhattan_dist(&vertices[i], &vertices[0]);
        } else {
            perimeter += manhattan_dist(&vertices[i], &vertices[i+1]);
        }
    }
    perimeter
}

pub fn shoelace(vertices: &Vec::<Point>) -> i64 {
    let mut area = 0;
    for i in 0..vertices.len() {
        if i == vertices.len()-1 {
            area += vertices[i][0]*vertices[0][1] - vertices[i][1]*vertices[0][0];
        } else {
            area += vertices[i][0]*vertices[i+1][1] - vertices[i][1]*vertices[i+1][0];
        }
    }
    i64::abs(area/2 as i64)
}

pub fn santa(day: i32, part: usize) -> String {
    let message = format!("Day {} - part {} {}:", day, part, std::char::from_u32(0x1F385).unwrap().to_string());
    message
}

pub fn christmas_tree(day: i32, part: usize) -> String {
    let message = format!("Day {} - part {} {}:", day, part, std::char::from_u32(0x1F384).unwrap().to_string());
    message
}
