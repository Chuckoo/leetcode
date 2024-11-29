from collections import Counter

def maximizeProcessingPower(processingPower):
    # Step 1: Count the frequency of each value
    freq = Counter(processingPower)
    
    # Step 2: Create a sorted list of unique values
    unique_values = sorted(freq.keys())
    
    # Step 3: Use dynamic programming to maximize the sum
    n = len(unique_values)
    dp = [0] * n  # dp[i] represents the max sum considering unique_values[:i+1]
    
    for i in range(n):
        current_value = unique_values[i]
        current_sum = current_value * freq[current_value]
        
        if i == 0:
            dp[i] = current_sum
        elif unique_values[i] == unique_values[i - 1] + 1:
            # Adjacent value conflict: choose max of taking or skipping this value
            dp[i] = max(dp[i - 1], current_sum + (dp[i - 2] if i > 1 else 0))
        else:
            # No conflict: simply add current_sum to dp[i-1]
            dp[i] = dp[i - 1] + current_sum
    
    return dp[-1]

# Test cases
print("Test 1 (should be 19):", maximizeProcessingPower([5,5,5,6,6,6]))
