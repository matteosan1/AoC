pub mod day6 {
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    fn preprocess() -> Vec::<[[usize;2]; 2]> {
        let mut inputs = Vec::<[[usize;2]; 2]>::new();
        let lines = utils::read_input("../instructions6a.txt");
        for line in lines {
            let parts: Vec<_> = line.split(" ").collect();
            
            let keyword;
            let mut idx = (2, 4);
            if parts[0] == "turn" {
                keyword = parts[1];
            } else {
                keyword = "toggle";
                idx = (1, 3);
            }
            
            let c1 = parts[idx.0].split_once(",").unwrap();//.map(|x| *x.parse::<usize>().unwrap());//.collect();
            let c2 = parts[idx.1].split_once(",").unwrap();//.map(|x| *x.parse::<usize>().unwrap());//.collect();         
            //println!("{}", c1);
            //let c2: Vec<_> = parts[idx.1].split(",")
            //    .map(|x| x.parse::<usize>().unwrap()).collect();
            inputs.push([[c1.0.parse::<usize>().unwrap(), c1.1.parse::<usize>().unwrap()],
                         [c2.0.parse::<usize>().unwrap(), c2.1.parse::<usize>().unwrap()]]); 
            //println!("{:?} {:?}", c1, c2);
        }
        inputs
    }

    pub fn solve() {
        let inputs = preprocess();
        let now = Instant::now();
        
        let res1 = part1(&inputs);
        let elapsed = now.elapsed();                
        println!("{} {} ({:.2?})", utils::santa(6, 1), res1, elapsed);
        
//        let res2 = part2(&inputs);
//        let elapsed = now.elapsed();
//        println!("{} {} ({:.2?})", utils::christmas_tree(6, 2), res2, elapsed);        
    }

    fn part1(inputs: &Vec::<[[usize;2]; 2]>) -> u32 {
        let mut lights = vec![[0u8; 1000]; 1000];
        
        for c in inputs {
            for row in &mut lights[c[0][0]..=c[1][0]] {
                for light in &mut row[c[0][1]..=c[1][1]] {
                    *light = match keyword {
			"on" => 1,
			"off" => 0,
                        "toggle" => if *light == 1 {0} else {1},
                        _ => 0
		    };
                }
            }
        }

        let mut tot: u32 = 0;
        for row in &mut lights[..] {
		for light in &mut row[..] {
			tot += *light as u32;
		}
	}
        tot
    }
    
    fn part2(input: &Vec<String>) -> u32 {
        let mut lights = vec![[0u8; 1000]; 1000];
        
        for line in input.iter() {
            let parts: Vec<_> = line.split(" ").collect();
            
            let keyword;
            let mut idx = (2, 4);
            if parts[0] == "turn" {
                keyword = parts[1];
            } else {
                keyword = "toggle";
                idx = (1, 3);
            }
            
            let c1: Vec<_> = parts[idx.0].split(",")
                .map(|x| x.parse::<usize>().unwrap()).collect();
            let c2: Vec<_> = parts[idx.1].split(",")
                .map(|x| x.parse::<usize>().unwrap()).collect();
            for row in &mut lights[c1[0]..=c2[0]] {
                for light in &mut row[c1[1]..=c2[1]] {
                    *light = match keyword {
			"on" => *light + 1,
			"off" => if *light <= 0 {0} else {*light - 1},
                        "toggle" => *light + 2,
                        _ => 0
		    };
                }
            }
        }

        let mut tot: u32 = 0;
        for row in &mut lights[..] {
	    for light in &mut row[..] {
		tot += *light as u32;
	    }
	}
        tot
    }
}
