pub mod day9 {
    extern crate aoc;
    use aoc::utils;

    fn preprocess(lines: &Vec<String>) -> Vec::<Vec::<i32>> {
        let inputs: Vec<_> = lines.iter().map(|line| {
            line.split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<_>>()
        }).collect();
        inputs
    }
    
    fn subtraction(input: &Vec<i32>) -> Vec<i32> {
        let mut new_input = Vec::<i32>::new();
        for i in 0..input.len()-1 {
            new_input.push(input[i+1]-input[i]);
        }
        new_input
    }
    
    pub fn part1(lines: &Vec<String>) {
        let mut inputs = preprocess(lines);
        let mut predictions = Vec::<i32>::new();
        for input in &mut inputs {
            if input.len() == 0 { continue; }                
            let mut new_inputs = Vec::<i32>::new();
            new_inputs.push(*input.last().unwrap());
            loop {
                let x = subtraction(input);
                if x.iter().all(|v| *v == 0) {
                    break;
                }
                *input = x;
                new_inputs.push(*input.last().unwrap());
            }
            predictions.push(new_inputs.iter().sum::<i32>());
        }
        println!("{} {}", utils::santa(9, 1), predictions.iter().sum::<i32>());
    }


    pub fn part2(lines: &Vec<String>) {
        let mut inputs = preprocess(lines);
        let mut predictions = Vec::<i32>::new();
        for input in &mut inputs {
            if input.len() == 0 { continue; }                
            let mut new_inputs = Vec::<i32>::new();
            new_inputs.push(input[0]);
            loop {
                let x = subtraction(input);
                if x.iter().all(|v| *v == 0) {
                    break;
                }
                *input = x;
                new_inputs.push(input[0]);
            }
            let mut res: i32 = 0;
            for i in (0..new_inputs.len()).rev() {
                res = new_inputs[i]-res;
            }
            predictions.push(res);
        }
        println!("{} {}", utils::christmas_tree(9, 2), predictions.iter().sum::<i32>());
    }
}
