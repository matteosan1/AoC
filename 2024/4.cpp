#include <chrono>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void part1(char xwords[100][100], const int& row, const int& cols) {
  
  for (int i = 0; i <= row; i++) {
    for (int j = 0; j < cols; j++) {
      if (xwords[i][j] == 'X') {
	
      }
    }
    cout << endl;
  }
  
  //std::cout << "🎄   Part 1: " << tot;
}

int main() {
  ifstream file("input_4.txt");

  if (!file.is_open()) {
    cerr << "Error opening file!" << endl;
    return 1;
  }

  char xwords[100][100];
  int row = 0, col = 0, columns=0;

  char c;
  while (file.get(c)) {
    if (c == '\n') {
      row++;
      columns = col;
      col = 0;
    } else {
      xwords[row][col] = c;
      col++;
    }
  }

  file.close();

  std::cout << "Day 4: Ceres Search" << std::endl;

  //auto start = std::chrono::high_resolution_clock::now();
  part1(xwords, row, columns);
  //auto end = std::chrono::high_resolution_clock::now();
  //auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
  //std::cout << " - " << duration.count() << "\u00B5s" << std::endl;
  //
  //start = std::chrono::high_resolution_clock::now();
  //part2(memory);
  //end = std::chrono::high_resolution_clock::now();
  //duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
  //std::cout << " - " << duration.count() << "\u00B5s" << std::endl;

  return 0;
}
