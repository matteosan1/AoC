#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <chrono>

using namespace std;
using namespace std::chrono;

class IntCode {
private:
    int A;
    int B;
    int C;
    vector<int> code;
    vector<int> out;
    int pointer;

public:
    IntCode() : A(0), B(0), C(0), pointer(0) {}

    void reset() {
        pointer = 0;
        out.clear();
    }

    vector<int> getCode() {
      return code;
    }
    void setCode(const string& code_str) {
        code.clear(); // Clear existing code
        stringstream ss(code_str);
        string token;
        while (getline(ss, token, ',')) {
            code.push_back(stoi(token));
        }
    }

    void setRegister(int a = -1, int b = -1, int c = -1) {
        if (a != -1) A = a;
        if (b != -1) B = b;
        if (c != -1) C = c;
    }

    int getRegister(char reg) const { // Make const
        if (reg == 'A') return A;
        if (reg == 'B') return B;
        if (reg == 'C') return C;
        return -1; // Or throw an exception for invalid register
    }

    string output() const{ // Make const
        string result;
        for (int o : out) {
            result += to_string(o) + ",";
        }
        if (!out.empty()) {
            result.pop_back(); // Remove the trailing comma
        }
        return result;
    }

    void run(bool debug = false) {
        while (pointer < code.size()) {
            int opcode = code[pointer];
            int operand = (pointer + 1 < code.size()) ? code[pointer + 1] : 0;

            if (opcode == 0) { // adv
                A /= (1 << getRegister('B'));
                pointer += 2;
            } else if (opcode == 1) { // bxl
                B ^= operand;
                pointer += 2;
            } else if (opcode == 2) { // bst
                B = getRegister('B') % 8;
                pointer += 2;
            } else if (opcode == 3) { // jnz
                if (A != 0) {
                    pointer = operand;
                } else {
                    pointer += 2;
                }
            } else if (opcode == 4) { // bxc
                B ^= C;
                pointer += 2;
            } else if (opcode == 5) { // out
                out.push_back(getRegister('B') % 8);
                pointer += 2;
            } else if (opcode == 6) { // bdv
                B = A / (1 << getRegister('B'));
                pointer += 2;
            } else if (opcode == 7) { // cdv
                C = A / (1 << getRegister('B'));
                pointer += 2;
            } else {
                cerr << "Invalid opcode: " << opcode << endl;
                return; // Exit the run loop on invalid opcode
            }

            if (debug) {
                cout << "A: " << A << " B: " << B << " C: " << C << endl;
            }
        }
    }
};

IntCode loadInput(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        exit(1);
    }

    IntCode intcode;
    string line;
    while (getline(file, line)) {
        if (line.empty()) continue;
        if (line.find("Register A:") != string::npos) {
            intcode.setRegister(stoi(line.substr(13)), -1, -1);
        } else if (line.find("Register B:") != string::npos) {
            intcode.setRegister(-1, stoi(line.substr(13)), -1);
        } else if (line.find("Register C:") != string::npos) {
            intcode.setRegister(-1, -1, stoi(line.substr(13)));
        } else if (line.find("Code:") != string::npos) {
            intcode.setCode(line.substr(7));
        }
    }
    return intcode;
}

int pyintcode(int A) {
    int B = A % 8;
    B = B ^ 6;
    int C = A / (1 << B);
    B = B ^ C;
    B = B ^ 4;
    return B % 8;
}

void findQuin(int A, const vector<int>& program, int col, vector<int>& res) {
    if (pyintcode(A) != program[program.size() - 1 - col]) {
        return;
    }

    if (col == program.size() - 1) {
        res.push_back(A);
    } else {
        for (int B = 0; B < 8; ++B) {
            findQuin(A * 8 + B, program, col + 1, res);
        }
    }
}

void part1(IntCode& intcode) {
    intcode.run();
    cout << "🎄 Part 1: " << intcode.output() << endl;
}

void part2(IntCode& intcode) {
    intcode.reset();
    const vector<int>& program = intcode.getCode();
    vector<int> res;
    for (int a = 0; a < 8; ++a) {
        findQuin(a, program, 0, res);
    }

    cout << "🎄🎅 Part 2: " << res[0] << endl;
}

int main() {
    string title = "Day 17: Chronospatial Computer";
    string sub = string(title.length() + 2, '-');

    cout << endl;
    cout << " " << title << " " << endl;
    cout << sub << endl;

    IntCode inputs = loadInput("input_17.txt");

    auto t1_start = high_resolution_clock::now();
    part1(inputs);
    auto t1_end = high_resolution_clock::now();
    auto duration1 = duration_cast<milliseconds>(t1_end - t1_start);
    cout << duration1.count() << " ms" << endl;

    auto t2_start = high_resolution_clock::now();
    part2(inputs);
    auto t2_end = high_resolution_clock::now();
    auto duration2 = duration_cast<milliseconds>(t2_end - t2_start);
    cout << duration2.count() << " ms" << endl;

    return 0;
}