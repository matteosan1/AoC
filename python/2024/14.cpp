#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <complex>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <chrono>
#include <limits>
#include <iomanip> // For setting precision

using namespace std;
using namespace std::chrono;

using Complex = complex<double>;

// Function to split a string based on a delimiter
vector<string> split(const string& str, char delimiter) {
    vector<string> tokens;
    string token;
    istringstream stream(str);
    while (getline(stream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

pair<vector<Complex>, vector<Complex>> loadInput(const string& filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        exit(1);
    }

    vector<Complex> robots;
    vector<Complex> vels;
    string line;
    while (getline(file, line)) {
        vector<string> parts = split(line, ' ');
        robots.push_back(stod(parts[0].substr(2)) + stod(parts[0].substr(parts[0].find(',') + 1)) * 1i);
        vels.push_back(stod(parts[1].substr(2)) + stod(parts[1].substr(parts[1].find(',') + 1)) * 1i);
    }
    file.close();
    return make_pair(robots, vels);
}


vector<int> quadrants(const vector<Complex>& robots, int xmax, int ymax) {
    vector<int> quadrants(4, 0);
    for (const Complex& r : robots) {
        int q = 0;
        if (r.real() >= xmax / 2.0) q += 1;
        if (r.imag() >= ymax / 2.0) q += 2;
        quadrants[q]++;
    }
    return quadrants;
}

void part1(const vector<Complex>& robots, const vector<Complex>& vels, int xmax, int ymax) {
    vector<Complex> new_robots = robots;
    for (size_t i = 0; i < robots.size(); ++i) {
        new_robots[i] = Complex(fmod((robots[i] + vels[i] * 100.0).real(), xmax), fmod((robots[i] + vels[i] * 100.0).imag(), ymax));
    }
    vector<int> q = quadrants(new_robots, xmax, ymax);
    cout << "🎄 Part 1: " << q[0] * q[1] * q[2] * q[3] << endl;
}

void draw(const vector<Complex>& ps, int xmax, int ymax) {
    for (int y = 0; y < ymax; ++y) {
        for (int x = 0; x < xmax; ++x) {
            Complex pos(x, y);
            int count = count_if(ps.begin(), ps.end(), [&pos](const Complex& p) { return p == pos; });
            if (count != 0) {
                cout << count;
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
}

void part2(vector<Complex> robots, const vector<Complex>& vels, int xmax, int ymax) {
    int seconds = 10403;

    double min_std_x = numeric_limits<double>::infinity();
    double min_std_y = numeric_limits<double>::infinity();
    int christmas_tree = 0;

    for (int second = 1; second <= seconds; ++second) {
        for (size_t i = 0; i < robots.size(); ++i) {
            robots[i] = Complex(fmod((robots[i] + vels[i]).real(), xmax), fmod((robots[i] + vels[i]).imag(), ymax));
        }

        vector<double> x_coords, y_coords;
        for(const auto& r : robots){
            x_coords.push_back(r.real());
            y_coords.push_back(r.imag());
        }

        double std_x = 0.0, std_y = 0.0;
        if(x_coords.size() > 1){
            double sum_x = accumulate(x_coords.begin(), x_coords.end(), 0.0);
            double mean_x = sum_x / x_coords.size();
            for(double x : x_coords) std_x += pow(x - mean_x, 2);
            std_x = sqrt(std_x / x_coords.size());
        }
        if(y_coords.size() > 1){
            double sum_y = accumulate(y_coords.begin(), y_coords.end(), 0.0);
            double mean_y = sum_y / y_coords.size();
            for(double y : y_coords) std_y += pow(y - mean_y, 2);
            std_y = sqrt(std_y / y_coords.size());
        }

        if (std_x <= min_std_x && std_y <= min_std_y) {
            min_std_x = std_x;
            min_std_y = std_y;
            christmas_tree = second;
        }
    }

    vector<Complex> final_robots = robots;
    for (size_t i = 0; i < robots.size(); ++i) {
        final_robots[i] = Complex(fmod((robots[i] + vels[i] * christmas_tree).real(), xmax), fmod((robots[i] + vels[i] * christmas_tree).imag(), ymax));
    }
    draw(final_robots, xmax, ymax);
    cout << "🎄🎅 Part 2: " << christmas_tree << endl;
}

int main() {
    string title = "Day 14: Restroom Redoubt";
    string sub = string(title.length() + 2, '-');

    cout << endl;
    cout << " " << title << " " << endl;
    cout << sub << endl;

    int xmax = 101, ymax = 103;

    auto [robots, vels] = loadInput("input_14.txt");

    auto t1_start = high_resolution_clock::now();
    part1(robots, vels, xmax, ymax);
    auto t1_end = high_resolution_clock::now();
    auto duration1 = duration_cast<milliseconds>(t1_end - t1_start);
    cout << duration1.count() << " ms" << endl;

    auto t2_start = high_resolution_clock::now();
    part2(robots, vels, xmax, ymax);
    auto t2_end = high_resolution_clock::now();
    auto duration2 = duration_cast<milliseconds>(t2_end - t2_start);
    cout << duration2.count() << " ms" << endl;

    return 0;
}