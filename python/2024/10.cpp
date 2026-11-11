#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <complex>
#include <queue>
#include <set>
#include <chrono>
#include <iomanip>

using namespace std;
using namespace std::chrono;

using Complex = complex<int>;

map<int, Complex> dirs = {
    {0, {0, -1}}, {1, {1, 0}}, {2, {0, 1}}, {3, {-1, 0}}
};

pair<map<Complex, int>, vector<Complex>> loadInput(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        exit(1);
    }

    map<Complex, int> map;
    vector<Complex> starts;
    string line;
    int y = 0;
    while (getline(file, line)) {
        for (int x = 0; x < line.length(); ++x) {
            if (line[x] == '.') {
                map[{x, y}] = 0;
            } else if (line[x] == '0') {
                starts.push_back({x, y});
                map[{x, y}] = 0; // Assign 0 to the start position in the map
            } else {
                map[{x, y}] = line[x] - '0';
            }
        }
        y++;
    }
    return {map, starts};
}

int part1(const map<Complex, int>& map, const vector<Complex>& starts) {
    int score = 0;
    for (Complex start : starts) {
        queue<pair<Complex, int>> q;
        q.push({start, 0});
        set<Complex> visited;
        visited.insert(start);

        while (!q.empty()) {
            auto [pos, dist] = q.front();
            q.pop();

            if (dist == 9) {
                score++;
            }

            for (int i = 0; i < 4; ++i) {
                Complex npos = pos + dirs.at(i);
                if (map.count(npos) > 0 && visited.find(npos) == visited.end()) {
                    if (map.at(npos) - dist == 1) {
                        q.push({npos, map.at(npos)});
                        visited.insert(npos);
                    }
                }
            }
        }
    }
    return score;
}

int part2(const map<Complex, int>& map, const vector<Complex>& starts) {
    map<Complex, int> rate;
    for (Complex start : starts) {
        queue<pair<Complex, int>> q;
        q.push({start, 0});

        while (!q.empty()) {
            auto [pos, dist] = q.front();
            q.pop();

            if (dist == 9) {
                rate[pos]++;
            }

            for (int i = 0; i < 4; ++i) {
                Complex npos = pos + dirs.at(i);
                if (map.count(npos) > 0) {
                    if (map.at(npos) - dist == 1) {
                        q.push({npos, map.at(npos)});
                    }
                }
            }
        }
    }
    int sum = 0;
    for (const auto& [k, v] : rate) {
        sum += v;
    }
    return sum;
}

int main() {
    string title = "Day 10: Hoof It";
    string sub = string(title.length() + 2, '-');

    cout << endl;
    cout << " " << title << " " << endl;
    cout << sub << endl;

    auto [map, starts] = loadInput("input_10.txt");

    auto t0 = high_resolution_clock::now();
    int res1 = part1(map, starts);
    auto t1 = duration_cast<microseconds>(high_resolution_clock::now() - t0).count() / 1000000.0;

    t0 = high_resolution_clock::now();
    int res2 = part2(map, starts);
    auto t2 = duration_cast<microseconds>(high_resolution_clock::now() - t0).count() / 1000000.0;

    cout << fixed << setprecision(5);
    cout << "🎄 Part 1: " << res1 << " (" << t1 << ") - 🎄🎅 Part 2: " << res2 << " (" << t2 << ")" << endl;

    return 0;
}