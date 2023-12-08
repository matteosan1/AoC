use std::time::Instant;

extern crate aoc;
use aoc::utils;

mod day9;

fn main() {
    let lines = utils::read_input("../input_9.txt");

    let now = Instant::now();
    let input = day9::day9::preprocess1(&lines);
    day9::day9::part1(&lines);
    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);

    let now2 = Instant::now();
    let input = day9::day9::preprocess2(&lines);
    day9::day9::part2(&lines);
    let elapsed2 = now2.elapsed();
    println!("Elapsed: {:.2?}", elapsed2); 

}
