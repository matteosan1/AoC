pub mod day4 {
    extern crate aoc;
    use aoc::utils;

    struct Card {
        win: Vec<u16>,
        mine: Vec<u16>,
        qty: u32
    }
        
    fn preprocess(input: &Vec<String>) -> Vec<Card> {
	let scratchcards: Vec<_> = input.iter().map(|line| {
            let (first, second) = line.split_once(":").unwrap().1.split_once("|").unwrap();
            let win: Vec<_> = first.split_whitespace().map(|y| y.parse::<u16>().unwrap()).collect();
            let mine: Vec<_> = second.split_whitespace().map(|y| y.parse::<u16>().unwrap()).collect();
            Card { win: win, mine:mine, qty: 1}
        }).collect();
	scratchcards
    }

    fn winning(wins: &Vec<u16>, cards: &Vec<u16>) -> u16 {
	let mut points: u16 = 0;
	for w in wins {
	    if cards.contains(&w) { 
		points += 1;
	    }
        }
	points
    }

    pub fn part1(input: &Vec<String>) {
	let scratchcards = preprocess(input);
	let mut tot = 0;
	for card in &scratchcards {
	    let points = winning(&card.win, &card.mine);
	    if points > 0 {
		tot += u16::pow(2, (points-1).into());
	    }
	}
        println!("{} {}", utils::santa(4, 1), tot);
    }
    
    pub fn part2(input: &Vec<String>) {
	let mut scratchcards = preprocess(input);
        
	for idx in 0..scratchcards.len() {
	    let points = winning(&scratchcards[idx].win, &scratchcards[idx].mine);
	    if points > 0 {
                for i in 0..points {
                    let jdx = idx as u16 + (1+i);
                    scratchcards[jdx as usize].qty += scratchcards[idx as usize].qty;
	        }
	    }	
	}
	
	let mut tot = 0;
	for v in &scratchcards {
	    tot += v.qty;
	}
        println!("{} {}", utils::christmas_tree(4, 2), tot);
    }
}
