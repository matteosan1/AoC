#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <chrono>

std::vector<int> loadInput(const std::string& filename) {
    std::ifstream file(filename);
    std::vector<int> numbers;
    int num;
    while (file >> num) {
        numbers.push_back(num);
    }
    return numbers;
}

uint32_t generate(uint32_t n) {
    n = (n << 6 ^ n) & 0xFFFFFF;
    n = (n >> 5 ^ n) & 0xFFFFFF;
    return (n << 11 ^ n) & 0xFFFFFF;
}

int main() {
    std::vector<int> secret_numbers = loadInput("input_22.txt");

    // Part 1
    uint64_t secret_sum = 0;
    auto start1 = std::chrono::high_resolution_clock::now();
    for (int n : secret_numbers) {
        for (int i = 0; i < 2000; ++i) {
            n = generate(n);
        }
        secret_sum += n;
    }
    auto end1 = std::chrono::high_resolution_clock::now();
    auto duration1 = std::chrono::duration_cast<std::chrono::microseconds>(end1 - start1);
    std::cout << "🎄 Part 1: " << secret_sum << std::endl;
    std::cout << "Time taken: " << duration1.count() / 1000.0 << " ms" << std::endl;

    // Part 2
    std::vector<std::vector<int>> total_keys;
    std::vector<int> totals;
    auto start2 = std::chrono::high_resolution_clock::now();
    for (int n : secret_numbers) {
        std::vector<int> seq_key(4, 0);
        int prev = n % 10;
        for (int i = 0; i < 2000; ++i) {
            n = generate(n);
            int curr = n % 10;
            for (int i=0; i<3; i++) {
                seq_key[i] = seq_key[i+1];
            }
            seq_key[3] = curr - prev;
            prev = curr;
            if (i >= 3) {
                auto idx = std::find(total_keys.begin(), total_keys.end(), seq_key);
                if (idx  != total_keys.end()) {
                    totals[idx-total_keys.begin()] += curr; 
                } else {
                    total_keys.push_back(seq_key);
                    totals.push_back(curr);
                }
            }
        }
    }
    auto end2 = std::chrono::high_resolution_clock::now();
    auto duration2 = std::chrono::duration_cast<std::chrono::microseconds>(end2 - start2);
    int max_value = 0;
    for (const auto& value : totals) {
        max_value = std::max(max_value, value);
    }
    std::cout << "🎄🎅 Part 2: " << max_value << std::endl;
    std::cout << "Time taken: " << duration2.count() / 1000.0 << " ms" << std::endl;

    return 0;
}