#include <vector>
#include <algorithm>

using namespace std;

int firstMissingPositive(vector<int>& nums) {
    int n = nums.size();
    
    // Step 1: Replace negatives and numbers >n with 1 (if 1 doesn't exist, answer is 1)
    bool contains_one = false;
    for (int i = 0; i < n; ++i) {
        if (nums[i] == 1) {
            contains_one = true;
        }
        if (nums[i] <= 0 || nums[i] > n) {
            nums[i] = 1;
        }
    }
    if (!contains_one) return 1;
    
    // Step 2: Use indices as hash keys (mark presence by making nums[val-1] negative)
    for (int i = 0; i < n; ++i) {
        int val = abs(nums[i]);
        if (nums[val - 1] > 0) {
            nums[val - 1] *= -1;
        }
    }
    
    // Step 3: The first positive index + 1 is the missing number
    for (int i = 0; i < n; ++i) {
        if (nums[i] > 0) {
            return i + 1;
        }
    }
    
    // If all numbers from 1 to n are present, return n+1
    return n + 1;
}