fn reset(reindeers: &mut Vec<[i32; 6]>) {
    for r in reindeers {
        r[4] = 0;
    }
}

fn assign_points(reindeers: &mut Vec<[i32; 6]>) {
    let mdist = reindeers.iter().map(|x| x[4]).max().unwrap();
    for r in reindeers {
        if r[4] == mdist {
            r[5] += 1;
        }
    }
}

fn main() {
    let lines = vec![
//"Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
//"Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."    
"Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.",
"Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.",
"Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.",
"Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.",
"Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.",
"Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.",
"Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.",
"Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.",
"Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds."
];

    let mut names = Vec::<&str>::new();
    let mut reindeers = Vec::<[i32; 6]>::new();
    for (i, l) in lines.iter().enumerate() {
        let parts = l[0..l.len()-1].split_whitespace().collect::<Vec<&str>>();
        let speed = parts[3].parse::<i32>().unwrap();
        let t1 = parts[6].parse::<i32>().unwrap();
        let rest = parts[13].parse::<i32>().unwrap();
        names.push(parts[0]);
        reindeers.push([i as i32, speed, t1, rest, 0, 0]);
    }

    for t in 0..=2502 {
        for i in 0..reindeers.len() {
            let state = t % (reindeers[i][2]+reindeers[i][3]);
            if state < reindeers[i][2] {
                reindeers[i][4] += reindeers[i][1];
            }
        }
    }
    
    reindeers.sort_by(|a, b| b[4].cmp(&a[4]));
    println!("{} {}", names[reindeers[0][0] as usize].to_string(), reindeers[0][4]);
    
    reset(&mut reindeers);
    
    for t in 0..=2502 {
        for i in 0..reindeers.len() {
            let state = t % (reindeers[i][2]+reindeers[i][3]);
            if state < reindeers[i][2] {
                reindeers[i][4] += reindeers[i][1];
            }
        }
        
        reindeers.sort_by(|a, b| b[4].cmp(&a[4]));
        assign_points(&mut reindeers);
        //println!("{:?}", reindeers);
    }
 
    reindeers.sort_by(|a, b| b[5].cmp(&a[5]));
    println!("{} {}", names[reindeers[0][0] as usize].to_string(), reindeers[0][5]);
   
}