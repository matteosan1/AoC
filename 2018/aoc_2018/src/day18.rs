pub mod day18 {
    use std::time::Instant;
    
    extern crate aoc;
    use aoc::utils;

    fn preprocess() -> [[u8; 102]; 102] {
        let lines = utils::read_input("../instructions18a.txt");
        let mut grid = [[0u8; 102]; 102];
        for (y, l) in lines.iter().enumerate() {
            for (x, c) in l.chars().enumerate() {
                if c == '#' {
                    grid[x+1][y+1] = 1;
                } else if c == '.' {
                    grid[x+1][y+1] = 0;
                }
            }
        }
        grid
    }

    pub fn solve () {
        let grid = preprocess();
        
        let now = Instant::now();
        let res1 = part1(grid);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::santa(18, 1), res1, elapsed);
        
        let res2 = part2(grid);
        let elapsed = now.elapsed();
        println!("{} {} ({:.2?})", utils::christmas_tree(18, 2), res2, elapsed);
    }

    fn switch(x: usize, y: usize, grid: &[[u8; 102]; 102]) -> u8 {
        let mut val = 0;
        for xp in [x-1, x, x+1] {
            for yp in [y-1, y, y+1] {
                if xp == x && yp == y {
                    continue;
                }
                if grid[xp][yp] == 1 {
                    val += 1;
                }
            }
        }
        
        if grid[x][y] == 1 {
            if val == 2 || val == 3 {
                return 1;
            } else {
                return 0;
            }
        } else {
            if val == 3 {
                return 1;
            } else {
                return 0;
            }
        }
    }

    fn sumall(grid: &[[u8; 102]; 102]) -> i32 {
        let mut val = 0;
        for x in 1..101 {
            for y in 1..101 {
                val += grid[x][y] as i32;
            }
        }
        val
    }
    
    fn part1(mut grid: [[u8; 102];102]) -> i32 {
        let mut new_grid = [[0u8; 102];102];

        for _ in 0..100 {
            for x in 1..101 {
                for y in 1..101 {
                    new_grid[x][y] = switch(x, y, &grid);
                }
            }
            grid = new_grid.clone();
        }
        sumall(&grid)            
    }
    
    fn part2(mut grid: [[u8; 102];102]) -> i32 {
        let mut new_grid = [[0u8; 102];102];
        grid[1][100] = 1;
        grid[1][1] = 1;
        grid[100][1] = 1;
        grid[100][100] = 1;        

        for _ in 0..100 {
            for x in 1..101 {
                for y in 1..101 {
                    if x == 1 && (y == 1 || y == 100) ||
                        x == 100 && (y == 1 || y == 100) {
                        new_grid[x][y] = 1;
                    } else {
                        new_grid[x][y] = switch(x, y, &grid);
                    }
                }
            }
            grid = new_grid.clone();
        }
        sumall(&grid)            
    }    
}
    


