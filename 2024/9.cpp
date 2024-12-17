#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <numeric>
#include <chrono>
#include <iomanip>
#include <algorithm>

using namespace std;
using namespace std::chrono;

vector<string> split(const string& str, char delim) {
    vector<string> result;
    stringstream ss(str);
    string token;
    while (getline(ss, token, delim)) {
        result.push_back(token);
    }
    return result;
}

string loadInput(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        exit(1);
    }
    string disk;
    getline(file, disk);
    return disk;
}

int part1(const string& disk) {
    vector<int> fragments;
    try {
        for (size_t i = 0; i < disk.length(); i += 2) {
            for (int j = 0; j < disk[i] - '0'; ++j) {
                fragments.push_back(i / 2);
            }
            for (int j = 0; j < disk[i + 1] - '0'; ++j) {
                fragments.push_back(-1);
            }
        }
    } catch (const std::out_of_range& oor) {
        // Handle potential out-of-range errors (if input is malformed)
    }

    int idx_rvs = fragments.size() - 1;
    for (size_t idx = 0; idx < fragments.size(); ++idx) {
        if (fragments[idx] == -1) {
            while (fragments[idx_rvs] == -1 && idx_rvs > idx) {
                idx_rvs--;
            }
            if(idx_rvs <= idx) break;
            fragments[idx] = fragments[idx_rvs];
            fragments[idx_rvs] = -1;
            idx_rvs--;
        }
        if (idx == idx_rvs) break;
    }

    int checksum = 0;
    for (size_t i = 0; i < fragments.size(); ++i) {
        if (fragments[i] != -1) {
            checksum += i * fragments[i];
        }
    }
    return checksum;
}

class Fragment {
public:
    int id;
    int length;

    Fragment(int id, int length) : id(id), length(length) {}

    int checksum(int idx) const {
        int v = 0;
        for (int i = 0; i < length; ++i) {
            v += id * (idx + i);
        }
        return v;
    }

    friend ostream& operator<<(ostream& os, const Fragment& f) {
        for (int i = 0; i < f.length; ++i) {
            os << (f.id == -1 ? "." : to_string(f.id));
        }
        return os;
    }
};

int part2(const string& disk) {
    vector<Fragment> fragments;
    for (size_t i = 0; i < disk.length(); ++i) {
        int id = (i % 2 == 0) ? i / 2 : -1;
        fragments.emplace_back(id, disk[i] - '0');
    }

    int idx_rvs = fragments.size() - 1;
    while (idx_rvs > 1) {
        if (fragments[idx_rvs].id != -1 && fragments[idx_rvs].length != 0) {
            size_t idx = 0;
            while (idx < fragments.size()) {
                if (idx == idx_rvs) break;
                if (fragments[idx].id == -1) {
                    if (fragments[idx].length >= fragments[idx_rvs].length) {
                        int old_length = fragments[idx].length;
                        fragments[idx].id = fragments[idx_rvs].id;
                        fragments[idx].length = fragments[idx_rvs].length;
                        fragments.insert(fragments.begin() + idx + 1, Fragment(-1, old_length - fragments[idx_rvs].length));
                        idx_rvs++;
                    } else {
                        fragments[idx].id = fragments[idx_rvs].id;
                        fragments[idx_rvs].id = -1;
                        break;
                    }
                }
                idx++;
            }
        }
        idx_rvs--;
    }

    int idx = 0;
    int checksum = 0;
    for (const auto& f : fragments) {
        if (f.id != -1) {
            checksum += f.checksum(idx);
        }
        idx += f.length;
    }
    return checksum;
}

int main() {
    string title = "Day 9: Disk Fragmenter";
    string sub = string(title.length() + 2, '-');

    cout << endl;
    cout << " " << title << " " << endl;
    cout << sub << endl;

    string inputs = loadInput("input_9.txt");

    auto t0 = high_resolution_clock::now();
    int res1 = part1(inputs);
    auto t1 = duration_cast<microseconds>(high_resolution_clock::now() - t0).count() / 1000000.0;

    t0 = high_resolution_clock::now();
    int res2 = part2(inputs);
    auto t2 = duration_cast<microseconds>(high_resolution_clock::now() - t0).count() / 1000000.0;

    cout << fixed << setprecision(5);
    cout << "🎄 Part 1: " << res1 << " (" << t1 << ") - 🎄🎅 Part 2: " << res2 << " (" << t2 << ")" << endl;

    return 0;
}