use std::time::Instant;

extern crate aoc;
use aoc::utils;

mod day22;

fn main() {
    let lines = utils::read_input("../input_22.txt");

    let now = Instant::now();
    day22::day22::part1(&lines);
    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);

    let now2 = Instant::now();
    day22::day22::part2(&lines);
    let elapsed2 = now2.elapsed();
    println!("Elapsed: {:.2?}", elapsed2); 

}
