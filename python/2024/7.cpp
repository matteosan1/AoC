#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <chrono>
#include <iomanip>
#include <cmath>

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

vector<pair<int, vector<int>>> loadInput(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        exit(1);
    }

    vector<pair<int, vector<int>>> operations;
    string line;
    while (getline(file, line)) {
        size_t colon_pos = line.find(": ");
        if (colon_pos != string::npos) {
            int target = stoi(line.substr(0, colon_pos));
            vector<int> operands = split_int(line.substr(colon_pos + 2), ' ');
            operations.push_back({target, operands});
        }
    }
    return operations;
}

int part1(const vector<pair<int, vector<int>>>& operations) {
    int valid = 0;
    for (const auto& o : operations) {
        int spaces = o.second.size() - 1;
        vector<char> sequence(spaces);

        function<void(int)> generate_sequences = 
            [&](int k) {
                if (k == spaces) {
                    long long result = o.second[0];
                    for (int i = 0; i < spaces; ++i) {
                        if (sequence[i] == '+') {
                            result += o.second[i + 1];
                        } else {
                            result *= o.second[i + 1];
                        }
                        if (result > o.first) {
                            return;
                        }
                    }
                    if (o.first == result) {
                        valid += result;
                        return;
                    }
                    return;

                } else {
                  sequence[k] = '+';
                  generate_sequences(k+1);
                  sequence[k] = '*';
                  generate_sequences(k+1);
                }
            };
        generate_sequences(0);

    }
    return valid;
}

int part2(const vector<pair<int, vector<int>>>& operations) {
    int valid = 0;
    for (const auto& o : operations) {
        int spaces = o.second.size() - 1;
        vector<char> sequence(spaces);

        function<void(int)> generate_sequences = 
            [&](int k) {
                if (k == spaces) {
                    long long result = o.second[0];
                    for (int i = 0; i < spaces; ++i) {
                        if (sequence[i] == '+') {
                            result += o.second[i + 1];
                        } else if (sequence[i] == '*') {
                            result *= o.second[i + 1];
                        } else {
                            int ofm = static_cast<int>(log10(abs(o.second[i + 1]))) + 1;
                            result = result * static_cast<long long>(pow(10, ofm)) + o.second[i + 1];
                        }
                        if (result > o.first) {
                            return;
                        }
                    }
                    if (o.first == result) {
                        valid += result;
                        return;
                    }
                    return;

                } else {
                  sequence[k] = '+';
                  generate_sequences(k+1);
                  sequence[k] = '*';
                  generate_sequences(k+1);
                  sequence[k] = '|';
                  generate_sequences(k+1);
                }
            };
        generate_sequences(0);
    }
    return valid;
}

int main() {
    string title = "Day 7: Bridge Repair";
    string sub = string(title.length() + 2, '-');

    cout << endl;
    cout << " " << title << " " << endl;
    cout << sub << endl;

    vector<pair<int, vector<int>>> inputs = loadInput("input_7.txt");

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