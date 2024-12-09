#include <chrono>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

void part1(vector<int>& id1, vector<int>& id2) {
  sort(id1.begin(), id1.end());
  sort(id2.begin(), id2.end());
  
  int diff = 0;
  for (int i=0; i<id1.size(); i++)
    diff += abs(id1[i] - id2[i]);

  std::cout << "🎄   Part 1: " << diff;
}

void part2(vector<int>& id1, vector<int>& id2) {
  
  unordered_map<int, int> occurrencies;
  for (int id: id2)
    occurrencies[id]++;
  
  int diff = 0;
  for (int i=0; i<id1.size(); i++)
    diff += id1[i]*occurrencies[id1[i]];
  
  std::cout << "🎄🎅 Part 2: " << diff;
}

int main() {
  ifstream file("input_1.txt");
  
  if (!file.is_open()) {
    cerr << "Error opening file!" << endl;
    return 1;
  }
  
  vector<int> id1, id2;

  string line;
  while (getline(file, line)) {
    istringstream iss(line);
    string column1, column2;
    
    if (getline(iss, column1, ' ') && getline(iss, column2)) {
      id1.push_back(move(stoi(column1)));
      id2.push_back(move(stoi(column2)));
    } else {
      cerr << "Invalid line: " << line << endl;
    }
  }

  file.close();

  std::cout << "Day 1: Historian Hysteria" << std::endl;

  auto start = std::chrono::high_resolution_clock::now();
  part1(id1, id2);
  auto end = std::chrono::high_resolution_clock::now();
  auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
  std::cout << " - " << duration.count() << "\u00B5s" << std::endl; 

  start = std::chrono::high_resolution_clock::now();
  part2(id1, id2);
  end = std::chrono::high_resolution_clock::now();
  duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
  std::cout << " - " << duration.count() << "\u00B5s" << std::endl; 

  return 0;
}
