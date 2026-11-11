C++

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <complex>
#include <chrono>
#include <set>

using namespace std;
using namespace std::chrono;

using Complex = complex<int>;

map<int, Complex> dirs = {
    {0, {0, -1}}, {1, {1, 0}}, {2, {0, 1}}, {3, {-1, 0}}
};

map<int, Complex> full_dirs = {
    {0, {0, -1}}, {2, {1, 0}}, {4, {0, 1}}, {6, {-1, 0}},
    {1, {1, -1}}, {3, {1, 1}}, {5, {-1, 1}}, {7, {-1, -1}}
};

map<Complex, char> loadInput(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        exit(1);
    }

    map<Complex, char> garden;
    string line;
    int y = 0;
    while (getline(file, line)) {
        for (int x = 0; x < line.length(); ++x) {
            garden[{x, y}] = line[x];
        }
        y++;
    }
    return garden;
}

map<char, vector<vector<Complex>>> get_regions(const map<Complex, char>& garden) {
    map<char, vector<Complex>> gardens;
    for (const auto& [pos, gtype] : garden) {
        gardens[gtype].push_back(pos);
    }

    map<char, vector<vector<Complex>>> regions;
    for (const auto& [gtype, positions] : gardens) {
        regions[gtype] = {};
        set<Complex> visited;
        for (const Complex& pos : positions) {
            if (visited.count(pos)) continue;
            vector<Complex> group;
            vector<Complex> neighs = {pos};
            visited.insert(pos);
            while (!neighs.empty()) {
                Complex spot = neighs.back();
                neighs.pop_back();
                group.push_back(spot);
                for (const auto& [dir_id, d] : dirs) {
                    Complex new_spot = spot + d;
                    if (garden.count(new_spot) && !visited.count(new_spot) && garden.at(new_spot) == gtype) {
                        visited.insert(new_spot);
                        neighs.push_back(new_spot);
                    }
                }
            }
            regions[gtype].push_back(group);
        }
    }
    return regions;
}

pair<int, map<char, vector<vector<Complex>>>> part1(const map<Complex, char>& garden) {
    map<char, vector<vector<Complex>>> regions = get_regions(garden);
    int cost = 0;
    for (const auto& [k, v] : regions) {
        for (const auto& subregion : v) {
            int area = subregion.size();
            int perimeter = 0;
            for (const Complex& spot : subregion) {
                for (const auto& [dir_id, d] : dirs) {
                    perimeter += (subregion.end() == find(subregion.begin(), subregion.end(), spot + d));
                }
            }
            cost += area * perimeter;
        }
    }
    return {cost, regions};
}

int count_corners(const Complex& pos, const vector<Complex>& region) {
    int corners = 0;
    array<bool, 8> adjacent = {false};
    for (const auto& [i, d] : full_dirs) {
        if (find(region.begin(), region.end(), pos + d) != region.end()) {
            adjacent[i] = true;
        }
    }

    if (!adjacent[0] && !adjacent[2] && !adjacent[4] && !adjacent[6]) corners += 4;

    if ((adjacent[0] && !adjacent[2] && !adjacent[4] && !adjacent[6]) ||
        (adjacent[2] && !adjacent[0] && !adjacent[4] && !adjacent[6]) ||
        (adjacent[4] && !adjacent[2] && !adjacent[0] && !adjacent[6]) ||
        (adjacent[6] && !adjacent[2] && !adjacent[4] && !adjacent[0])) corners += 2;

    if ((adjacent[4] && adjacent[2] && !adjacent[0] && !adjacent[6]) ||
        (adjacent[4] && adjacent[6] && !adjacent[0] && !adjacent[2]) ||
        (adjacent[0] && adjacent[2] && !adjacent[4] && !adjacent[6]) ||
        (adjacent[0] && adjacent[6] && !adjacent[4] && !adjacent[2])) corners += 1;

    if ((adjacent[2] && adjacent[0] && !adjacent[1]) ||
        (adjacent[2] && adjacent[4] && !adjacent[3]) ||
        (adjacent[6] && adjacent[0] && !adjacent[7]) ||
        (adjacent[6] && adjacent[4] && !adjacent[5])) corners += 1;

    return corners;
}

int part2(const map<char, vector<vector<Complex>>>& regions) {
    int cost = 0;
    for (const auto& [k, v] : regions) {
        for (const auto& subregion : v) {
            int area = subregion.size();
            int perimeter = 0;
            for (const Complex& pos : subregion) {
                perimeter += count_corners(pos, subregion);
            }
            cost += area * perimeter;
        }
    }
    return cost;
}

int main() {
    string title = "Day 12: Garden Groups";
    string sub = string(title.length() + 2, '-');

    cout << endl;
    cout << " " << title << " " << endl;
    cout << sub << endl;

    map<Complex, char> inputs = loadInput("input_12.txt");

    auto t0 = high_resolution_clock::now();
    auto [res1, regions] = part1(inputs);
    auto t1 = duration_cast<microseconds>(high_resolution_clock::now() - t0).count() / 1000000.0;

    t0 = high_resolution_clock::now();
    int res2 = part2(regions);
    auto t2 = duration_cast<microseconds>(high_resolution_clock::now() - t0).count() / 1000000.0;

    cout << fixed << setprecision(5);
    cout << "🎄 Part 1: " << res1 << " (" << t1 << ") - 🎄🎅 Part 2: " << res2 << " (" << t2 << ")" << endl;

    return 0;
}