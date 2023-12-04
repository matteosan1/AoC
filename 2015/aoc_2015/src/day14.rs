pub mod day14 {
    use regex::Regex;
    use std::cmp::min;
    use std::cmp::Ordering;
    use std::collections::HashMap;
    
    extern crate aoc;
    use aoc::utils;

    struct Reindeer {
        speed: i32,
        time: i32,
        rest: i32,
        name: String,
        dist: i32,
    }

    impl Ord for Reindeer {
        fn cmp(&self, other: &Self) -> Ordering {
            self.dist.cmp(&(other.dist))
        }
    }
    
    impl PartialOrd for Reindeer {
        fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
            Some(self.cmp(other))
        }
    }
    
    impl PartialEq for Reindeer {
        fn eq(&self, other: &Self) -> bool {
            self.dist == other.dist
        }
    }
    
    impl Eq for Reindeer { }
    
    impl Reindeer {
        fn run(self: &mut Reindeer, t: i32) {
            self.dist = t/(self.time + self.rest)*self.speed*self.time + min(t%(self.time+self.rest), self.time)*self.speed;
        }
    }
    
    fn initialize(input: &Vec<String>, players: &mut Vec::<Reindeer>, ranking: &mut HashMap::<String, i32>) {
        let re = Regex::new(r"^(\w+)( \w+)+ (\d+) km\/s for (\d+) seconds,( \w+)+ (\d+)").unwrap();
        
        for line in input.iter() {
            for (_, [name, _, speed, time, _, rest]) in re.captures_iter(line).map(|c| c.extract()) {
                players.push(Reindeer {speed: speed.parse::<i32>().unwrap(),
                                       time: time.parse::<i32>().unwrap(),
                                       rest: rest.parse::<i32>().unwrap(),
                                       name: name.to_string(), dist: 0 as i32});
                ranking.insert(name.to_string(), 0);
            }
        }
    }
    
    pub fn part1(input: &Vec<String>) {
        let mut players = Vec::<Reindeer>::with_capacity(9);
        let mut ranking = HashMap::<String, i32>::new();
        initialize(&input, &mut players, &mut ranking);
        
        for p in &mut players {
            p.run(2503);
        }
        
        players.sort();
        players.reverse();
        
        println!("{} {}-{}", utils::santa(14, 1), players[0].name, players[0].dist);
    }
    
    pub fn part2(input: &Vec<String>) {
        let mut players = Vec::<Reindeer>::with_capacity(9);
        let mut ranking = HashMap::<String, i32>::new();
        initialize(&input, &mut players, &mut ranking);

        for t in 1..=2503 {
            for p in &mut players {
                p.run(t);
            }

            players.sort();
            players.reverse();
            let names = players.iter().filter(|x| x.dist == players[0].dist);
            for n in names {
                let score = ranking.get_mut(&n.name).unwrap();
                *score += 1;
            }
        }

        let max_score = ranking.values().max();
        println!("{} {}", utils::christmas_tree(14, 2), max_score.unwrap());
    }
}
