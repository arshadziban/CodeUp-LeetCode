#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

// Custom comparator for sorting
bool compare(pair<char, int>& a, pair<char, int>& b) {
    if (a.second == b.second)
        return a.first < b.first; // Alphabetical if frequency same
    return a.second > b.second;   // Higher frequency first
}

int main() {
    string input;
    cout << "Enter a string: ";
    getline(cin, input);

    map<char, int> freq;

    // Count frequencies (case-sensitive)
    for (char c : input) {
        if (isalpha(c)) {
            freq[c]++;
        }
    }

    // Move to vector for sorting
    vector<pair<char, int>> freqVec(freq.begin(), freq.end());

    // Sort using custom comparator
    sort(freqVec.begin(), freqVec.end(), compare);

    // Build output string
    string result = "";
    for (auto& p : freqVec) {
        result += string(p.second, p.first);
    }

    cout << "Output: " << result << endl;

    return 0;
}
