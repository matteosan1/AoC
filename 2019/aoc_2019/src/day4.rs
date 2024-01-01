pub mod day4 {
    extern crate crypto;

    //use std::thread;
    //use crossbeam_channel::{unbounded, Sender, Receiver, TryRecvError};
    use crypto::digest::Digest;
    use crypto::md5::Md5;
    use std::fmt;
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    pub fn solve() {
        let now = Instant::now();
        
        let res1 = part1();
        let elapsed = now.elapsed();                
        println!("{} {} ({:.2?})", utils::santa(4, 1), res1, elapsed);
        
        let res2 = part2();
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(4, 2), res2, elapsed);        
    }

    //fn run(input: &str, start: usize, max_iter: usize, str_start: &str, tx: &Sender<i32>, rx: &Receiver<i32>) -> usize {
    //    println!("{}", start);
    //    let mut idx = 0;
    //    while idx < max_iter {
    //        let s = format!("{}{:0>6}", input, idx+start);
    //        let digest = md5::compute(&s);
    //        let hash = format!("{:x}", digest);
    //        if hash.starts_with(str_start) {
    //            println!("done");
    //            let _ = tx.send(1);
    //            return idx + start;
    //        }
    //        
    //        match rx.try_recv() {
    //            Ok(_) | Err(TryRecvError::Disconnected) => {
    //                println!("Terminating.");
    //                break;
    //            }
    //            Err(TryRecvError::Empty) => {}
    //        }
    //        idx += 1;
    //    }
    //    0
    //}

    fn run(input: &str, str_start: &str) -> u32 {
        let mut idx = 10000u32;
        let mut sh = Md5::new();

        loop {
            idx += 1;
            sh.input_str(&fmt::format(format_args!("{}{}", input, idx)));
            if sh.result_str().starts_with(str_start) {
                break;
            }            
            sh.reset();
        }
        idx
    }

    fn part1() -> u32 {
        let input = "bgvyzdsv";     
        run(input, "00000")
    }

    fn part2() -> u32 {
        let input = "bgvyzdsv";     
        run(input, "000000")
        //let input = "bgvyzdsv";
        //let mut children = vec![];
        //let max_iter = 10000000;
        //let step = 1000000;
        //let (tx, rx) = unbounded();
        //
        //for idx in (0..max_iter).step_by(step) {
        //    let tx = tx.clone();
        //    //let rx = rx.clone();
        //    children.push(thread::spawn(move || run(input, idx, step, "000000", &tx, &rx)));
        //}
        //children.into_iter().map(|c| c.join().unwrap()).max().unwrap()
    }
}

