#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <map>
#include <chrono>
#include <iomanip>
#include <numeric>

using namespace std;
using namespace std::chrono;

vector<int> split_int(const string& s, char delim) {
    vector<int> result;
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) {
        result.push_back(stoi(item));
    }
    return result;
}

pair<vector<vector<int>>, vector<vector<int>>> loadInput(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        exit(1);
    }

    vector<vector<int>> orderings;
    vector<vector<int>> updates;
    string line;
    while (getline(file, line)) {
        if (line.find('|') != string::npos) {
            orderings.push_back(split_int(line, '|'));
        } else if (line.find(',') != string::npos) {
            updates.push_back(split_int(line, ','));
        }
    }
    return {orderings, updates};
}

vector<int> part1(const vector<vector<int>>& orderings, const vector<vector<int>>& updates) {
    int mid_page = 0;
    vector<int> ordered;
    for (size_t iu = 0; iu < updates.size(); ++iu) {
        const auto& upd = updates[iu];
        bool is_ordered = true;
        for (size_t x = 0; x < upd.size() - 1; ++x) {
            if (find(orderings.begin(), orderings.end(), vector<int>{upd[x], upd[x + 1]}) == orderings.end()) {
                is_ordered = false;
                break;
            }
        }
        if (is_ordered) {
            ordered.push_back(iu);
            mid_page += upd[upd.size() / 2];
        }
    }

    cout << "🎄 Part 1: " << mid_page << endl;
    return ordered;
}

void part2(const vector<vector<int>>& orderings, const vector<vector<int>>& updates, const vector<int>& ordered) {
    int mid_page = 0;
    for (size_t iu = 0; iu < updates.size(); ++iu) {
        if (find(ordered.begin(), ordered.end(), iu) != ordered.end()) {
            continue;
        }

        const auto& upd = updates[iu];
        vector<vector<int>> new_orderings;
        for (const auto& o : orderings) {
            if (find(upd.begin(), upd.end(), o[0]) != upd.end() &&
                find(upd.begin(), upd.end(), o[1]) != upd.end()) {
                new_orderings.push_back(o);
            }
        }

        map<int, int> rank;
        for (int u : upd) {
            rank[u] = 0;
            for (const auto& o : new_orderings) {
                if (o[1] == u) {
                    rank[u]++;
                }
            }
        }

        vector<pair<int, int>> rank_vec(rank.begin(), rank.end());
        sort(rank_vec.begin(), rank_vec.end(), [](const auto& left, const auto& right) {
            return left.second < right.second;
        });
        vector<int> sorted_dict;
        for(const auto& p : rank_vec) sorted_dict.push_back(p.first);
        mid_page += sorted_dict[sorted_dict.size() / 2];
    }

    cout << "🎄🎅 Part 2: " << mid_page << endl;
}

int main() {
    string title = "Day 5: Print Queue";
    string sub = string(title.length() / 2 + 2, '⛄');

    cout << endl;
    cout << " " << title << " " << endl;
    cout << sub << endl;

    auto [orderings, updates] = loadInput("input_5.txt");

    auto t0 = high_resolution_clock::now();
    auto ordered = part1(orderings, updates);
    auto t1 = duration_cast<microseconds>(high_resolution_clock::now() - t0).count() / 1000000.0;

    t0 = high_resolution_clock::now();
    part2(orderings, updates, ordered);
    auto t2 = duration_cast<microseconds>(high_resolution_clock::now() - t0).count() / 1000000.0;

    cout << fixed << setprecision(5);
    cout << "Time Part 1: " << t1 << endl;
    cout << "Time Part 2: " << t2 << endl;

    return 0;
}