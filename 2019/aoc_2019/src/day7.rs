pub mod day7 {
    use std::collections::{HashMap, VecDeque};
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    pub fn solve() {
        let lines = utils::read_input("../instructions7a.txt");
        let mut cmds = VecDeque::<Vec<&str>>::new();
        for l in &lines {
            let parts = l.split_once(" -> ").unwrap();
            let mut temp = Vec::<&str>::new();
            temp.push(parts.1);
            for p in parts.0.split_whitespace() {
                temp.push(p);
            }
            cmds.push_back(temp);
        }
        
        let now = Instant::now();
        
        let res1 = part1(cmds.clone());
        let elapsed = now.elapsed();                
        println!("{} {} ({:.2?})", utils::santa(7, 1), res1, elapsed);
        
        //        let res2 = part2(&inputs);
        //        let elapsed = now.elapsed();
        //        println!("{} {} ({:.2?})", utils::christmas_tree(7, 2), res2, elapsed);        
    }

    fn part1(mut inputs: VecDeque::<Vec<&str>>) -> i32 {
        let mut vars = HashMap::<&str, i32>::new();
        
        while inputs.len() != 0 {
            let m = inputs.pop_front().unwrap();
            if m.len() == 4 {               
                let var1 = ;
                if m[1].to_string().is_digit() {
                    let var1 = m[1].parse::<i32>().unwrap();
                } else {
                    if vars.contains_key(m[1]) {
                        let var1 = vars.get(m[1]).unwrap();
                    } else {
                        let var1 = "";
                    }
                }

                let var2;
                if m[3].to_string().is_digit() {
                    let var2 = m[3].parse::<i32>().unwrap();
                } else {
                    if vars.contains_key(m[3]) {
                        let var2 = vars.get(m[3]).unwrap();
                    } else {
                        let var2 = "";
                    }
                }

                if var1 == "" || var2 = "" {
                    inputs.push_back(m);
                    break;
                }
            }
            //println!("{:?}", m);
            
        //           if vars.contains(instructions[i][0]) {
        //               m = instructions.popleft()
        //                   
        //                   
        //        cmd = decrypt(m)
        //        try:
        //            #print("executing:", cmd)
        //            c = cmd.split("=")
        //            vars[c[0]] = eval(c[1])
        //        except:
        //            instructions.append(m)
        }
        //    vars.get(&"a")
        0
    }
    
    pub fn part2(input: &Vec<String>) {
        //println!("{} {}", utils::christmas_tree(7, 2), tot);
    }
}
