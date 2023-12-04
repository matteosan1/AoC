pub mod day5 {
    use std::collections::HashMap;
    
    extern crate aoc;
    use aoc::utils;

    fn is_vowel(c: &char) -> bool {
	matches!(*c, 'a' | 'e' | 'i' | 'o' | 'u')
    }

    fn is_illegal_pair(c1: &char, c2: &char) -> bool {
	let s = [*c1, *c2].iter().collect::<String>();
        ["ab","cd","pq","xy"]
	    .iter()
	    .any(|&i| i==s)
    }

    pub fn part1(input: &Vec<String>) {
        let mut part = 0;
        
        for line in input.iter() {
            let mut vowel_count: u32 = 0;
            let chars = line.chars();
            let mut last_char: char = ' ';
            let mut double: bool = false;
            let mut all_legal: bool = true;
	    
            for c in chars {
                if is_vowel(&c) {vowel_count += 1;};
                if !double && &c == &last_char {double = true};
                if is_illegal_pair(&last_char, &c) {all_legal = false};
                last_char = c.clone();
            };
            
            if vowel_count >= 3 && double && all_legal {
                part += 1;
            };
        }
        
        println!("{} {}", utils::santa(5, 1), part);
    }
    
    pub fn part2(input: &Vec<String>) {
        let mut part = 0;
        
        for line in input.iter() {
            let chars = line.chars();
            
	    let mut last_char: char = ' ';
	    let mut second_to_last_char: char = ' ';
	    let mut offset_double: bool = false;
	    let mut substrings = HashMap::new();
	    let mut contains_repeat: bool = false;
	    
	    for c in chars {	
		if !offset_double && &c == &second_to_last_char {offset_double = true};
		let current_pair = [last_char, c].iter().collect::<String>();
		if !contains_repeat && substrings.contains_key(&current_pair) {contains_repeat = true};
		
		substrings.insert(
		    [second_to_last_char, last_char].iter().collect::<String>(),
		    true
		);
		second_to_last_char = last_char.clone();
		last_char = c.clone();
	    };
            
	    if offset_double && contains_repeat {
		part += 1;
	    }
        }
        println!("{} {}", utils::christmas_tree(5, 2), part);
    }
}
