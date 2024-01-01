pub mod day19 {
    use std::collections::HashMap;
    use std::collections::HashSet;
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    fn preprocess() -> (String, HashMap::<String, Vec::<String>>) {
        let lines = utils::read_input("../instructions19a.txt");
        let mut reactions = HashMap::<String, Vec<String>>::with_capacity(50);
        for l in &lines {
            if l == "" {
                break;
            }
            let parts = l.split_once(" => ").unwrap();
            let key = parts.0.to_string();
            if !reactions.contains_key(&key) {
                reactions.insert(key.clone(), Vec::<String>::new());
            }
            reactions.get_mut(&key).unwrap().push(parts.1.to_string());
        }
        let molecule = lines[lines.len()-1].to_string();
        (molecule, reactions)
    }

    pub fn solve () {
        let (molecule, reactions) = preprocess();
        
        let now = Instant::now();
        let res1 = part1(&molecule, &reactions);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::santa(19, 1), res1, elapsed);
        
        let res2 = part2(&molecule, &reactions);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(19, 2), res2, elapsed);
    }
    
    fn part1(molecule: &str, reactions: &HashMap<String, Vec<String>>) -> usize {
        let molec = molecule.to_string();
        let mut new_molecules = Vec::<String>::new();

        for key in reactions.keys() {
            for m in molec.match_indices(key).map(|(i, _)| i).collect::<Vec<usize>>() {
                for repl in reactions.get(key).unwrap() {
                    let new_mol = molec[0..m].to_string() + repl + &molec[m+key.len()..molec.len()].to_string();
                    new_molecules.push(new_mol);
                }
            }
        }

        new_molecules.into_iter().collect::<HashSet<_>>().len()
    }

    fn part2(molecule: &str, reactions: &HashMap<String, Vec<String>>) -> i32 {
        let mut reps = Vec::<[String; 2]>::new();
        for (k, v) in reactions {
            for item in v {
                reps.push([k.to_string(), item.to_string()]);
            }
        }
        
        let mut target = molecule.to_string();
        let mut steps = 0;

        while target != 'e' {
            let tmp = target;
            for (a, b) in reps {
                if !target.contains(b) {
                    continue;
                }

                target = target.replacen(b, a, 1);
                steps += 1;
            }
            
            if tmp == target {
                target = molecule.to_string();
                steps = 0;
                shuffle(reps);
            }
        }
        
        steps
    }
}
    


