pub mod day14 {
    extern crate aoc;
    use aoc::utils;

    type Map = Vec<Vec<char>>;

    fn tilt_north(map: Map) -> Map {
        let mut empty_above: Vec<usize> = vec![0; map[0].len()];
        let mut new_map = map.clone();

        for (vertical_pos, line) in map.iter().enumerate() {
            for (horizontal_pos, rock) in line.iter().enumerate() {
                match rock {
                    '.' => {
                        empty_above[horizontal_pos] += 1;
                    }
                    '#' => {
                        empty_above[horizontal_pos] = 0;
                    }
                    'O' => {
                        let new_rock_pos = vertical_pos - empty_above[horizontal_pos];
                        new_map[vertical_pos][horizontal_pos] = '.';
                        new_map[new_rock_pos][horizontal_pos] = 'O';
                    }
                    _ => panic!("Invalid rock type {}", rock),
                }
            }
        }

        new_map
    }

    fn tilt_east(map: Map) -> Map {
        let mut empty_right: Vec<usize> = vec![0; map.len()];
        let mut new_map = map.clone();
        
        for horizontal_pos in (0..map[0].len()).rev() {
            for vertical_pos in 0..map.len() {
                let rock = map[vertical_pos][horizontal_pos];
                match rock {
                    '.' => {
                        empty_right[vertical_pos] += 1;
                    }
                    '#' => {
                        empty_right[vertical_pos] = 0;
                    }
                    'O' => {
                        let new_rock_pos = horizontal_pos + empty_right[vertical_pos];
                        new_map[vertical_pos][horizontal_pos] = '.';
                        new_map[vertical_pos][new_rock_pos] = 'O';
                    }
                    _ => panic!("Invalid rock type {}", rock),
                }
            }
        }
        
        new_map
    }
    
    fn tilt_south(map: Map) -> Map {
        let mut empty_below: Vec<usize> = vec![0; map[0].len()];
        let mut new_map = map.clone();
        let map_height = map.len();
        
        for (vertical_pos, line) in map.iter().rev().enumerate() {
            for (horizontal_pos, rock) in line.iter().enumerate() {
                match rock {
                    '.' => {
                        empty_below[horizontal_pos] += 1;
                    }
                    '#' => {
                        empty_below[horizontal_pos] = 0;
                    }
                    'O' => {
                        let new_rock_pos = vertical_pos - empty_below[horizontal_pos];
                        new_map[map_height - 1 - vertical_pos][horizontal_pos] = '.';
                        new_map[map_height - 1 - new_rock_pos][horizontal_pos] = 'O';
                    }
                    _ => panic!("Invalid rock type {}", rock),
                }
            }
        }
        
        new_map
    }
    
    fn tilt_west(map: Map) -> Map {
        let mut empty_left: Vec<usize> = vec![0; map.len()];
        let mut new_map = map.clone();
        
        for horizontal_pos in 0..map[0].len() {
            for vertical_pos in 0..map.len() {
                let rock = map[vertical_pos][horizontal_pos];
                match rock {
                    '.' => {
                        empty_left[vertical_pos] += 1;
                    }
                    '#' => {
                        empty_left[vertical_pos] = 0;
                    }
                    'O' => {
                        let new_rock_pos = horizontal_pos - empty_left[vertical_pos];
                        new_map[vertical_pos][horizontal_pos] = '.';
                        new_map[vertical_pos][new_rock_pos] = 'O';
                    }
                    _ => panic!("Invalid rock type {}", rock),
                }
            }
        }
        
        new_map
    }
    
    fn cycle(map: Map) -> Map {
        let map = tilt_north(map);
        let map = tilt_west(map);
        let map = tilt_south(map);
        tilt_east(map)
    }
    
    fn get_load_on_support(map: &Map) -> usize {
        let mut total_load = 0;
        for (vertical_pos, line) in map.iter().enumerate() {
            for (_, c) in line.iter().enumerate() {
                if *c == 'O' {
                    total_load += map.len() - vertical_pos;
                }
            }
        }

        total_load
    }
    
    pub fn part1(lines: &Vec<String>) {
        let mut map: Map = lines.iter().map(|line| line.chars().collect()).collect();
        let mut empty_above: Vec<usize> = vec![0; lines[0].len()];

        let mut total_load = 0;
        for (vertical_pos, line) in map.iter().enumerate() {
            for (horizontal_pos, c) in line.iter().enumerate() {
                match *c {
                    '.' => {
                        empty_above[horizontal_pos] += 1;
                    }
                    '#' => {
                        empty_above[horizontal_pos] = 0;
                    }
                    'O' => {
                        let new_rock_pos = vertical_pos - empty_above[horizontal_pos];
                        total_load += lines.len() - new_rock_pos;
                    }
                    _ => panic!("Invalid rock type {}", *c),
                }
            }
        }
        
        println!("{} {}", utils::santa(14, 1), total_load.to_string());
    }

    pub fn part2(lines: &Vec<String>) {
        let mut map: Map = lines.iter().map(|line| line.chars().collect()).collect();
        let mut seen_states: Vec<Map> = vec![map.clone()];

        loop {
            map = cycle(map.clone());
            if let Some(index) = seen_states.iter().position(|x| x == &map) {
                let cycle_length = seen_states.len() - index;
                let cycle_start = index;
                let final_map =
                    seen_states[cycle_start + (1000000000 - cycle_start) % cycle_length].clone();
                println!("{} {}", utils::christmas_tree(14, 2), get_load_on_support(&final_map).to_string());
                break;
            }
            seen_states.push(map.clone());
        }
    }
}



//def loadInput():
//    lines = readInput("input_14.txt")
//    platform = []
//    for y, l in enumerate(lines):
//        temp = []
//        for x, c in enumerate(l):
//            if c == ".":
//                temp.append(0)
//            elif c == "#":
//                temp.append(2)
//            elif c == "O":
//                temp.append(1)
//        platform.append(temp)
//    platform = np.array(platform)
//    return platform
//
//def find_north_space(rock, column):
//    i = rock-1
//    for i in range(rock-1, -1, -1):
//        if column[i] != 0:
//            return i+1
//    return 0
//
//def count_load(platform):
//    tot = 0
//    for x in range(platform.shape[1]):
//        tot += (platform.shape[0] - np.where(platform[:, x]==1)[0]).sum()
//    return tot
//    
//def part1(platform):
//    for x in range(platform.shape[1]):
//        rocks = np.where(platform[:, x] == 1)[0]
//        for r in rocks:
//            space = find_north_space(r, platform[:, x])
//            if space != r:
//                platform[r, x] = 0
//                platform[space, x] = 1
//    return count_load(platform)
//
//def arreq_in_list(myarr, list_arrays):
//    return next((True for elem in list_arrays if np.array_equal(elem, myarr)), False)
//
//def arridx_in_list(myarr, list_arrays):
//    return next((i for i, elem in enumerate(list_arrays) if np.array_equal(elem, myarr)), -1)
//
//def part2(platform):
//    cycles = 1000000000
//    platforms = []
//    for i in range(cycles):
//        for rot in range(0, 4):
//            for x in range(platform.shape[1]):
//                rocks = np.where(platform[:, x] == 1)[0]
//                for r in rocks:
//                    space = find_north_space(r, platform[:, x])
//                    if space != r:
//                        platform[r, x] = 0
//                        platform[space, x] = 1
//            platform = np.rot90(platform, -1)
//
//        if not arreq_in_list(platform, platforms):
//            platforms.append(platform.copy())
//        else:
//            break
//    offset = arridx_in_list(platform, platforms)
//    period = i - offset
//    idx = (cycles - offset)%period+offset-1
//    return count_load(platforms[idx])
