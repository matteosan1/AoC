pub mod day21 {
    use std::collections::HashMap;
    use itertools::Itertools;
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;
    
    pub fn solve () {
        let now = Instant::now();
        let res1 = part1();
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::santa(21, 1), res1, elapsed);
    
        //let elapsed = now.elapsed();
        //println!("{} {} ({:.2?})", utils::christmas_tree(21, 2), res2, elapsed);
    }

    fn part1() -> i32 {
        let weapons: HashMap::<&str, (i32, i32)>  =
            HashMap::<&str, (i32, i32)>::from([("Dagger"   ,(8, 4 )),
                                               ("Shortsword",(10, 5)),
                                               ("Warhammer" ,(25, 6)),
                                               ("Longsword" ,(40, 7)),
                                               ("Greataxe"  ,(74, 8))]);
        let armors: HashMap::<&str, (i32, i32)> =
            HashMap::<&str, (i32, i32)>::from([("None"      ,(0,0   )),
                                               ("Leather"  ,(13, -1)),
                                               ("Chainmail" ,(31, -2)),
                                               ("Splintmail",(53, -3)),
                                               ("Bandedmail",(75, -4)),
                                               ("Platemail" ,(102,-5))]);
        let rings_p: HashMap::<&str, (i32, i32)> =
            HashMap::<&str, (i32, i32)>::from([("No ring"  ,(0, 0  )),
                                               ("Damage +1",(25, 1 )),
                                               ("Damage +2",(50, 2 )),
                                               ("Damage +3",(100, 3))]);
        let rings_m: HashMap::<&str, (i32, i32)> =
            HashMap::<&str, (i32, i32)>::from([("No ring"   ,(0, 0  )),
                                               ("Defense +1",(20, -1)),
                                               ("Defense +2",(40, -2)),
                                               ("Defense +3",(80, -3))]);

        let boss = vec![109, 8, -2]; //power_b = 109 damage_b = 8 armor_b = -2
        let hit_points = 100;

        //let res = [];
        let mut cost_min = 500;
        //let mut choice = (-1, -1, -1, -1);
        let rings_p_comb: Vec<_> = rings_p.keys().into_iter().combinations(2).collect();
        let rings_m_comb: Vec<_> = rings_m.keys().clone().into_iter().combinations(2).collect();
            
        for (k, v) in weapons {
            for kr1 in &rings_p_comb {
                let A = -(v.1 + rings_p[kr1[0]].1 + rings_p[kr1[1]].1 + boss[2])/boss[0]*hit_points + boss[1];
                for (k1, v1) in armors {
                    let no_ring1 = kr1.iter().filter(|x| ***x == "No ring").count();
                    for kr2 in &rings_m_comb {
                        let no_ring2 = kr2.iter().filter(|x| ***x == "No ring").count();
//                        if no_ring2 + no_ring1 >= 2 {
//                            if (v1.1 + rings_m[kr2[0]].1 + rings_m[kr2[1]].1) < -A {
//                                let cost = v.0 + rings_p[kr1[0]].0 + rings_p[kr1[1]].0 + v1.0 + rings_m[kr2[0]].0 + rings_m[kr2[1]].0;
//                                if cost < cost_min {
//                                    //choice = (k, k1, kr1, kr2);
//                                    println!("{}", cost);
//                                    cost_min = cost;
//                                }
//                            }
//                        }
                    }
                }
            }
        }
        0
    }

//def sim(choice, PP, PB, DB, AB):
//    DP = weapons[choice[0]][1]
//    AP = armors[choice[1]][1]
//    ring1 = rings_p[choice[2][0]][1]
//    ring2 = rings_p[choice[2][1]][1]
//    ring3 = rings_m[choice[3][0]][1]
//    ring4 = rings_m[choice[3][1]][1]
//
//    while True:
//        PB -= max(1, DP + ring1 + ring2 + AB)
//        if PB <= 0:
//            return True
//        PP -= max(1, DB + AP + ring3 + ring4)
//        if PP <= 0:
//            return False
}
