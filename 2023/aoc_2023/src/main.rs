use std::time::Instant;

extern crate aoc;
use aoc::utils;

mod day21;

fn main() {
    let lines = utils::read_input("../input_21.txt");

    let now = Instant::now();
    day21::day21::part1(&lines);
    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);

    let now2 = Instant::now();
    day21::day21::part2(&lines);
    let elapsed2 = now2.elapsed();
    println!("Elapsed: {:.2?}", elapsed2); 

}
