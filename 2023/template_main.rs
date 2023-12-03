use std::time::Instant;

extern crate aoc;
use aoc::utils;

mod dayDAY;

fn main() {
    let now = Instant::now();
    let input = utils::read_input("../input_DAY.txt");
    dayDAY::dayDAY::part1(&input);
    dayDAY::dayDAY::part2(&input);

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed); 
}
