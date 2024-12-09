#include <chrono>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>

using namespace std;

void part1(string& memory) {
  const regex pattern("mul\\((\\d{1,3}),(\\d{1,3})\\)");//|do\\(\\)|don't\\(\\)");
  int tot = 0;
  sregex_iterator iter(memory.begin(), memory.end(), pattern);
  sregex_iterator end_iter;
  
  while (iter != end_iter) {
    smatch match = *iter;
    
    tot += stoi(match[1])*stoi(match[2]);
    ++iter;
  }

  std::cout << "🎄   Part 1: " << tot;
}

void part2(string& memory) {

  const regex pattern("mul\\((\\d{1,3}),(\\d{1,3})\\)|do\\(\\)|don't\\(\\)");
  int tot = 0;
  bool enabled = true;
  sregex_iterator iter(memory.begin(), memory.end(), pattern);
  sregex_iterator end_iter;
  
  while (iter != end_iter) {
    smatch match = *iter;
    if (match.str() == "do()")
      enabled = true;
    else if (match.str() == "don't()")
      enabled = false;
    else {
      if (enabled)
	tot += stoi(match[1])*stoi(match[2]);
    }
    ++iter;
  }

  std::cout << "🎄🎅 Part 2: " << tot;
}

int main() {
  ifstream file("input_3.txt");
  
  if (!file.is_open()) {
    cerr << "Error opening file!" << endl;
    return 1;
  }
  
  string memory;
  string line;
  while (getline(file, line)) {
    memory += line;  
  }

  file.close();

  std::cout << "Day 3: Mull It Over" << std::endl;

  auto start = std::chrono::high_resolution_clock::now();
  part1(memory);
  auto end = std::chrono::high_resolution_clock::now();
  auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
  std::cout << " - " << duration.count() << "\u00B5s" << std::endl; 

  start = std::chrono::high_resolution_clock::now();
  part2(memory);
  end = std::chrono::high_resolution_clock::now();
  duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
  std::cout << " - " << duration.count() << "\u00B5s" << std::endl; 

  return 0;
}
