use std::collections::VecDeque;
use std::collections::HashMap;
use priority_queue::PriorityQueue;

const DIRECTIONS: [(i32, i32); 4] = [(1, 0), (0, 1), (-1, 0), (0, -1)];

#[derive(Copy, Clone, Hash, Eq, Debug)]
pub struct Node {
    pub coord: Coord,
    pub prev: Coord,
}

impl Node {
    pub fn new(c: Coord, p: Coord) -> Self {
        Node { coord: c, prev: p }
    }
}

impl PartialEq for Node {
     fn eq(&self, other: &Self) -> bool {
        (self.coord == other.coord) && (self.prev == other.prev)
     }
}

#[derive(Copy, Clone, Hash, Eq, Debug)]
pub struct Coord {
    pub x: i32,
    pub y: i32,
    pub dist: i32,
}

impl Coord {
    pub fn new(x: i32, y: i32, dist: i32) -> Self {
        Coord {x: x, y: y, dist: dist}
    }
}

impl Default for Coord {
    fn default() -> Self {
        Coord { x: 0, y: 0, dist: -i32::MAX as i32 }
    }
}

impl PartialEq for Coord {
     fn eq(&self, other: &Self) -> bool {
        (self.x == other.x) && (self.y == other.y)
     }
}

pub fn backtrack(visited: &Vec<Node>, start: &Coord, target: &Coord) -> Vec<Coord> {
    
    let mut path: Vec<Coord> = Vec::new();

    path.push(*target);
    let mut pos = target;
    while pos != start {
        pos = &visited.iter()
            .filter(|x| x.coord == *pos).collect::<Vec<_>>()[0].prev;
        path.push(*pos)
    }

    path.reverse();
    path
}

pub fn min_distance(distances: &HashMap<Coord, i32>, target: &Coord) -> i32 {
    match distances.get(target) {
        Some(x) => *x,
        None => -i32::MAX,
    }   
}

pub fn bfs(arr: &Vec<Coord>, start: &Coord, target: &Coord) -> Result<(Vec::<Coord>, i32), &'static str> {
    let mut visited: Vec<Node> = Vec::new();

    let mut queue: VecDeque<Node> = VecDeque::new();
    let n = Node::new(*start, *start);
    queue.push_back(n);

    while let Some(pos) = queue.pop_front() {
        visited.push(pos);

        if pos.coord == *target {
            let path = backtrack(&visited, &start, &target);
            let d = path.len() as i32;
            return Ok((path, d));
        }

        for (dx, dy) in DIRECTIONS {
            let new_coord = Coord::new(pos.coord.x + dx, pos.coord.y + dy, 1);
            let new_pos = Node::new(new_coord, pos.coord);
            if arr.contains(&new_coord) &&
                visited.iter()
                .filter(|x| x.coord == new_coord).collect::<Vec<_>>().len() == 0 {
                    queue.push_back(new_pos);
                }
        }
    }
    Err("path not found!")
}

pub fn dijkstra(arr: &Vec<Coord>, start: &Coord, target: &Coord, endwithtarget: bool) -> Result<(Vec::<Coord>, i32), &'static str> {
    let mut visited = Vec::<Node>::new();
    let mut distances: HashMap<Coord, i32> = HashMap::new();    
    let mut pq = PriorityQueue::new();

    for i in arr {
        distances.insert(*i, i32::MAX);
    }
    distances.insert(*start, 1);
    let n = Node::new(*start, *start);
    pq.push(n, 0);
    while let Some((pos, _)) = pq.pop() {
        visited.push(pos);
        if endwithtarget && pos.coord == *target {
            return Ok((backtrack(&visited, &start, &target),
                       min_distance(&distances, target)));
        }
        let old_cost =  *distances.get(&pos.coord).unwrap();
        for (dx, dy) in DIRECTIONS {
            let new_coord = Coord {x: pos.coord.x + dx, y: pos.coord.y + dy, ..Default::default()};
            let new_pos = match arr.iter().find(|x| **x == new_coord) {
                Some (x) => *x,
                None => continue,
            };
            if new_pos.dist >= 0 {
                let distance = new_pos.dist;
                let mut new_node = Node::new(new_pos, pos.coord);
                if visited.iter()
                    .filter(|x| x.coord == new_pos).collect::<Vec<_>>().len() == 0 {
                        let new_cost = old_cost + distance;
                        if new_cost <= *distances.get(&new_pos).unwrap() {                            
                            new_node.prev = pos.coord;
                            pq.push(new_node, -new_cost);
                            distances.insert(new_pos, new_cost);
                        }
                    }
            }
        }
    }
    if endwithtarget {
        Err("path not found!")
    } else {
        Ok((backtrack(&visited, &start, &target),
            min_distance(&distances, target)))
    }
}
