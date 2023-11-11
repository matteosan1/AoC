pub fn part1() -> String {
    let input = std::fs::read_to_string("input_2.txt").unwrap();
    
    input
        .lines()
        .map(|line| {
            let bytes = line.as_bytes();
            let left = (bytes[0] - b'A') as i8;
            let right = (bytes[2] - b'X') as i8;
            let outcome = (right - left + 1).rem_euclid(3);

            let shape_score = right + 1;
            let outcome_score = 3 * outcome;
            (shape_score + outcome_score) as u32
        })
        .sum::<u32>()
        .to_string()
}

pub fn part2() -> String {
    let input = std::fs::read_to_string("input_2.txt").unwrap();

    input
        .lines()
        .map(|line| {
            let bytes = line.as_bytes();
            let left = (bytes[0] - b'A') as i8;
            let right = (bytes[2] - b'X') as i8;

            let my_shape = (left - 1 + right).rem_euclid(3);

            let shape_score = my_shape + 1;
            let outcome_score = 3 * right;
            (shape_score + outcome_score) as u32
        })
        .sum::<u32>()
        .to_string()
}
fn main() {
    println!("{}", part1());
    println!("{}", part2());
}
