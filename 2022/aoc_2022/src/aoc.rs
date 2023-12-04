pub mod aoc3 {
    pub fn part1() -> u32 {
        let input = std::fs::read_to_string("input_3.txt").unwrap();

        input.lines()
            .filter_map(|line| {
                let line = line.as_bytes();
                let (left, right) = line.split_at(line.len()/2);

                left.iter()
                    .find(|item| right.contains(item))
                    .map(|item| match item {
                        b'a'..=b'z' => (item - b'a') + 1,
                        _ => (item - b'A') + 1 + 26,
                    } as u32)
            })
            .sum()
    }

    use itertools::Itertools;
    pub fn part2() -> u32 {
        let input = std::fs::read_to_string("input_3.txt").unwrap();

        input.lines()
            .map(|line| line.as_bytes())
            .tuples()
            .filter_map(|(sack1, sack2, sack3)| {
                sack1
                    .iter()
                    .find(|item| sack2.contains(item) && sack3.contains(item))
                    .map(|item| match item {
                        b'a'..=b'z' => (item - b'a') + 1,
                        _ => (item - b'A') + 1 + 26,
                    } as u32)
            })
            .sum()
    }
}

pub mod aoc4 {
    pub fn part1() -> usize {
        let input = std::fs::read_to_string("input_4.txt").unwrap();

        input.lines()
            .filter(|line| {
                let (elf1, elf2) = line.split_once(",").unwrap();
                let (min1, max1) = elf1.split_once("-").unwrap();
                let (min2, max2) = elf2.split_once("-").unwrap();
                let min1: u32 = min1.parse().unwrap();
                let max1: u32 = max1.parse().unwrap();
                let min2: u32 = min2.parse().unwrap();
                let max2: u32 = max2.parse().unwrap();

                (min1 <= min2 && max1 >= max2) || (min2 <= min1 && max2 >= max1)
            })
            .count()
    }

    pub fn part2() -> usize {
        let input = std::fs::read_to_string("input_4.txt").unwrap();

        input.lines()
            .filter(|line| {
                let (elf1, elf2) = line.split_once(",").unwrap();
                let (min1, max1) = elf1.split_once("-").unwrap();
                let (min2, max2) = elf2.split_once("-").unwrap();
                let min1: u32 = min1.parse().unwrap();
                let max1: u32 = max1.parse().unwrap();
                let min2: u32 = min2.parse().unwrap();
                let max2: u32 = max2.parse().unwrap();

                max1 >= min2 && min1 <= max2
            })
            .count()
    }
}

pub mod aoc5 {
    struct Instruction {
        amount: usize,
        from: usize,
        to: usize,
    }

    use itertools::Itertools;
    pub fn part1() -> usize {
        let input = std::fs::read_to_string("input_5.txt").unwrap();
        let (left, instructions_str) = input.split_once("\n\n").unwrap();
        let (stacks_str, platforms) = left.rsplit_once('\n').unwrap();
        let num_stacks = platforms.split_whitespace().last().unwrap().parse().unwrap();
        let mut stacks = vec![Vec::new(); num_stacks];


        input.lines()
            .filter(|line| {
                let (elf1, elf2) = line.split_once(",").unwrap();
                let (min1, max1) = elf1.split_once("-").unwrap();
                let (min2, max2) = elf2.split_once("-").unwrap();
                let min1: u32 = min1.parse().unwrap();
                let max1: u32 = max1.parse().unwrap();
                let min2: u32 = min2.parse().unwrap();
                let max2: u32 = max2.parse().unwrap();

                (min1 <= min2 && max1 >= max2) || (min2 <= min1 && max2 >= max1)
            })
            .count()
    }
}