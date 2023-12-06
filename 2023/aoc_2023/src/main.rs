use std::time::Instant;

extern crate aoc;
use aoc::utils;

mod day6;

fn main() {
    let now = Instant::now();
    let input = utils::read_input("../input_6.txt");
    day6::day6::part1(&input);
    day6::day6::part2(&input);

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed); 
}
