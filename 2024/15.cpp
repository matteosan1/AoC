#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <complex>
#include <chrono>
#include <set>
#include <algorithm>

using namespace std;
using namespace std::chrono;

using Complex = complex<int>;

map<char, Complex> dirs = {
    {'^', {0, -1}},
    {'>', {1, 0}},
    {'<', {-1, 0}},
    {'v', {0, 1}}
};

pair<map<Complex, int>, string> loadInput(int part = 1) {
    ifstream file("input_15.txt");
    if (!file.is_open()) {
        cerr << "Error opening file" << endl;
        exit(1);
    }

    map<Complex, int> grid;
    string instructions = "";
    Complex start;
    string line;
    int y = 0;

    while (getline(file, line)) {
        if (line[0] != '#') {
            instructions += line;
        } else {
            int ix = 0;
            for (int x = 0; x < line.length(); ++x) {
                Complex c;
                if (part == 2) {
                    c = {ix, y};
                } else {
                    c = {x, y};
                }
                
                if (line[x] == '#') {
                    grid[c] = 1;
                    if(part == 2) grid[{ix+1, y}] = 1;
                } else if (line[x] == '.') {
                    grid[c] = 0;
                    if(part == 2) grid[{ix+1, y}] = 0;
                } else if (line[x] == '@') {
                    start = c;
                    grid[c] = 0;
                    if(part == 2) grid[{ix+1, y}] = 0;
                } else if (line[x] == 'O') {
                    grid[c] = 3;
                    if(part == 2) grid[{ix+1, y}] = 4;
                }
                if(part == 2) ix += 2;
            }
        }
        y++;
    }
    return {grid, instructions};
}

Complex move(Complex pos, map<Complex, int>& grid, Complex dir) {
    Complex new_pos = pos + dir;
    if (grid.count(new_pos) && grid[new_pos] == 3) {
        move(new_pos, grid, dir);
    }
    if (grid.count(new_pos) && grid[new_pos] == 0) {
        grid[new_pos] = grid[pos];
        grid[pos] = 0;
        return new_pos;
    }
    return pos;
}

int GPS(const map<Complex, int>& grid) {
    int gps = 0;
    for (const auto& [g, val] : grid) {
        if (val == 3) {
            gps += g.real() + g.imag() * 100;
        }
    }
    return gps;
}

void part1(map<Complex, int> grid, const string& instructions, Complex start) {
    for (char i : instructions) {
        start = move(start, grid, dirs[i]);
    }
    int score = GPS(grid);
    cout << "🎄 Part 1: " << score << endl;
}

Complex move2(vector<Complex> pos, map<Complex, int>& grid, Complex dir) {
    vector<Complex> new_pos;
    for (Complex p : pos) new_pos.push_back(p + dir);
    
    if (dir.real() == -1 || dir.real() == 1) {
        if (grid.count(new_pos[0]) && (grid[new_pos[0]] == 3 || grid[new_pos[0]] == 4)) {
            move2(new_pos, grid, dir);
        }
    } else {
        vector<Complex> new_new_pos;
        for (size_t i = 0; i < new_pos.size(); ++i) {
            if (grid.count(new_pos[i])) {
                if (grid[new_pos[i]] == 3) {
                    new_new_pos.push_back(new_pos[i]);
                    new_new_pos.push_back(new_pos[i] + 1);
                } else if (grid[new_pos[i]] == 4) {
                    new_new_pos.push_back(new_pos[i]);
                    new_new_pos.push_back(new_pos[i] - 1);
                }
            } else {
                new_new_pos.clear();
                break;
            }
        }
        if (!new_new_pos.empty()) {
            set<Complex> s(new_new_pos.begin(), new_new_pos.end());
            new_new_pos.assign(s.begin(), s.end());
            move2(new_new_pos, grid, dir);
        }
    }

    if (all_of(new_pos.begin(), new_pos.end(), [&](Complex np){ return grid.count(np) && grid[np] == 0;})) {
        for (size_t i = 0; i < new_pos.size(); ++i) {
            grid[new_pos[i]] = grid[pos[i]];
            grid[pos[i]] = 0;
        }
    }
    if (grid.count(new_pos[0]) && grid[new_pos[0]] == 0) {
        return new_pos[0];
    } else {
        return pos[0];
    }
}

void part2(map<Complex, int> grid, const string& instructions, Complex start) {
    for (char i : instructions) {
        start = move2({start}, grid, dirs[i]);
    }
    int score = GPS(grid);
    cout << "🎄🎅 Part 2: " << score << endl;
}

void draw(const map<Complex, int>& grid, Complex start, int part = 1) {
    int xmax = 0, ymax = 0;
    for (const auto& [c, v] : grid) {
        xmax = max(xmax, (int)c.real());
        ymax = max(ymax, (int)c.imag());
    }
    xmax++; ymax++;

    for (int y = 0; y < ymax; ++y) {
        for (int x = 0; x < xmax; ++x) {
            Complex g(x, y);
            if (g == start) {
                cout << "@";
            } else if (grid.count(g) && grid.at(g) == 0) {
                cout << ".";
            } else if (grid.count(g) && grid.at(g) == 1) {
                cout << "#";
            } else if (grid.count(g) && grid.at(g) == 3) {
                cout << (part == 1 ? 'O' : '[');
            } else if (grid.count(g) && grid.at(g) == 4) {
                cout << "]";
            }
        }
        cout << endl;
    }
}

int main() {
    string title = "Day 15: Warehouse Woes";
    string sub = string(title.length() + 2, '-');

    cout << endl;
    cout << " " << title << " " << endl;
    cout << sub << endl;

    auto [grid1, instructions1] = loadInput();
    Complex start1;
    for(auto const& [key, val] : grid1){
        if(val == 0){
            start1 = key;
            break;
        }
    }

    auto t1_start = high_resolution_clock::now();
    part1(grid1, instructions1, start1);
    auto t1_end = high_resolution_clock::now();
    auto duration1 = duration_cast<milliseconds>(t1_end - t1_start);
    cout << duration1.count() << " ms" << endl;
}