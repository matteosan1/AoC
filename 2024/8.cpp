#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <chrono>
#include <iomanip>
#include <cmath>
#include <tuple>

using namespace std;
using namespace std::chrono;

using Point = pair<int, int>;

pair<map<char, vector<Point>>, int> loadInput(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        exit(1);
    }

    map<char, vector<Point>> antennas;
    string line;
    int y = 0;
    int xmax = 0;
    while (getline(file, line)) {
        xmax = max(xmax, (int)line.length());
        for (int x = 0; x < line.length(); ++x) {
            if (line[x] != '.' && line[x] != '#') {
                antennas[line[x]].push_back({x, y});
            }
        }
        y++;
    }
    int ymax = y;
    return {antennas, xmax, ymax};
}

void draw_map(const map<char, vector<Point>>& antennas, const set<Point>& antinodes, int xmax, int ymax) {
    map<Point, char> antennas_drawing;
    for (const auto& [k, v] : antennas) {
        for (const auto& item : v) {
            antennas_drawing[item] = k;
        }
    }

    for (int y = 0; y < ymax; ++y) {
        for (int x = 0; x < xmax; ++x) {
            Point current_point(x,y);
            if (antennas_drawing.count(current_point)) {
                cout << antennas_drawing.at(current_point);
            } else if (antinodes.count(current_point)) {
                cout << "#";
            } else {
                cout << ".";
            }
        }
        cout << endl;
    }
}

int part1(const map<char, vector<Point>>& antennas, int xmax, int ymax) {
    set<Point> antinodes;
    for (const auto& [freq, poss] : antennas) {
        for (size_t i = 0; i < poss.size() - 1; ++i) {
            for (size_t j = i + 1; j < poss.size(); ++j) {
                int dx = poss[j].first - poss[i].first;
                int dy = poss[j].second - poss[i].second;

                for (int c : {-1, 2}) {
                    Point an(poss[i].first + c * dx, poss[i].second + c * dy);
                    if (an.first >= 0 && an.first < xmax && an.second >= 0 && an.second < ymax) {
                        antinodes.insert(an);
                    }
                }
            }
        }
    }
    return antinodes.size();
}

int part2(const map<char, vector<Point>>& antennas, int xmax, int ymax) {
    set<Point> antinodes;
    for (const auto& [freq, poss] : antennas) {
        for (size_t i = 0; i < poss.size() - 1; ++i) {
            for (size_t j = i + 1; j < poss.size(); ++j) {
                antinodes.insert(poss[i]);
                antinodes.insert(poss[j]);
                int dx = poss[j].first - poss[i].first;
                int dy = poss[j].second - poss[i].second;

                Point an = poss[i];
                bool forward = true;
                bool backward = true;
                int c = 0;
                while (true) {
                    an = {poss[i].first + c * dx, poss[i].second + c * dy};
                    if (an.first >= 0 && an.first < xmax && an.second >= 0 && an.second < ymax) {
                        antinodes.insert(an);
                    } else {
                        forward = false;
                    }

                    an = {poss[i].first - c * dx, poss[i].second - c * dy};
                    if (an.first >= 0 && an.first < xmax && an.second >= 0 && an.second < ymax) {
                        antinodes.insert(an);
                    } else {
                        backward = false;
                    }

                    if (!forward && !backward) {
                        break;
                    } else {
                        c++;
                    }
                }
            }
        }
    }
    return antinodes.size();
}

int main() {
    string title = "Day 8: Resonant Collinearity";
    string sub = string(title.length() + 2, '-');

    cout << endl;
    cout << " " << title << " " << endl;
    cout << sub << endl;

    auto [antennas, xmax, ymax] = loadInput("input_8.txt");

    auto t0 = high_resolution_clock::now();
    int res1 = part1(antennas, xmax, ymax);
    auto t1 = duration_cast<microseconds>(high_resolution_clock::now() - t0).count() / 1000000.0;

    t0 = high_resolution_clock::now();
    int res2 = part2(antennas, xmax, ymax);
    auto t2 = duration_cast<microseconds>(high_resolution_clock::now() - t0).count() / 1000000.0;

    cout << fixed << setprecision(5);
    cout << "🎄 Part 1: " << res1 << " (" << t1 << ") - 🎄🎅 Part 2: " << res2 << " (" << t2 << ")" << endl;

    return 0;
}