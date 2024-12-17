#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <chrono>
#include <iomanip>
#include <functional>

using namespace std;
using namespace std::chrono;

// Cache implementation (simple memoization)
template <typename K, typename V>
class Cache {
private:
    map<K, V> cache;
    function<V(K)> func;

public:
    Cache(function<V(K)> f) : func(f) {}

    V get(const K& key) {
        if (cache.count(key)) {
            return cache.at(key);
        } else {
            V result = func(key);
            cache[key] = result;
            return result;
        }
    }
};

vector<int> loadInput(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        exit(1);
    }

    vector<int> stones;
    string line;
    getline(file, line);
    stringstream ss(line);
    int stone;
    while (ss >> stone) {
        stones.push_back(stone);
    }
    return stones;
}

vector<int> rules_impl(int s) {
    if (s == 0) {
        return {1};
    }
    int oom = s == 0 ? 0 : static_cast<int>(log10(s) + 1);
    if (oom != 0 && oom % 2 == 0) {
        int s1 = s / static_cast<int>(pow(10, oom / 2));
        int s2 = s - s1 * static_cast<int>(pow(10, oom / 2));
        return {s1, s2};
    } else {
        return {s * 2024};
    }
}

int blinking(map<int, int>& vect, int blinks, Cache<int, vector<int>>& rules_cache) {
    for (int _ = 0; _ < blinks; ++_) {
        map<int, int> new_vect;
        for (const auto& [stone, i] : vect) {
            vector<int> s = rules_cache.get(stone);
            for (int item : s) {
                new_vect[item] += i;
            }
        }
        vect = new_vect;
    }
    int sum = 0;
    for(const auto& [k, v] : vect) sum += v;
    return sum;
}

long long part1(const vector<int>& stones, Cache<int, vector<int>>& rules_cache) {
    long long length = 0;
    for (int stone : stones) {
        map<int, int> init = {{stone, 1}};
        length += blinking(init, 1000, rules_cache);
    }
    return length;
}

long long part2(const vector<int>& stones, Cache<int, vector<int>>& rules_cache) {
    long long length = 0;
    for (int stone : stones) {
        map<int, int> init = {{stone, 1}};
        length += blinking(init, 75, rules_cache);
    }
    return length;
}

int main() {
    string title = "Day 11: Plutonian Pebbles";
    string sub = string(title.length() + 2, '-');

    cout << endl;
    cout << " " << title << " " << endl;
    cout << sub << endl;

    vector<int> inputs = loadInput("input_11.txt");
    Cache<int, vector<int>> rules_cache(rules_impl);

    auto t0 = high_resolution_clock::now();
    long long res1 = part1(inputs, rules_cache);
    auto t1 = duration_cast<microseconds>(high_resolution_clock::now() - t0).count() / 1000000.0;

    t0 = high_resolution_clock::now();
    long long res2 = part2(inputs, rules_cache);
    auto t2 = duration_cast<microseconds>(high_resolution_clock::now() - t0).count() / 1000000.0;

    cout << fixed << setprecision(5);
    cout << "🎄 Part 1: " << res1 << " (" << t1 << ") - 🎄🎅 Part 2: " << res2 << " (" << t2 << ")" << endl;

    return 0;
}