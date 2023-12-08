use std::time::Instant;

extern crate aoc;
use aoc::utils;

mod dayDAY;

fn main() {
    let lines = utils::read_input("../input_DAY.txt");

    let now = Instant::now();
    let input = dayDAY::dayDAY::preprocess1(&lines);
    dayDAY::dayDAY::part1(&input);
    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);

    let now2 = Instant::now();
    let input = dayDAY::dayDAY::preprocess2(&lines);
    dayDAY::dayDAY::part2(&input);
    let elapsed2 = now2.elapsed();
    println!("Elapsed: {:.2?}", elapsed2); 

}
