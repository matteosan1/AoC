use std::time::Instant;

extern crate aoc;
use aoc::utils;

mod day16;

fn main() {
    let lines = utils::read_input("../input_16.txt");

    let now = Instant::now();
    day16::day16::part1(&lines);
    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);

    let now2 = Instant::now();
    day16::day16::part2(&lines);
    let elapsed2 = now2.elapsed();
    println!("Elapsed: {:.2?}", elapsed2); 

}
