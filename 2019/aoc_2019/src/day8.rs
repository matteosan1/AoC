pub mod day8 {
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    pub fn solve() {
        let lines = utils::read_input("../input_8.txt");
        //println!("{:?}", lines.len());
        //let nlayers = lines[0].len()/(25*6);
        
        let mut image = Vec::<u32>::new();
        for c in lines[0].chars() {
            image.push(c.to_digit(10).unwrap());
        }
        
        let now = Instant::now();
        
        let res1 = part1(&image);
        let elapsed = now.elapsed();                
        println!("{} {} ({:.2?})", utils::santa(8, 1), res1, elapsed);
        
        part2(&image);
        let elapsed = now.elapsed();
        println!("{} ({:.2?})", utils::christmas_tree(8, 2), elapsed);        
    }

    fn part1(image: &Vec::<u32>) -> usize {
        let s = 25*6;
        let mut min_layer = (0, s);
        let nlayers = image.len()/s;
        for i in 0..nlayers {
            let c = image[i*s..(i+1)*s].iter().filter(|&n| *n == 0).count();
            if c < min_layer.1 {
                min_layer = (i, c);
            }
        }
        let i = min_layer.0;
        image[i*s..(i+1)*s].iter().filter(|&n| *n == 1).count() * image[i*s..(i+1)*s].iter().filter(|&n| *n == 2).count()
    }


    fn show_image(image: &Vec::<u32>) {
        for y in 0..6 {
            for x in 0..25 {
                if image[y*25 + x] == 1 {
                    print!("▮");
                } else if image[y*25 + x] == 0 {
                    print!(" ");
                }
            }
            println!("");
        }
    }
    
    fn part2(image: &Vec::<u32>) {
        let s = 25*6;
        let nlayers = image.len()/s;
        let mut rendering = vec![0u32; s];
        for i in 0..s {
            for n in 0..nlayers {
                if image[n*s+i] != 2 {
                    rendering[i] = image[n*s+i];
                    break;
                }
            }
        }
        show_image(&rendering);
    }
}
