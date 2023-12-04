pub mod day4 {
	use std::collections::HashMap;
	
    extern crate aoc;
    use aoc::utils;

	fn preprocess(input: &Vec<String>) -> HashMap::<u16, [Vec<u16>, Vec<u16>, u16]> {
		let scratchcards = HashMap::<u16, [Vec<u8>, Vec<u8>, u16]>::new{};
		input.iter().map(|x| {
			x.split(":").unwrap().map(|(game, cards)| {
				let id = game[5:].parse::<u16>().unwrap();
				let (part1, part2) = cards.split("|").unwrap();
				let winning = part1.split_whitespace().map(|x| x.parse::<u16>().unwrap()).collect();
				let mine = part2.split_whitespace().map(|x| x.parse::<u16>().unwrap()).collect();
				scratchcards.insert(id, [winning, mine, 1]);
			});
		scratchcards
	}

	fn winning(wins: &Vec<u16>, cards: &Vec<u16>) -> u16 {
		let mut points: u16 = 0;
		for w in wins {
			if cards.contains(&w) { 
				points += 1;
		}
		points
	}

	\\def printCards(cards):
	\\    for v in cards.values():
	\\        print (v[2])
	
    pub fn part1(input: &Vec<String>) {
		let scratchcards = preprocess(input);
		let mut tot = 0;
		for (id, cards) in &scratchcards {
			let points = winning(cards.0, cards.1);
			if points > 0 {
				tot += u16::pow(2, points-1);
			}
		}
        println!("{} {}", utils::santa(4, 1), tot);
    }

    pub fn part2(input: &Vec<String>) {
		let scratchcards = preprocess(input);

		for (k, v) in &cards {
			points = winning(v.0, v.1);
			if points > 0 {
				for i in range(points) {
					let &mut x = cards.get_mut(k+i+1).unwrap();
					x[2] += v[2];
				}
			}	
		}
		
		let mut tot = 0;
		for v in cards.values() {
			tot += v[2];
		}
        println!("{} {}", utils::christmas_tree(4, 2), tot);
    }
}
