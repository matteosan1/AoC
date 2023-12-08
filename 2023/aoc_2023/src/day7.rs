// make part 2 assuming best J choice to be the highest recurring card
pub mod day7 {
    use std::collections::HashMap;
    
    extern crate aoc;
    use aoc::utils;

    fn count_cards(hand: &str) -> i32 {
        let wins: HashMap::<[i32; 2], i32> = HashMap::from([([5,0], 6), ([4,1], 5), ([3,2], 4), ([3,1], 3), 
                                                            ([2,2], 2), ([2,1], 1), ([1,1], 0)]);

        let letter_counts: HashMap<char, i32> =
            hand.chars()
            .fold(HashMap::new(), |mut map, c| {
                *map.entry(c).or_insert(0) += 1;
                map
            });
        let mut res: Vec<_> = letter_counts.values().cloned().collect();
        if res.len() == 1 {
            return 6;
        }
        res.sort();
        res.reverse();
        *wins.get(&res[0..2]).unwrap()
    }

    fn preprocess(input: &Vec<String>) -> Vec::<(i32, i32, i32)> {
        let cards: HashMap<char, i32> = HashMap::<char, i32>::from([('A', 12), ('K', 11), ('Q', 10), ('J', 9), ('T', 8), ('9', 7), 
                                                                    ('8', 6), ('7', 5), ('6', 4), ('5', 3), ('4', 2), ('3', 1), ('2', 0)]);
        let mut hands = Vec::<(i32, i32, i32)>::new();
        
        for i in 0..input.len() {
            let mut val = 0;
            let (hand, bid) = input[i].split_once(" ").unwrap();
            let count = count_cards(hand);
            for (j, c) in hand.chars().rev().enumerate() {
                val += i32::pow(13, j as u32)*cards.get(&c).unwrap();
            }
            hands.push((val, count, bid.parse::<i32>().unwrap()));
        }
        hands
    }

    pub fn part1(input: &Vec<String>) {
        let mut hands = preprocess(input);
        hands.sort_by_key(|tuple| (tuple.1, tuple.0));
        let mut points = 0;
        for (i, h) in hands.iter().enumerate() {
            points += (i+1)as i32 *h.2;
        }
        
        println!("{} {}", utils::santa(7, 1), points);
    }


    pub fn part2(input: &Vec<String>) {
        
        //println!("{} {}", utils::christmas_tree(7, 2), );
    }
}


//
//const cards_with_jocker = HashMap::<str, i32>::from([("A", 13), ("K", 12), ("Q", 11), ("T", 9), ("9", 8), 
//                                         ("8", 7), ("7", 6), ("6", 5), ("5", 4), ("4", 3), ("3", 2), ("2", 1), ("J", 0)]);
//static mut part = 1;
//
//struct Hand {
//    hand: str,
//    bid: i32,
//    typ: [i32; 5]
//}
//

//fn find_rank(hand: &str) -> [i32; 5] {
//    let rank = hand.chars().
//    self.c = tuple(sorted(Counter(self.h).values()))
//    self.rank = wins[self.c]
//    if self.part == 2 and 'J' in self.h:
//        max_rank = self.rank
//        max_hand = self.h
//        for c in cards:
//            new_hand = self.h.replace("J", c)
//            new_rank = wins[tuple(sorted(Counter(new_hand).values()))]
//            if new_rank > max_rank:
//                max_hand = new_hand
//                max_rank = new_rank
//        self.rank = max_rank
//        self.max_h = max_hand
//}
//
//impl Hand {
//    fn new(h: &str) -> &Self {
//        
//        Hand {}
//    }
//}
//
//impl PartialEq for Hand {
//    fn eq(&self, other: &Self) -> bool {
//        self.student_id == other.student_id
//    }
//}
//
//impl PartialOrd for SomeNum {
//    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
//        //Some(self.cmp(other))
//        //(self.value, &self.name).cmp(&(other.value, &other.name))
//        if self.part == 2 {
//            for i in 0..self.hand.len() {
//                if self.hand[i] != other.h[i]:
//                    if self.part == 1:
//                        return cards[self.h[i]] < cards[other.h[i]]
//                    else:
//                        return cards_with_jocker[self.h[i]] < cards_with_jocker[other.h[i]]
//
//        }
//        
//        Some(self.typ < other.typ)
//    }
//}
//
//class Hand:
//    def __init__(self, h, bid, part=1):
//        self.part = part
//        self.h = h
//        self.find_rank()
//        self.bid = bid
//
//   def __lt__(self, other):
//        if self.rank != other.rank:
//            return self.rank < other.rank
//        else:
//            for i in range(5):
//                if self.h[i] != other.h[i]:
//                    if self.part == 1:
//                        return cards[self.h[i]] < cards[other.h[i]]
//                    else:
//                        return cards_with_jocker[self.h[i]] < cards_with_jocker[other.h[i]]
//    def __str__(self):
//        return str(self.h)
//
//def loadInput(part):
//    lines = readInput("input_7.txt")
//    hands = []
//    bids = []
//    for l in lines:
//        hand, bid = l.split()
//        hands.append(Hand(hand, int(bid), part))
//
//    return sorted(hands)
//
//def part1(hands):
//    points  = 0
//    for ih, h in enumerate(hands):
//        points += (ih+1) * h.bid
//
//def part2(hands):
//    points  = 0
//    for ih, h in enumerate(hands):
//        points += (ih+1) * h.bid
