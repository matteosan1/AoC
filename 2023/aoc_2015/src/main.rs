use std::time::Instant;

extern crate aoc;
use aoc::utils;

mod day13;

fn main() {
    let now = Instant::now();
    let input = utils::read_input("input_13.txt");
    day13::day13::part1(&input);
    day13::day13::part2(&input);

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed); 
}
