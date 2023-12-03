pub mod day6 {
    extern crate aoc;
    use aoc::utils;

    pub fn part1(input: &Vec<String>) {
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
        println!("{} {}", utils::santa(6, 1), tot);
    }
    
    pub fn part2(input: &Vec<String>) {
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
        
        println!("{} {}", utils::christmas_tree(6, 2), tot);
    }
}
