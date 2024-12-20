#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <chrono>
#include <iomanip>
#include <set>
#include <functional>
#include <unordered_map>

using namespace std;
using namespace std::chrono;

template <typename K, typename V>
class Cache {
private:
    unordered_map<K, V> cache;
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

    void clear() {
        cache.clear();
    }
};

pair<set<string>, vector<string>> loadInput(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        exit(1);
    }

    string line;
    getline(file, line);
    line.pop_back();
    set<string> towels;
    std::string delimiter = ", ";
    size_t last = 0; 
    size_t next = 0; 
    while ((next = line.find(delimiter, last)) != string::npos) {   
        //cout << line.substr(last, next-last) << endl;   
        towels.insert(line.substr(last, next-last));
        last = next + 2; 
    } 

    getline(file, line);
    vector<string> designs;
    while (getline(file, line)) {
        line.pop_back();
        designs.push_back(line);
    }

    return {towels, designs};
}

string remove_prefix(const string& prefix, const string& word) {
    if (word.rfind(prefix, 0) == 0) {
        return word.substr(prefix.length());
    }
    return word;
}

int check_design(const string& design, const set<string>& towels) {
    if (design == "") {
        return 1;
    }

    int res = 0;
    for (const string& towel : towels) {
        //cout << design << " - " << towel << endl;
        if (design.find(towel, 0) == 0) {
            //cout << " SI" << endl;
            res += check_design(remove_prefix(towel, design), towels);
        }
    }
    //cout << res << endl;
    return res;
}

int part1(const set<string>& towels, const vector<string>& designs) {
    int found = 0;
    for (const string& design : designs) {
        found += (check_design(design, towels) > 0);
    }
    cout << "🎄 Part 1: " << found << endl;
    return found;
}


int part2(const set<string>& towels, const vector<string>& designs) {
    int found = 0;
    Cache<string, int> design_cache([&](const string& d) { return check_design(d, towels); });

    for (const string& design : designs) {
        found += design_cache.get(design);
    }
    design_cache.clear();
    cout << "🎄🎅 Part 2: " << found << endl;
    return found;
}

int main() {
    string title = "Day 19: ";
    string sub = string(title.length() + 2, '-');

    cout << endl;
    cout << " " << title << " " << endl;
    cout << sub << endl;

    auto [towels, designs] = loadInput("input_19.txt");
    
    auto t1_start = high_resolution_clock::now();
    part1(towels, designs);
    auto t1_end = high_resolution_clock::now();
    auto duration1 = duration_cast<microseconds>(t1_end - t1_start);
    cout << duration1.count() / 1000.0 << " ms" << endl;

    // auto t2_start = high_resolution_clock::now();
    // part2(towels, designs);
    // auto t2_end = high_resolution_clock::now();
    // auto duration2 = duration_cast<microseconds>(t2_end - t2_start);
    // cout << duration2.count() / 1000.0 << " ms" << endl;

    return 0;
}