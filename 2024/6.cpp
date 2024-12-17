#include <iostream>
#include <fstream>
#include <string>
#include <complex>
#include <set>
#include <vector>
#include <unordered_set>
#include <chrono>
#include <iomanip>

using namespace std;
using namespace std::chrono;

typedef complex<int> Point;

struct Color {
    static const string RED;
    static const string BOLD;
    static const string END;
};

const string Color::RED = "\033[31m";
const string Color::BOLD = "\033[1m";
const string Color::END = "\033[0m";

unordered_map<Point, int> loadInput(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        exit(1);
    }

    unordered_map<Point, int> area;
    Point start;
    string line;
    int y = 0;
    while (getline(file, line)) {
        for (int x = 0; x < line.length(); ++x) {
            switch (line[x]) {
                case '.':
                    area[Point(x, y)] = 0;
                    break;
                case '^':
                    area[Point(x, y)] = 0;
                    start = Point(x, y);
                    break;
                case '#':
                    area[Point(x, y)] = 1;
                    break;
            }
        }
        y++;
    }
    return area;
}

const vector<Point> movements = {Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)};

set<Point> part1(const unordered_map<Point, int>& area, const Point& start) {
    int face = 0;
    Point pos = start;
    set<Point> distincts = {pos};
    while (true) {
        Point new_pos = pos + movements[face];
        if (area.count(new_pos) && area.at(new_pos) == 0) {
            pos = new_pos;
            distincts.insert(pos);
        } else {
            face = (face + 1) % movements.size();
        }
    }
    cout << " Part 1: " << distincts.size() << endl;
    return distincts;
}

vector<Point> part2(const unordered_map<Point, int>& area, const Point& start, const set<Point>& path) {
    vector<Point> blocks;
    vector<Point> path_copy(path.begin(), path.end());
    path_copy.erase(remove(path_copy.begin(), path_copy.end(), start), path_copy.end());
    for (const Point& p : path_copy) {
        if (find(blocks.begin(), blocks.end(), p) != blocks.end()) {
            continue;
        }
        area.at(p) = 1;
        int face = 0;
        Point pos = start;
        unordered_set<pair<Point, int>> turns;
        bool is_loop = false;
        while (true) {
            Point new_pos = pos + movements[face];
            if (area.count(new_pos) && area.at(new_pos) == 1) {
                face = (face + 1) % movements.size();
                if (turns.count({pos, face})) {
                    is_loop = true;
                    break;
                }
                turns.insert({pos, face});
            } else {
                pos = new_pos;
            }
        }
        if (is_loop) {
            blocks.push_back(p);
            area.at(p) = 0;
        }
    }

    cout << " Part 2: " << blocks.size() << endl;
    return blocks;
}

int main() {
    string title = "Day 6: Guard Gallivant";
    string sub = string(title.length() / 2 + 2, '⛄');

    cout << endl;
    cout << " " << title << "