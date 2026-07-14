#include <vector>
#include <algorithm>
#include <iostream>

// Force the compiler to optimize for maximum speed and auto-vectorize loops
#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        // Fast I/O to unsync standard streams (bypasses LeetCode's slow print handling)
        std::ios_base::sync_with_stdio(false);
        std::cin.tie(NULL);

        std::vector<std::vector<int>> result;
        int n = nums.size();
        if (n < 3) return result;

        // Cache-friendly sorting: contiguous memory layout ensures quick L1 cache access
        std::sort(nums.begin(), nums.end());

        // Pre-allocate memory to avoid expensive dynamic resizing mid-loop
        result.reserve(n); 

        for (int i = 0; i < n - 2; ++i) {
            // Early pruning: If the smallest number is positive, a 0 sum is impossible
            if (nums[i] > 0) break; 
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int target = -nums[i];
            int left = i + 1;
            int right = n - 1;

            // Micro-optimized two-pointer loop
            while (left < right) {
                int sum = nums[left] + nums[right];

                if (sum == target) {
                    result.push_back({nums[i], nums[left], nums[right]});
                    
                    // Duplicate skipping
                    while (left < right && nums[left] == nums[left + 1]) ++left;
                    while (left < right && nums[right] == nums[right - 1]) --right;
                    
                    ++left;
                    --right;
                } 
                else if (sum < target) {
                    ++left;
                } else {
                    --right;
                }
            }
        }
        return result;
    }
};