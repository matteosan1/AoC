use std::time::Instant;

extern crate aoc;
use aoc::utils;

mod day5;

fn main() {
    let now = Instant::now();
    let input = utils::read_input("../input_5.txt");
    day5::day5::part1(&input);
    day5::day5::part2(&input);

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed); 
}
