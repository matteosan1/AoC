pub mod day9 {
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    extern crate intcode;
    use intcode::intcode::Machine;

    pub fn solve() {
        let input = utils::read_input("../input_9.txt");
        let program = input[0].split(",").map(|x| x.parse::<isize>().unwrap()).collect::<Vec::<isize>>();
        
        let now = Instant::now();
        
        let res1 = part1(&program);
        let elapsed = now.elapsed();                
        println!("{} {} ({:.2?})", utils::santa(9, 1), res1, elapsed);

        let res2 = part2(&program);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(9, 2), res2, elapsed);        
    }

    fn part1(program: &[isize]) -> isize {
        let mut machine = Machine::with_program(program);
        let mut output = Vec::<isize>::new();
        let input = vec![1];
        let _exit = machine.run(input.iter().copied(), |a| output.push(a));
        *output.last().unwrap()
    }

    fn part2(program: &[isize]) -> isize {
        let mut machine = Machine::with_program(program);
        let mut output = Vec::<isize>::new();
        let input = vec![2];
        let _exit = machine.run(input.iter().copied(), |a| output.push(a));
        *output.last().unwrap()
    }
}
