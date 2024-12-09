pub mod day16 {
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    fn preprocess() -> Vec::<i32> {
        let lines = utils::read_input("../input_16.txt");
        let mut digits = Vec::new();

        for char in lines[0].chars() {
            if let Some(digit) = char.to_digit(10) {
                digits.push(digit as i32);
            } else {
                println!("Invalid character: {}", char);
            }
        }

        digits.into_iter().collect::<Vec<i32>>()
    }
    
    pub fn solve () {
        let input = preprocess();
        
        let now = Instant::now();
        
        let res1 = part1(input.clone());
        let elapsed = now.elapsed();
        println!("{:?} {} ({:.2?})", utils::santa(16, 1), res1, elapsed);
        
        let res2 = part2(&input);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(16, 2), res2, elapsed);
    }

    fn build_pattern(phase: i32, pattern: &mut [i32]) {
        let base_pattern = [0, 1, 0, -1];
        let mut idx = 0;
        let mut counter = 1;
        for i in 0..pattern.len() {
            if counter == phase {
                counter = 0;
                idx += 1;
                idx %= 4;
            }
            pattern[i] = base_pattern[idx];
            counter += 1;
        }
    }

    fn part1(mut input: Vec::<i32>) -> i32 {
        let mut pattern = vec![0; input.len()];
        let mut temp = vec![0; input.len()];
        for _ in 0..100 {
            for i in 0..input.len() {
                build_pattern((i+1) as i32, &mut pattern);
                let mut val = 0;
                for x in 0..input.len() {
                    val += pattern[x]*input[x];
                }
                temp[i] = i32::abs(val)%10;
            }
            input = temp.clone();
        }

        convert_to_number(&input, 8)
    }

    fn convert_to_number(input: &Vec::<i32>, size: usize) -> i32 {
        let mut res = 0;
        for i in 0..size {
            res += input[i]*i32::pow(10, (size-i-1) as u32);
        }
        res
    }
    
    fn part2(input: &Vec::<i32>) -> i32 {
        let offset = convert_to_number(input, 7);
        let y: Vec<i32> = input.into_iter().cycle().take(input.len() * 10000).collect::<Vec::<i32>>();
        0
    //input = np.array(list(reversed((input*10000)[offset:])))
    //for phase in range(100):
    //    fft = np.mod(np.cumsum(input), 10)
    //    input = fft.copy()
    //        //print (f"🎅🎄 Part 2: {''.join(list(map(str, reversed(input[-8:]))))}")
    }    
}
    

