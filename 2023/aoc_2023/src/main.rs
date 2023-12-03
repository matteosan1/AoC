use std::time::Instant;

extern crate aoc;
use aoc::utils;

mod day4;

fn main() {
    let now = Instant::now();
    let input = utils::read_input("../input_4.txt");
    day4::day4::part1(&input);
    day4::day4::part2(&input);

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed); 
}
