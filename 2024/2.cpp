#include <chrono>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> calculate_differences(const vector<int>& numbers) {
    vector<int> differences;

    for (size_t i = 1; i < numbers.size(); ++i) {
        int diff = numbers[i] - numbers[i - 1];
        differences.push_back(diff);
    }

    return differences;
}

bool all_positive(const vector<int>& numbers) {
    for (int num : numbers) {
        if (num <= 0) {
            return false;
        }
    }
    return true;
}

bool all_negative(const vector<int>& numbers) {
    for (int num : numbers) {
        if (num >= 0) {
            return false;
        }
    }
    return true;
}

void part1(vector<vector<int>>& reports) {

  int valid = 0;
  for (auto r : reports) {
    vector<int> differences = calculate_differences(r);
    if ((all_positive(differences) and *max_element(differences.begin(), differences.end()) <= 3) or (all_negative(differences) and *min_element(differences.begin(), differences.end()) >= -3)) valid++; 
  }

  std::cout << "🎄   Part 1: " << valid;
}

void part2(vector<vector<int>>& reports) {
  int valid = 0;
  for (auto r : reports) {
    vector<int> differences = calculate_differences(r);
    if ((all_positive(differences) and *max_element(differences.begin(), differences.end()) <= 3) or (all_negative(differences) and *min_element(differences.begin(), differences.end()) >= -3)) {
      valid++; 
    } else {
      vector<int> rnew(r.size()-1, 0);
      for (int i=0; i<r.size(); i++) {
	int y = 0;
	for (int j=0; j<r.size(); j++) {
	  if (i == j) continue;
	  rnew[y] = r[j];
	  y++;
	}
	vector<int> differences = calculate_differences(rnew);
	if ((all_positive(differences) and *max_element(differences.begin(), differences.end()) <= 3) or (all_negative(differences) and *min_element(differences.begin(), differences.end()) >= -3)) {
	  valid++;
	  break;
	}
      }	
    }
  }
  std::cout << "🎄🎅 Part 2: " << valid;
}

int main() {
  ifstream file("input_2.txt");
  
  if (!file.is_open()) {
    cerr << "Error opening file!" << endl;
    return 1;
  }
  
  vector<vector<int>> reports;

  string line;
  while (getline(file, line)) {
    vector<int> r;
    istringstream iss(line);
    string word;
    while (iss >> word) {
      try {
	r.push_back(stoi(word));
      } catch (const invalid_argument& e) {
	cerr << "Invalid input: " << word << endl;
      }
    }
    reports.push_back(r);
  }
  file.close();

  std::cout << "Day 2: Red-Nosed Reports" << std::endl;

  auto start = std::chrono::high_resolution_clock::now();
  part1(reports);
  auto end = std::chrono::high_resolution_clock::now();
  auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
  std::cout << " - " << duration.count() << "\u00B5s" << std::endl; 

  start = std::chrono::high_resolution_clock::now();
  part2(reports);
  end = std::chrono::high_resolution_clock::now();
  duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
  std::cout << " - " << duration.count() << "\u00B5s" << std::endl; 

  return 0;
}
