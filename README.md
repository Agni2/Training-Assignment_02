# Training-Assignment_02

## You are given an integer array A of size N. You can perform the following operation any
number of times:
• Choose any index i and replace A[i] with A[i] + K or A[i] - K, where K is a fixed
integer.
Your goal is to:
• Transform the array such that all elements become equal.
• Return the minimum total number of operations required, or -1 if it is not possible.
### Input Format:
• First line: Integer N
• Second line: N space-separated integers (array A)
• Third line: Integer K
### Output Format:
• Print minimum number of operations or -1
### Constraints:
• 1≤N≤105
• 1≤A[i],K≤109
### Example:
#### Input:
5
2
2 4 6 8 10
#### Output:
6
### Explanation:
Convert all elements to 6:
• 2 → 6 (2 steps)
• 4 → 6 (1 step)
• 6 → 6 (0 steps)
• 8 → 6 (1 step)
• 10 → 6 (2 steps)
Total operations = 6
