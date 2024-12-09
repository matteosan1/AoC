pub mod day10 {
    use std::time::Instant;
    use std::f32::consts::PI;
    use std::cmp::Ordering;
    
    extern crate aoc;
    use aoc::utils;

    fn preprocess() -> Vec<(isize, isize)> {
        let lines = utils::read_input("../input_10.txt");
        let mut asteroids = Vec::<(isize, isize)>::new();
        for (y, l) in lines.iter().enumerate() {
            for (x, c) in l.chars().enumerate() {
                if c  == '#' {
                    asteroids.push((x as isize, y as isize));
                }
            }
        }
        asteroids
    }
    
    pub fn solve () {
        let asteroids = preprocess();
        let now = Instant::now();

        let res1 = part1(&asteroids);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::santa(10, 1), res1.0, elapsed);

        let res2 = part2(&asteroids, &res1.1);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(10, 2), res2, elapsed);
    }

    fn prune(v: &Vec::<f32>) -> usize {
        let mut doubles = 0 as usize;
        for i in 0..v.len()-1 {
            for j in i+1..v.len() {
                if f32::abs(v[i] - v[j]) < 1e-8 {
                    doubles += 1;
                    break;
                }
            }
        }
        v.len() - doubles        
    }
    
    fn part1(asteroids: &Vec<(isize, isize)>) -> (usize, usize) {
        let mut seen = Vec::<usize>::new();
        for a in asteroids {
            let mut angles = Vec::<f32>::new();
            for x in asteroids {
                if x == a {
                    continue;
                }
                let diff = ((x.1-a.1) as f32, (x.0-a.0) as f32);
                angles.push(diff.1.atan2(diff.0));
            }
            seen.push(prune(&angles));
        }
        (*seen.iter().max().unwrap(),
         seen.iter().enumerate().max_by(|(_, a), (_, b)| a.cmp(b))
         .map(|(index, _)| index).unwrap())

    }

    fn angle(a: &(isize, isize)) -> f32 {
        let coord = (a.0 as f32, a.1 as f32);
        let mut val = coord.1.atan2(coord.0);
        if val < -PI/2.0 {
            val += 2.0*PI + PI/2.;
        } else if val >= -PI/2. {
            val += PI/2.;
        }
        val
    }

    //#[derive(Clone)]
    //struct Asteroid {
    //    pos: (isize, isize),
    //    ang: f32,
    //    dist: f32
    //}
    //
    //fn create_asteroid(a: &(isize, isize), station: &(isize, isize)) -> Asteroid {
    //    let new_pos = (a.0-station.0, a.1-station.1);
    //    Asteroid { pos: new_pos, ang: angle(a), dist: f32::sqrt((a.0^2+a.1^2) as f32) }
    //}

    
    //impl PartialEq for Asteroid {
    //    fn eq(&self, other: &Self) -> bool {
    //        self.ang == other.ang && self.dist == other.dist
    //    }
    //}
    //
    //impl Ord for Asteroid {
    //    fn cmp(&self, other: &Self) -> Ordering {
    //        if self.ang < other.ang {
    //            Ordering::Less
    //        } else if self.ang > other.ang {
    //            Ordering::Greater
    //        } else if self.dist < other.dist {
    //            Ordering::Less
    //        } else if self.dist > other.dist {
    //            Ordering::Greater
    //        } else {
    //            Ordering::Equal
    //        }
    //    }
    //}
    //
    //impl PartialOrd for Asteroid {
    //    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
    //        Some(self.cmp(other))
    //    }
    //}

    fn part2(asteroids: &Vec<(isize, isize)>, station: &usize) -> isize {
        0
//        let mut new_asteroids = Vec::<Asteroid>::new();
//        for a in asteroids {
//            new_asteroids.push(create_asteroid(a, &asteroids[*station]));
//        }
//        //new_asteroids.sort_by_key(|x| (x.ang, x.dist));
//        //new_asteroids.sort();
//        
//        let mut n = 0;
//        //let mut vaporized = Vec::<Asteroid>::new();
//        while new_asteroids.len() != 0 {
//            let mut prev = 111111111111111111.1;
//            let mut left_over = Vec::<Asteroid>::new();
//            for i in 0..new_asteroids.len() {
//                if new_asteroids[i].dist == 0.0 {
//                    continue;
//                }
//                if new_asteroids[i].ang == prev {
//                    left_over.push(new_asteroids[i].clone());
//                    // print ("left ", sorted_ast[i][0]+station, sorted_ast[i][1:])
//                } else {                    
//                    n += 1;
//                    //vaporized.push(new_asteroids[i]);
//                    // print (f"vaporized {n}", sorted_ast[i][0]+station, sorted_ast[i][1:])
//                }
//                if n == 200 {
//                    let pos = (new_asteroids[i].pos.0 + asteroids[*station].0,
//                               new_asteroids[i].pos.1 + asteroids[*station].1);
//                    return pos.0*100+pos.1
//                }
//                prev = new_asteroids[i].ang;
//            }
//            new_asteroids = left_over.clone();
//        }
//        0
    }
}

//def show_map(asteroids, vaporized, station):
//    v = [v[0] for v in vaporized]
//    a = [a[0] for a in asteroids]
//    xs = [x[0] for x in a]
//    ys = [x[1] for x in a]
//    xmin, xmax = min(xs), max(xs)
//    ymin, ymax = min(ys), max(ys)
//    for y in range(ymin, ymax+1):
//        for x in range(xmin, xmax+1):
//            p = np.array([x, y])
//            if np.all(p == np.array([0,0])):
//                print ("S", end='')
//            elif arreq_in_list(p, v):
//                print ("0", end='')
//            elif arreq_in_list(p, a):
//                print ("#", end='')
//            else:
//                print (" ", end='')
//        print ()

