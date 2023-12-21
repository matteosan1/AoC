use std::fs;
use std::process;
use crate::search::Coord;

type Point<T> = [T; 2];
    
fn manhattan_dist<T>(p1: Point<T>, p2: Point<T>) -> T 
where T: num::Signed + Copy + std::ops::Sub + std::ops::Add + std::ops::Mul,
{
    T::abs(&(p1[0]-p2[0])) + T::abs(&(p1[1]-p2[1]))
}

pub fn perimeter<T>(vertices: &Vec::<Point<T>>) -> T 
where T: num::Signed + Copy + std::ops::Sub + std::ops::AddAssign + std::ops::Mul,
{
    let mut perimeter: T = T::zero();
    for i in 0..vertices.len() {
        if i == vertices.len()-1 {
            perimeter += manhattan_dist::<T>(vertices[i], vertices[0]);
        } else {
            perimeter += manhattan_dist::<T>(vertices[i], vertices[i+1]);
        }
    }
    perimeter
}

pub fn shoelace<T>(vertices: &Vec::<Point<T>>) -> T 
where T: num::Signed + Copy + std::ops::Sub + std::ops::AddAssign + std::ops::Mul + std::convert::From<i64>,
{
    let mut area = T::zero();
    for i in 0..vertices.len() {
        if i == vertices.len()-1 {
            area += vertices[i][0]*vertices[0][1] - vertices[i][1]*vertices[0][0];
        } else {
            area += vertices[i][0]*vertices[i+1][1] - vertices[i][1]*vertices[i+1][0];
        }
    }
    T::abs(&(area/<T as From<i64>>::from(2)))
}

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

pub fn santa(day: i32, part: usize) -> String {
    let message = format!("Day {} - part {} {}:", day, part, std::char::from_u32(0x1F385).unwrap().to_string());
    message
}

pub fn christmas_tree(day: i32, part: usize) -> String {
    let message = format!("Day {} - part {} {}:", day, part, std::char::from_u32(0x1F384).unwrap().to_string());
    message
}
