pub mod day14 {
    use std::collections::HashMap;
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    fn parse_chem(s: &str) -> (i32, &str) {
        let (units, name) = s.split_once(" ").unwrap();
        (units.parse::<i32>().unwrap(), name)
    }
    
    fn preprocess() -> HashMap::<i32, String> {
        let lines = utils::read_input("../input_14.txt");
        let mut reactions = HashMap::<i32, String>::new();
        for reaction in lines {
            let (input, output) = reaction.split_once(" => ").unwrap();
            let inputs = Vec::<(i32, String)>::new();
            for chem in input.split_once(", ").unwrap() {
                inputs.push(parse_chem(chem));
            }
            let (out_units, out_chem) = parse_chem(output);               
            reactions.insert(out_chem, (out_units, inputs));
        }
        reactions
    }

    pub fn solve () {
        let reactions = preprocess();
        
        let now = Instant::now();
        //let res1 = part1(&mut reindeers);
        //let elapsed = now.elapsed();
        //println!("{} {} ({:.2?})", utils::santa(14, 1), names[res1.0], elapsed);
        
        //let res2 = part2(&mut reindeers);
        //let elapsed = now.elapsed();
        //println!("{} {} ({:.2?})", utils::christmas_tree(14, 2), names[res2.0], elapsed);
    }

    fn part1(reindeers: &mut Vec::<[i32; 6]>) -> (usize, i32) {
        for t in 0..=2502 {
            for i in 0..reindeers.len() {
                let state = t % (reindeers[i][2]+reindeers[i][3]);
                if state < reindeers[i][2] {
                    reindeers[i][4] += reindeers[i][1];
                }
            }
        }
    
        reindeers.sort_by(|a, b| b[4].cmp(&a[4]));
        (reindeers[0][0] as usize, reindeers[0][4])
    }

    fn part2(reindeers: &mut Vec::<[i32; 6]>) -> (usize, i32) {
        reset(reindeers);

        for t in 0..=2502 {
            for i in 0..reindeers.len() {
                let state = t % (reindeers[i][2]+reindeers[i][3]);
                if state < reindeers[i][2] {
                    reindeers[i][4] += reindeers[i][1];
                }
            }
            
            reindeers.sort_by(|a, b| b[4].cmp(&a[4]));
            assign_points(reindeers);
        }
 
        reindeers.sort_by(|a, b| b[5].cmp(&a[5]));
        (reindeers[0][0] as usize, reindeers[0][5])
    }
}

//def minimum_ore(reactions, chem='FUEL', units=1, waste=None):
//    if waste is None:
//        waste = defaultdict(int)
//
//    if chem == 'ORE':
//        return units
//
//    # Re-use waste chemicals.
//    reuse = min(units, waste[chem])
//    units -= reuse
//    waste[chem] -= reuse
//
//    # Work out how many reactions we need to perform.
//    produced, inputs = reactions[chem]
//    n = ceil(units / produced)
//
//    # Determine the minimum ore required to produce each input.
//    ore = 0
//    for required, input in inputs:
//        ore += minimum_ore(reactions, input, n * required, waste)
//
//    # Store waste so it can be re-used
//    waste[chem] += n * produced - units
//    return ore
//    
//def part1(reactions):
//    ore = minimum_ore(reactions)
//    print (f"🎅 Part 1: {ore}")
//    
//def part2(reactions):
//    target = 1000000000000
//    lower = None
//    upper = 1
//
//    # Find upper bound.
//    while minimum_ore(reactions, units=upper) < target:
//        lower = upper
//        upper *= 2
//
//    # Binary search to find maximum fuel produced.
//    while lower + 1 < upper:
//        mid = (lower + upper) // 2
//        ore = minimum_ore(reactions, units=mid)
//        if ore > target:
//            upper = mid
//        elif ore < target:
//            lower = mid
//
//    print (f"🎅🎄 Part 2: {lower}")
//
