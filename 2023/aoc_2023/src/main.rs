use std::time::Instant;

extern crate aoc;
use aoc::utils;

mod day7;

fn main() {
    let now = Instant::now();
    let input = utils::read_input("../input_7.txt");
    day7::day7::part1(&input);
    day7::day7::part2(&input);

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed); 
}
