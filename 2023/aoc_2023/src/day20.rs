pub mod day20 {
    use std::collections::{HashMap, VecDeque};
    
    const LOW: bool = false;
    const HIGH: bool = true;
    
    extern crate aoc;
    use aoc::utils;
    
    struct Module<'a> {
        typ: char,
        state: bool,
        connections: HashMap<&'a str, bool>,
        memory: Vec<&'a str>,
    }
    
    struct Pulse<'a> {
        destination: &'a str,
        signal: bool,
        source: &'a str,        
    }

    fn update<'a>( modules : & mut HashMap<&'a str, Module<'a>>,  pulse : Pulse<'a>) -> (Vec< Pulse<'a> >, usize, usize) {
        let mut res_vec : Vec< Pulse<'a> > = Vec::new();
        let mut low_count = 0;
        let mut high_count = 0;
        if let Some(value) = modules.get_mut(pulse.destination) {
            if value.typ == 'b' {
                low_count = value.memory.len();
                for dest in &value.memory {
                    res_vec.push(Pulse { destination: dest, signal: LOW, source: pulse.destination});
                }
            } else if value.typ == '%' && pulse.signal == LOW {
                value.state = !value.state;
                if value.state == LOW {
                    low_count = value.memory.len();
                } else {
                    high_count = value.memory.len();
                }
                for dest in &value.memory {
                    res_vec.push(Pulse { destination: dest, signal: value.state, source: pulse.destination });
                }
            } else if value.typ == '&' {
                value.connections.insert(pulse.source, pulse.signal);
                let mut new_signal = LOW;
                for (_k,v) in &value.connections {
                    if *v == LOW {
                        new_signal = HIGH;
                        break;
                    }
                }
                if new_signal == LOW {
                    low_count = value.memory.len();
                } else {
                    high_count = value.memory.len();
                }
                for dest in &value.memory {
                    res_vec.push( Pulse { destination: dest, signal: new_signal, source: pulse.destination });
                }
            }
        } 
        return (res_vec, low_count, high_count);
    }
    
    pub fn part1(lines: &Vec<String>) {
        let mut modules : HashMap<&str, Module > = HashMap::new();
        let mut reverse : HashMap<&str, Vec<&str>> = HashMap::new();
        
        for line in lines {
            let (sender_and_type, receivers_raw) : (&str, &str) = line.split_once(" -> ").unwrap();
            let typ: char = sender_and_type.chars().nth(0).unwrap();
            let sender: &str = &sender_and_type[1..];
            let mut receivers : Vec<&str> = Vec::new();
            let mut receiver_iterator = receivers_raw.split(", ");
            while let Some(x) = receiver_iterator.next() {
                receivers.push(x);
            }
            
            for r in &receivers {
                if let Some(x) = reverse.get_mut(r) {
                    x.push(sender)
                } else {
                    let mut new_vec : Vec<&str> = Vec::new();
                    new_vec.push(sender);
                    reverse.insert(r, new_vec);
                }
            }
            modules.insert(sender, Module{typ: typ, state:LOW,
                                          connections: HashMap::new(),
                                          memory: receivers});
        }
        
        for (key,value) in &mut modules {
            if value.typ == '&' {
                for m in reverse.get_mut(key).unwrap() {
                    value.connections.insert(m, LOW);
                }
            }
        }
        
        let mut targets : HashMap<&str, usize> = HashMap::new();
        let last_conv = reverse.get("rx").unwrap()[0];
        for target in reverse.get(last_conv).unwrap() { 
            targets.insert(target, 0);
        }
        
        let mut counter = 0;
        let mut low_count = 0;
        let mut high_count = 0;
        let mut p1 = 0;
        let mut p2;
        'simulate:
        loop {
            counter += 1;
            let mut queue : VecDeque< Pulse > = VecDeque::new();
            queue.push_back( Pulse {destination: "roadcaster", signal: LOW, source: ""});
            low_count += 1;
            'process_queue:
            while let Some(current) = queue.pop_front() {
                let next = update( & mut modules, current);
                if next.0.len() == 0 {
                    continue 'process_queue;
                }
                for n in next.0 {
                    if targets.get(n.destination).is_some_and(|_x| n.signal == LOW) {
                        targets.insert(n.destination, counter);
                    }
                    p2 = 1;
                    for (_k,v) in &targets {
                        p2 *= *v;
                    }
                    if p2 != 0 {
                        break 'simulate;
                    }
                    queue.push_back(n);
                }
                low_count += next.1;
                high_count += next.2;
            }
            if counter == 1000 {
                p1 = low_count*high_count;
            }
        }
        println!("{}\n{}", p1, p2);
        //let elapsed = now.elapsed();
        //println!("{} µs", elapsed.as_micros());
    }
       
    //        let mut system: Vec<_> = lines.iter().map(|line| {
    //            let parts: Vec<_> = line.split(" -> ").collect();
    //            let typ = match &line[..1] {
    //                "%" => 1, 
    //                "&" => 2,
    //                "b" => 0,
    //                _   => -1
    //            };
    //            let name = match typ {
    //                1 => parts[0][1..].to_string(),
    //                2 => parts[0][1..].to_string(),
    //                0 => parts[0].to_string(),
    //                _ => String::from("")
    //            };
    //            Module { typ: typ, name: name, 
    //                     dest: parts[1].split(", ").map(|x| x.to_string()).collect(),
    //                     memory: HashMap::<String, i8>::new()}
    //        }).collect();
    //        system.push(Module{ typ: 0, name: String::from("rx"),
    //                            dest: Vec::<String>::new(),
    //                            memory: HashMap::<String, i8> });
    //        println!("{:?}", system);
    //    }
    //    
    //    pub fn part1(lines: &Vec<String>) {
    //        preprocess(lines);
    //
    //        let mut counter = [0, 0];
    //        let mut cycle = 0;
    //        loop {
    //            new_output = modules['broadcaster'].receive(0)
    //                counter[0] += 1
    //                count_pulses(new_output, counter)
    //                
    //                while len(new_output) != 0:
    //            output = []
    //            for o in new_output:
    //                output += modules[o[0]].receive(o[1])
    //            new_output = output
    //                count_pulses(new_output, counter)
    //        
    //                cycle += 1;
    //                if cycle == 1000 {
    //                    break;
    //                }
    //        }
    //        println!("{}", counter[1]*counter[0]);
    //        //println!("{} {}", utils::santa(20, 1), );
    //    }
    //
    pub fn part2(lines: &Vec<String>) {
        
        //println!("{} {}", utils::christmas_tree(20, 2), );
    }
}
