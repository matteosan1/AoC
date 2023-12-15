pub mod day15 {
    extern crate aoc;
    use aoc::utils;

    fn hash_algo(instr: &str) -> u32 {
        let mut val: u32 = 0;
        for c in instr.chars() {
            val += c as u32;
            val *= 17;
            val %= 256;
        }

        val
    }
    
    pub fn part1(lines: &Vec<String>) {
        let instrs: Vec<_> = lines[0].split(",").collect();
        let checksum: u32 = instrs.iter().map(|code| hash_algo(code)).sum();

        println!("{} {}", utils::santa(15, 1), checksum);
    }

    #[derive(Debug)]
    struct Lens {
        code: String,
        focal: i32
    }

    type MyBox = Vec<Lens>;

    fn focusing_power(boxes: &Vec<MyBox>) -> i32 {
        let mut val: i32 = 0;
        for b in 0..boxes.len() {
            for l in 0..boxes[b].len() {
                val += (b as i32 +1)*(l as i32 +1)*boxes[b][l].focal;
            }
        }
        val
    }
    
    pub fn part2(lines: &Vec<String>) {
        let mut boxes = Vec::<MyBox>::with_capacity(256);
        for i in 0..256 {
            boxes.push(Vec::<Lens>::new());
        }
        
        let instrs: Vec<_> = lines[0].split(",").collect();
        for instr in instrs {
            if instr.contains('=') {
                let Some((label, value)) = instr.split_once("=") else { todo!{} };
                let abox = hash_algo(label) as usize;
                let focal = value.parse::<i32>().unwrap();
                if let Some(index) = boxes[abox].iter().position(|x| x.code == label) {
                    boxes[abox][index].focal = focal;
                } else {
                    boxes[abox].push(Lens { code:label.to_string(), focal: focal });
                }
            } else {
                let label = instr[0..instr.len()-1].to_string();
                let abox = hash_algo(&label) as usize;
                if let Some(index) = boxes[abox].iter().position(|x| x.code == label) {
                    boxes[abox].remove(index);
                }
            }
        }

        println!("{} {}", utils::christmas_tree(15, 2), focusing_power(&boxes));
    }
}
