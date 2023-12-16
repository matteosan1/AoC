pub mod day16 {
    extern crate aoc;
    use aoc::utils;

    #[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord)]
    enum Tile {
        MirrorUR,
        MirrorUL,
        SplitterVert,
        SplitterHoriz,
        Space
    }

    #[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord)]
    enum BeamDir {
        Right = 0b0001,
        Down = 0b0010,
        Left = 0b0100,
        Up = 0b1000
    }

    fn preprocess(lines: &Vec<String>) -> Vec<Vec<(Tile, u8)>> {
        lines.iter().map(|line| {
            line.chars().map(|c| (match c {
                '\\' => Tile::MirrorUR,
                '/' => Tile::MirrorUL,
                '|' => Tile::SplitterVert,
                '-' => Tile::SplitterHoriz,
                '.' => Tile::Space,
                _ => panic!(),
            }, 0 )).collect()
        }).collect()
    }

    fn energized_count(map: &mut Vec<Vec<(Tile, u8)>>, start: (BeamDir, usize, usize)) -> u16 {
        let mut beams = vec![start];
        let mut new_directions = Vec::with_capacity(2);
        let mut energized = 0;

        while let Some((direction, x, y)) = beams.pop() {
            let (tile, directions) = &mut map[y][x];

            if *directions & direction as u8 != 0 {
                continue;
            }

            if *directions == 0 {
                energized += 1;
            }

            *directions |= direction as u8;

            match *tile {
                Tile::MirrorUR => new_directions.push(match direction {
                    BeamDir::Right => BeamDir::Down,
                    BeamDir::Down => BeamDir::Right,
                    BeamDir::Left => BeamDir::Up,
                    BeamDir::Up => BeamDir::Left,
                }),

                Tile::MirrorUL => new_directions.push(match direction {
                    BeamDir::Right => BeamDir::Up,
                    BeamDir::Down => BeamDir::Left,
                    BeamDir::Left => BeamDir::Down,
                    BeamDir::Up => BeamDir::Right,
                }),

                Tile::SplitterVert => if direction as u8 & 0b1010 != 0 {
                    new_directions.push(direction);
                } else {
                    new_directions.extend(&[BeamDir::Up, BeamDir::Down]);
                }

                Tile::SplitterHoriz => if direction as u8 & 0b0101 != 0 {
                    new_directions.push(direction);
                } else {
                    new_directions.extend(&[BeamDir::Left, BeamDir::Right]);
                }

                Tile::Space => { new_directions.push(direction); }
            }

            for &new_direction in &new_directions {
                let (new_x, new_y) = match new_direction {
                    BeamDir::Right => (x+1, y),
                    BeamDir::Down => (x, y+1),
                    BeamDir::Left => (x.wrapping_sub(1), y),
                    BeamDir::Up => (x, y.wrapping_sub(1)),
                };

                if new_y >= map.len() || new_x >= map[new_y].len() {
                    continue;
                }

                beams.push((new_direction, new_x, new_y));
            }

            new_directions.clear();
        }

        energized
    }
                    
    pub fn part1(lines: &Vec<String>) {
        let mut map = preprocess(lines);
        println!("{} {}", utils::santa(16, 1), energized_count(&mut map, (BeamDir::Right, 0, 0)));
    }
        
    pub fn part2(lines: &Vec<String>) {
        let mut map = preprocess(lines);
        let height = map.len();
        let width = map[0].len();
        let energy = (0..height).flat_map(|y| {
            [(BeamDir::Right, 0, y), (BeamDir::Left, width-1, y)].into_iter()
        }).chain((0..width).flat_map(|x| {
            [(BeamDir::Down, x, 0), (BeamDir::Up, x, height-1)].into_iter()
        })).map(|start| {
            for line in &mut map {
                for (_, directions) in line {
                    *directions = 0;
                }
            }
            
            energized_count(&mut map, start)
        }).max().unwrap();

        println!("{} {}", utils::christmas_tree(16, 2), energy);
    }
}
