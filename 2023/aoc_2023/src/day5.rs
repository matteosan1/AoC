// implementare parte 2 location to seed...
pub mod day5 {
    extern crate aoc;
    use aoc::utils;

    #[derive(Copy, Clone)]
    struct Range {
        dest: i64,
        source: i64,
        length: i64,
    }
    
    fn preprocess(input: &Vec<String>) -> (Vec::<i64>, Vec::<Vec::<Range>>) {
        let mut data = Vec::<Vec::<Range>>::new();
        let mut seeds = Vec::<i64>::new();
        let mut ranges = Vec::<Range>::new();
        
        for l in input {
            if l.contains("seeds:") {
                let x = match l.split_once("seeds:") {
                    Some(x) => x.1,
                    _ => "",
                };
                seeds = x.split_whitespace().map(|x| x.parse::<i64>().unwrap()).collect();
            } else if l.ends_with("map:") {
                if ranges.len() > 0 {
                    data.push(ranges.clone());
                    ranges.clear();
                }
            } else if l == "" {
                continue;
            } else {
                let x: Vec<i64> = l.split_whitespace().map(|x| x.parse::<i64>().unwrap()).collect();
                let range = Range { dest: x[0], source: x[1], length: x[2] };
                ranges.push(range);
            }
        }
        data.push(ranges);
        //    for k, v in data.items():
        //        if k == 'seed':
        //            continue
        //        data[k].sort(key=itemgetter(1))
        (seeds, data)
    }

    fn mapping(seed: &i64, map: &Range) -> Result<i64, &'static str> {
        if *seed >= map.source && *seed <= map.source+map.length {
            return Ok((seed - map.source) + map.dest);
        }

        Err("not in range")
    }
    
    pub fn part1(input: &Vec<String>) {
        let (mut seeds, maps) = preprocess(input);
        for map in maps {
            for i in 0..seeds.len() {
                for m in &map {
                    match mapping(&seeds[i], &m) {
                        Ok(x) => {
                            seeds[i] = x;
                            break;
                        },
                        Err(_x) => continue
                    };
                }
            }
        }
        let min_location = seeds.iter().min().unwrap();
        println!("{} {}", utils::santa(5, 1), min_location);
    }


    pub fn part2(input: &Vec<String>) {
        
        //println!("{} {}", utils::christmas_tree(5, 2), );
    }
}
