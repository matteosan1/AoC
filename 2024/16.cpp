#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <limits>
#include <chrono>

using namespace std;
using namespace std::chrono;

struct Point {
    int x, y;
    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
    bool operator<(const Point& other) const {
        if (y != other.y) return y < other.y;
        return x < other.x;
    }
};

struct State {
    Point p;
    int dir;
    int cost;

    bool operator>(const State& other) const {
        return cost > other.cost;
    }
};

struct State2 {
    Point p;
    Point dir;
    int score;
    set<Point> tiles;
};

const vector<Point> DIRECTIONS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

map<Point, int> loadInput(const string& filename, Point& start, Point& target) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        exit(1);
    }

    map<Point, int> pitch;
    vector<string> lines;
    string line;
    while (getline(file, line)) {
        lines.push_back(line);
    }

    for (int y = 0; y < lines.size(); ++y) {
        for (int x = 0; x < lines[0].size(); ++x) {
            Point c = {x, y};
            if (lines[y][x] == '#') {
                pitch[c] = 1;
            } else if (lines[y][x] == 'S') {
                pitch[c] = 0;
                start = c;
            } else if (lines[y][x] == 'E') {
                target = c;
                pitch[c] = 0;
            } else if (lines[y][x] == '.') {
                pitch[c] = 0;
            }
        }
    }
    return pitch;
}

bool isValid(const map<Point, int>& grid, const Point& c) {
    return grid.count(c) > 0 && grid.at(c) != 1;
}

vector<pair<State, int>> getNeighbors(const map<Point, int>& grid, const Point& c, int direction) {
    vector<pair<State, int>> neighbors;
    for (int idc = 0; idc < DIRECTIONS.size(); ++idc) {
        Point dc = DIRECTIONS[idc];
        if (dc.x == -DIRECTIONS[direction].x && dc.y == -DIRECTIONS[direction].y) {
            continue;
        }
        Point nc = {c.x + dc.x, c.y + dc.y};
        if (isValid(grid, nc)) {
            int moveCost = (dc.x == DIRECTIONS[direction].x && dc.y == DIRECTIONS[direction].y) ? 1 : 1001;
            neighbors.push_back({{nc, idc, 0}, moveCost});
        }
    }
    return neighbors;
}

pair<int, vector<pair<Point, int>>> part1(const map<Point, int>& grid, const Point& start, const Point& target) {
    priority_queue<State, vector<State>, greater<State>> q;
    q.push({start, 1, 0});
    set<pair<Point, int>> visited;
    map<pair<Point, int>, pair<Point, int>> predecessors;

    while (!q.empty()) {
        State current_state = q.top();
        q.pop();
        Point c = current_state.p;
        int direction = current_state.dir;
        int cost = current_state.cost;

        if (visited.count({c, direction})) continue;
        visited.insert({c, direction});

        if (c == target) {
            vector<pair<Point, int>> path;
            pair<Point, int> current = {c, direction};
            while (predecessors.count(current)) {
                path.push_back(current);
                current = predecessors.at(current);
            }
            cout << "🎄 Part 1: " << cost;
            return {cost, vector<pair<Point,int>>(path.rbegin(), path.rend())};
        }

        for (auto& neighbor_data : getNeighbors(grid, c, direction)) {
            Point nc = neighbor_data.first.p;
            int nd = neighbor_data.first.dir;
            int move_cost = neighbor_data.second;

            if (!visited.count({nc, nd})) {
                int new_cost = cost + move_cost;
                q.push({nc, nd, new_cost});
                predecessors[{nc, nd}] = {c, direction};
            }
        }
    }
    return {-1, {}};
}

void part2(const map<Point, int>& pitch, const Point& start, const Point& target) {
    map<Point, map<Point, map<string, set<Point>>>> seen_states;
    for (const auto& [pos, val] : pitch) {
        for (Point dir : DIRECTIONS) {
            seen_states[pos][dir]["score"] = {};
            seen_states[pos][dir]["tiles"] = {};
        }
    }

    priority_queue<State2, vector<State2>, function<bool(const State2&, const State2&)>> q([](const State2& a, const State2& b) {
        return a.score > b.score;
    });

    q.push({start, {1, 0}, 0, {}});

    while (!q.empty()) {
        State2 current = q.top();
        q.pop();
        Point coord = current.p;
        Point direction = current.dir;
        set<Point> tiles = current.tiles;
        int score = current.score;

        set<Point> allowed = {{0,1}, {1,0}, {0,-1}, {-1,0}};
        for(Point p : DIRECTIONS){
            if(p.x == -direction.x && p.y == -direction.y){
                allowed.erase(p);
                break;
            }
        }

        for (Point dc : allowed) {
            Point new_coord = {coord.x + dc.x, coord.y + dc.y};
            if (!isValid(pitch, new_coord)) {
                continue;
            }
            int new_score = score + 1 + (dc.x != direction.x || dc.y != direction.y ? 1000 : 0);

            if (seen_states.count(new_coord) && seen_states[new_coord].count(dc)) {
                if (!seen_states[new_coord][dc]["score"].empty() && new_score > *seen_states[new_coord][dc]["score"].begin()) {
                    continue;
                }
            } else {
                seen_states[new_coord][dc]["score"].insert(numeric_limits<int>::max());
            }


            set<Point> new_tiles = tiles;
            new_tiles.insert(new_coord);

             seen_states[new_coord][dc]["score"].clear();
            seen_states[new_coord][dc]["score"].insert(new_score);
            seen_states[new_coord][dc]["tiles"] = new_tiles;

            q.push({new_coord, dc, new_score, new_tiles});
        }
    }

    int min_score = numeric_limits<int>::max();
    set<Point> min_tiles;
    for (const auto& [dir, data] : seen_states[target]) {
        if (!data["score"].empty() && *data["score"].begin() < min_score) {
            min_score = *data["score"].begin();
            min_tiles = data["tiles"];
        }
    }
    cout << "🎄🎅 Part 2: " << min_tiles.size() + 1 << endl;
}

void draw(const map<Point, int>& pitch, const set<Point>& sits) {
    int xmax = 0, ymax = 0;
    for (const auto& [c, v] : pitch) {
        xmax = max(xmax, c.x);
        ymax = max(ymax, c.y);
    }
    xmax++; ymax++;

    for (int y = 0; y < ymax; ++y) {
        for (int x = 0; x < xmax; ++x) {
            Point c = {x, y};
            if (sits.count(c)) {
                cout << "O";
            } else if (pitch.count(c) && pitch.at(c) == 1) {
                cout << "#";
            } else {
                cout << ".";
            }
        }
        cout << endl;
    }
}

int main() {
    string title = "Day 16: Reindeer Maze";
    string sub = string(title.length() + 2, '-');

    cout << endl;
    cout << " " << title << " " << endl;
    cout << sub << endl;

    Point start, target;
    map<Point, int> grid = loadInput("input_16.txt", start, target);

    auto t0 = std::chrono::high_resolution_clock::now();
    part1(grid, start, target);
    auto t1 = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0);
    std::cout << " - " << duration.count() << "\u00B5s" << std::endl; 

    auto t0 = std::chrono::high_resolution_clock::now();
    part2(grid, start, target);
    auto t1 = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0);
    std::cout << " - " << duration.count() << "\u00B5s" << std::endl; 

//   start = std::chrono::high_resolution_clock::now();
//   part2(memory);
//   end = std::chrono::high_resolution_clock::now();
//   duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
//   std::cout << " - " << duration.count() << "\u00B5s" << std::endl; 

    return 0;
}

// void part2(const map<Point, int>& pitch, const Point& start, const Point& target) {
//     map<Point, map<Point, map<string, set<Point>>>> seen_states;
//     for (const auto& [pos, val] : pitch) {
//         seen_states[pos][{0,0}]["score"] = set<Point>();
//         seen_states[pos][{0,0}]["tiles"] = set<Point>();

//         for(Point dir : DIRECTIONS){
//             seen_states[pos][dir]["score"] = set<Point>();
//             seen_states[pos][dir]["tiles"] = set<Point>();
//         }
//     }

//     priority_queue<State2, vector<State2>, function<bool(const State2&, const State2&)>> q([](const State2& a, const State2& b) {
//         return a.score > b.score;
//     });


//     q.push({start, {1, 0}, 0, {}});

//     while (!q.empty()) {
//         State2 current = q.top();
//         q.pop();
//         Point coord = current.p;
//         Point direction = current.dir;
//         set<Point> tiles = current.tiles;
//         int score = current.score;

//         set<Point> allowed = {{0,1}, {1,0}, {0,-1}, {-1,0}};
//         for(Point p : allowed){
//             if(p.x == -direction.x && p.y == -direction.y){
//                 allowed.erase(p);
//                 break;
//             }
//         }

//         for (Point dc : allowed) {
//             Point new_coord = {coord.x + dc.x, coord.y + dc.y};
//             if (!isValid(pitch, new_coord)) {
//                 continue;
//             }
//             int new_score = score + 1 + (dc.x != direction.x || dc.y != direction.y ? 1000 : 0);

//             if(seen_states.count(new_coord) == 0 || seen_states[new_coord].co#include <chrono>

// void part1(string& memory) {
//   const regex pattern("mul\\((\\d{1,3}),(\\d{1,3})\\)");//|do\\(\\)|don't\\(\\)");
//   int tot = 0;
//   sregex_iterator iter(memory.begin(), memory.end(), pattern);
//   sregex_iterator end_iter;
  
//   while (iter != end_iter) {
//     smatch match = *iter;
    
//     tot += stoi(match[1])*stoi(match[2]);
//     ++iter;
//   }

//   std::cout << "🎄   Part 1: " << tot;
// }

// void part2(string& memory) {

//   const regex pattern("mul\\((\\d{1,3}),(\\d{1,3})\\)|do\\(\\)|don't\\(\\)");
//   int tot = 0;
//   bool enabled = true;
//   sregex_iterator iter(memory.begin(), memory.end(), pattern);
//   sregex_iterator end_iter;
  
//   while (iter != end_iter) {
//     smatch match = *iter;
//     if (match.str() == "do()")
//       enabled = true;
//     else if (match.str() == "don't()")
//       enabled = false;
//     else {
//       if (enabled)
// 	tot += stoi(match[1])*stoi(match[2]);
//     }
//     ++iter;
//   }

//   std::cout << "🎄🎅 Part 2: " << tot;
// }

// int main() {
//   ifstream file("input_3.txt");
  
//   if (!file.is_open()) {
//     cerr << "Error opening file!" << endl;
//     return 1;
//   }
  
//   string memory;
//   string line;
//   while (getline(file, line)) {
//     memory += line;  
//   }

//   file.close();

//   std::cout << "Day 3: Mull It Over" << std::endl;


//   return 0;
// }
