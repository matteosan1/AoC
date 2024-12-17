C++

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <array>
#include <cmath>
#include <numeric>
#include <chrono>
#include <iomanip>

using namespace std;
using namespace std::chrono;

class Machine {
private:
    array<array<double, 2>, 2> button;
    array<double, 2> prize;

public:
    Machine() : button{{{0, 0}, {0, 0}}}, prize{0, 0} {}

    pair<double, double> solve() {
        double det = button[0][0] * button[1][1] - button[0][1] * button[1][0];
        if (abs(det) < 1e-9) { // Check for near-zero determinant
            return {-1, -1}; // Indicate no solution
        }
        double a = (prize[0] * button[1][1] - prize[1] * button[1][0]) / det;
        double b = (prize[1] * button[0][0] - prize[0] * button[0][1]) / det;

        if (abs(round(a) - a) < 1e-3 && abs(round(b) - b) < 1e-3) {
            return {round(a), round(b)};
        } else {
            return {-1, -1};
        }
    }

    int cost() {
        pair<double, double> pushes = solve();
        if (pushes.first == -1 && pushes.second == -1) {
            return 0;
        } else {
            return static_cast<int>(pushes.first) * 3 + static_cast<int>(pushes.second) * 1;
        }
    }

    void setButtonRow(int row, const string& data) {
        vector<string> items = split(data, ',');
        for (size_t i = 0; i < 2; ++i) {
            button[row][i] = stod(items[i].substr(items[i].find('+') + 1));
        }
    }

    void setPrize(const string& data) {
        vector<string> items = split(data, ',');
        for (size_t i = 0; i < 2; ++i) {
            prize[i] = stod(items[i].substr(items[i].find('=') + 1));
        }
    }

private:
    vector<string> split(const string& str, char delimiter) {
        vector<string> tokens;
        string token;
        istringstream tokenStream(str);
        while (getline(tokenStream, token, delimiter)) {
            tokens.push_back(token);
        }
        return tokens;
    }
};

vector<Machine> loadInput(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        exit(1);
    }

    vector<Machine> machines;
    Machine machine;
    string line;
    while (getline(file, line)) {
        if (line.empty()) continue;
        if (line.rfind("Button A", 0) == 0) {
            machine.setButtonRow(0, line);
        } else if (line.rfind("Button B", 0) == 0) {
            machine.setButtonRow(1, line);
        } else if (line.rfind("Prize", 0) == 0) {
            machine.setPrize(line);
            machines.push_back(machine);
            machine = Machine(); // Create a new machine
        }
    }
    file.close();
    return machines;
}

void part1(const vector<Machine>& machines) {
    int cost = 0;
    for (const auto& m : machines) {
        cost += m.cost();
    }
    cout << "🎄 Part 1: " << cost << endl;
}

void part2(vector<Machine>& machines) {
    long long const_val = 10000000000000;
    long long cost = 0;
    for (auto& m : machines) {
        m.setPrize(to_string(const_val + m.prize[0]) + "," + to_string(const_val + m.prize[1]));
        cost += m.cost();
    }
    cout << "🎄🎅 Part 2: " << cost << endl;
}

int main() {
    string title = "Day 13: Claw Contraption";
    string sub = string(title.length() + 2, '-');

    cout << endl;
    cout << " " << title << " " << endl;
    cout << sub << endl;

    vector<Machine> inputs = loadInput("input_13.txt");

    auto t1_start = high_resolution_clock::now();
    part1(inputs);
    auto t1_end = high_resolution_clock::now();
    auto duration1 = duration_cast<milliseconds>(t1_end - t1_start);
    cout << "Timing: " << duration1.count() << " ms" << endl;

    auto t2_start = high_resolution_clock::now();
    part2(inputs);
    auto t2_end = high_resolution_clock::now();
    auto duration2 = duration_cast<milliseconds>(t2_end - t2_start);
    cout << "Timing: " << duration2.count() << " ms" << endl;

    return 0;
}