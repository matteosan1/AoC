pub mod day2 {
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    extern crate intcode;
    use intcode::intcode::Machine;

    pub fn solve() {
        let input = utils::read_input("../input_2.txt");
        let program = input[0].split(",").map(|x| x.parse::<isize>().unwrap()).collect::<Vec::<isize>>();
        
        let now = Instant::now();
        
        let res1 = part1(&program);
        let elapsed = now.elapsed();                
        println!("{} {} ({:.2?})", utils::santa(2, 1), res1, elapsed);

        let res2 = part2(&program);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(2, 2), res2, elapsed);        
    }

    fn part1(program: &[isize]) -> isize {
        let mut machine = Machine::with_program(program);
        let mut output = Vec::<isize>::new();
        machine.mem_mut()[1] = 12;
        machine.mem_mut()[2] = 2;
        let _exit = machine.run([], |a| output.push(a));
        machine.mem()[0]
    }

    fn part2(program: &[isize]) -> isize {
        for noun in 1..100 {
            for verb in 1..100 {
                let mut machine = Machine::with_program(program);
                let mut output = Vec::<isize>::new();
                machine.mem_mut()[1] = noun;
                machine.mem_mut()[2] = verb;
                let _exit = machine.run([], |a| output.push(a));
                if machine.mem()[0] == 19690720 {
                    return noun*100 + verb;
                }
            }
        }
        0
    }
}
