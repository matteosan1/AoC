#include <complex>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <limits>
#include <iostream>
#include <string>
#include <utility>
#include <algorithm>
#include <chrono>
#include <fstream> // Include for file I/O
#include <sstream> // Include for stringstream

using namespace std;
using namespace std::chrono;

const complex<int> DIRECTIONS[4] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

const string RED = "\033[31m";
const string ENDC = "\033[0m";

vector<complex<int>> readInput(const string& filename) {
    vector<complex<int>> bytes;
    std::ifstream file(filename);
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            int x, y;
            char comma;
            std::istringstream iss(line);
            if (iss >> x >> comma >> y && comma == ',') {
                bytes.push_back({x, y});
            }
        }
        file.close();
    } else {
        std::cerr << "Unable to open file: " << filename << std::endl;
    }
    return bytes;
}

map<complex<int>, int> simulate_falling(const vector<complex<int>>& bytes, int nbytes, int width) {
  map<complex<int>, int> memory;
  for (int y = 0; y < width; ++y) {
    for (int x = 0; x < width; ++x) {
      complex<int> c(x, y);
      memory[c] = (find(bytes.begin(), bytes.begin() + nbytes, c) != bytes.begin() + nbytes) ? 0 : 1;
    }
  }
  return memory;
}

bool is_valid(const map<complex<int>, int>& grid, complex<int> c) {
  return grid.count(c) == 0 || grid.at(c) != 1;
}

vector<complex<int>> get_neighbors(const map<complex<int>, int>& grid,
				   complex<int> c,
				   const vector<complex<int>>* new_walls = nullptr) {
  vector<complex<int>> neighbors;
  for (const complex<int>& dc : DIRECTIONS) {
    complex<int> nc = c + dc;
    if (new_walls == nullptr) {
      if (is_valid(grid, nc)) {
        neighbors.push_back(nc);
      }
    } else {
      if (is_valid(grid, nc) && find(new_walls->begin(), new_walls->end(), nc) == new_walls->end()) {
        neighbors.push_back(nc);
      }
    }
  }
  return neighbors;
}

pair<int, vector<complex<int>>> solve(const map<complex<int>, int>& grid,
				      int width,
				      const vector<complex<int>>* new_walls = nullptr,
				      bool get_path = false) {
  complex<int> start(0, 0);
  complex<int> target(width - 1, width - 1);
  priority_queue<pair<int, complex<int>>, vector<pair<int, complex<int>>>, greater<pair<int, complex<int>>>> q;
  set<complex<int>> visited;
  map<complex<int>, complex<int>> predecessors;

  q.push({0, start});
  visited.insert(start); // Important: Mark start as visited initially

  while (!q.empty()) {
    int cost = q.top().first;
    complex<int> c = q.top().second;
    q.pop();

    if (c == target) {
      if (!get_path) {
        return {cost, {}};
      } else {
        vector<complex<int>> path;
        complex<int> current = c;
        while (current != start) {
          path.push_back(current);
          current = predecessors[current];
        }
        path.push_back(start);
        reverse(path.begin(), path.end());
        return {cost, path};
      }
    }

    for (const complex<int>& nc : get_neighbors(grid, c, new_walls)) {
      if (visited.find(nc) == visited.end()) {
        int new_cost = cost + 1;
        q.push({new_cost, nc});
        predecessors[nc] = c;
        visited.insert(nc); // Mark as visited when enqueued
      }
    }
  }
  return {-1, {}};
}

void draw(const map<complex<int>, int>& memory, const vector<complex<int>>& sits = {}, int width = 0) {
    cout << endl;
    int xmax, ymax;
    if (width == 0) {
        xmax = ymax = 0;
        for (const auto& pair : memory) {
            xmax = max(xmax, pair.first.real() + 1);
            ymax = max(ymax, pair.first.imag() + 1);
        }
    } else {
        xmax = ymax = width;
    }
    for (int y = 0; y < ymax; ++y) {
        for (int x = 0; x < xmax; ++x) {
            complex<int> c(x, y);
            if (find(sits.begin(), sits.end(), c) != sits.end()) {
                cout << RED << "O" << ENDC;
            } else if (memory.count(c) && memory.at(c) == 1) {
                cout << "#";
            } else {
                cout << ".";
            }
        }
        cout << endl;
    }
}

void part1(const vector<complex<int>>& bytes) {
    int nbytes = 1024;
    int width = 71;
    map<complex<int>, int> memory = simulate_falling(bytes, nbytes, width);
    auto result = solve(memory, width, nullptr, true);
    int cost = result.first;
    vector<complex<int>> path = result.second;
    draw(memory, path, width);
    cout << "🎄 Part 1: " << cost << endl;
}

//void part2(const vector<complex<int>>& bytes) {
//    int width = 71;
//    map<complex<int>, int> memory = simulate_falling(bytes, 1024, width);
//    int low = 1024;
//    int high = bytes.size() - 1;
//    vector<complex<int>> path;
//    int mid = 0;
//
//    while (low <= high) {
//        mid = (low + high) / 2;
//
//        auto result = solve(memory, width, &vector<complex<int>>(bytes.begin() + 1024, bytes.begin() + mid), true);
//        int cost = result.first;
//        path = result.second;
//
//        if (cost != -1) {
//            low = mid + 1;
//        } else {
//            if (mid == low || solve(memory, width, &vector<complex<int>>(bytes.begin() + 1024, bytes.begin() + mid - 1)).first != -1) {
//                break;
//            } else {
//                high = mid - 1;
//            }
//        }
//    }
//    cout << "🎄🎅 Part 2: " << bytes[mid - 1] << endl;
//}

int main() {
    string title = "Day 18: RAM Run";
    string sub = string(title.length() + 2, '-');

    cout << endl;
    cout << " " << title << " " << endl;
    cout << sub << endl;

    vector<complex<int>> inputs = readInput("input_18.txt"); // Provide the correct filename

    auto start = high_resolution_clock::now();
    part1(inputs);
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(end - start);
    cout << duration.count() << " ms" << endl;

//    start = high_resolution_clock::now();
//    part2(inputs);
//    end = high_resolution_clock::now();
//    duration = duration_cast<milliseconds>(end - start);
//    cout << duration.count() << " ms" << endl;
//
    return 0;
}
