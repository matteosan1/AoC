pub mod day6 {
    extern crate aoc;
    use aoc::utils;

    fn find_interval(time: &i64, dist: &i64) -> i64 {
        let x1 = ((*time as f64 + f64::sqrt(f64::powf(*time as f64, 2.0) - 4.0**dist as f64)) / 2.0) as i64;
        let x2 = ((*time as f64 - f64::sqrt(f64::powf(*time as f64, 2.0) - 4.0**dist as f64)) / 2.0) as i64;
        x1 - x2
    }
    
    fn mul(vec: &Vec<i64>) -> i64 {
        let mut tot: i64 = 1;
        for v in vec {
            tot *= *v;
        }
        tot
    }

    pub fn part1(input: &Vec<String>) {
        let times: Vec<_> = input[0][5..].split_whitespace().map(|x| x.parse::<i64>().unwrap()).collect();
        let distances: Vec<_> = input[1][9..].split_whitespace().map(|x| x.parse::<i64>().unwrap()).collect();
        let mut counts = Vec::<i64>::new();
        for it in 0..times.len() {
            counts.push(find_interval(&times[it], &distances[it]))
        }
        
        println!("{} {}", utils::santa(6, 1), mul(&counts));
    }

    pub fn part2(input: &Vec<String>) {
        let times = input[0][5..].split_whitespace().collect::<Vec<_>>().join("").parse::<i64>().unwrap();
        let distances = input[1][9..].split_whitespace().collect::<Vec<_>>().join("").parse::<i64>().unwrap();

        println!("{} {}", utils::christmas_tree(6, 2), find_interval(&times, &distances));
    }
}
