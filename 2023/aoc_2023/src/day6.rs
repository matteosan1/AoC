pub mod day6 {
    extern crate aoc;
    use aoc::utils;

    fn find_interval(time: &i32, dist: &i32) -> i32 {
        let x1 = time + i32::sqrt(i32::pow(time, 2) - 4*dist) / 2;
        let x2 = time - i32::sqrt(i32::pow(time, 2) - 4*dist) / 2;
        (x1 - x2) as u32
    }
    
    fn mul(vec: &Vec<i32>) -> i32 {
        let mut tot: i32 = 1;
        for v in vec {
            tot *= *v;
        }
        tot
    }
    
    pub fn part1(input: &Vec<String>) {
        let times = input[0][5:].split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect();
        let distances = input[1][9:].split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect();
        
        let mut counts = [i32; times.len()];
        for it in 0..times.len() {
            counts.push(find_interval(&times[it], &distances[it]))
        }
        
        println!("{} {}", utils::santa(6, 1), mul(counts));
    }


    pub fn part2(input: &Vec<String>) {
        let times = input[0][5:].split_whitespace().collect().join("");
        let distances = input[1][9:].split_whitespace().collect().join("");

        println!("{} {}", utils::christmas_tree(6, 2), find_interval(times, distances));
    }
}
