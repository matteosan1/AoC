use std::fs;

fn main() {
    let file_path = String::from("input_1.txt");

    let contents = fs::read_to_string(file_path)
        .expect("Should have been...");
    
    part1(&contents);
    part2(&contents);
}

fn part1(data: &String) {
    let parts = data.split("\n");

    let mut max_cal = 0;
    let mut cal = 0;
    for p in parts {
        match p.parse::<i32>() {
            Ok(num) => {
                cal = cal + num;
            },
            Err(_) => {
                if max_cal < cal {
                    max_cal = cal;
                }
                cal = 0;
            }
        };
    }

    println!("{}: {}",santa(), max_cal);
}

fn santa() -> char {
    match std::char::from_u32(0x1F385) {
        Some(c) => c,
        None => '�',
    }
}

fn chr_tree() -> char {
    match std::char::from_u32(0x1F384) {
        Some(c) => c,
        None => '�',
    }
}

fn part2(data: &String) {
    let parts = data.split("\n");

    let mut v: Vec<i32> = Vec::new();
    let mut cal = 0;
    for p in parts {
        match p.parse::<i32>() {
            Ok(num) => {
                cal = cal + num;
            },
            Err(_) => {
                v.push(cal);
                cal = 0;
            }
        };
    }

    v.sort();
    v.reverse();
    
    println!("{}: {:?}", chr_tree(), 
        &v[0..3].iter().sum::<i32>());
}