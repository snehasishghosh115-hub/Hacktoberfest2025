/*
 * LeetCode Problem: Valid Parentheses (Problem #20)
 * Difficulty: Easy
 * 
 * Problem Description:
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 * determine if the input string is valid.
 * 
 * An input string is valid if:
 * 1. Open brackets must be closed by the same type of brackets.
 * 2. Open brackets must be closed in the correct order.
 * 3. Every close bracket has a corresponding open bracket of the same type.
 * 
 * Examples:
 * Input: s = "()"
 * Output: true
 * 
 * Input: s = "()[]{}"
 * Output: true
 * 
 * Input: s = "(]"
 * Output: false
 * 
 * Input: s = "([)]"
 * Output: false
 * 
 * Input: s = "{[]}"
 * Output: true
 * 
 * Constraints:
 * - 1 <= s.length <= 10^4
 * - s consists of parentheses only '()[]{}'.
 * 
 * Solution Approach:
 * - Use a stack data structure
 * - Push opening brackets onto the stack
 * - When encountering closing bracket, check if it matches the top of stack
 * - Stack should be empty at the end for valid parentheses
 * 
 * Time Complexity: O(n) where n is the length of string
 * Space Complexity: O(n) for the stack in worst case
 * 
 * Author: Hacktoberfest 2025 Contributor
 * Date: October 2025
 */

import java.util.Stack;
import java.util.HashMap;
import java.util.Map;

public class ValidParentheses {
    
    /**
     * Solution 1: Using Stack and HashMap
     * This is the most clean and efficient approach
     * 
     * @param s Input string containing brackets
     * @return true if parentheses are valid, false otherwise
     */
    public static boolean isValid(String s) {
        // Edge case: empty string or odd length string cannot be valid
        if (s == null || s.length() % 2 != 0) {
            return false;
        }
        
        // Create a stack to store opening brackets
        Stack<Character> stack = new Stack<>();
        
        // Map to store matching pairs
        Map<Character, Character> matchingBrackets = new HashMap<>();
        matchingBrackets.put(')', '(');
        matchingBrackets.put('}', '{');
        matchingBrackets.put(']', '[');
        
        // Iterate through each character in the string
        for (char c : s.toCharArray()) {
            // If it's a closing bracket
            if (matchingBrackets.containsKey(c)) {
                // Check if stack is empty or top doesn't match
                if (stack.isEmpty() || stack.pop() != matchingBrackets.get(c)) {
                    return false;
                }
            } else {
                // It's an opening bracket, push to stack
                stack.push(c);
            }
        }
        
        // Stack should be empty for valid parentheses
        return stack.isEmpty();
    }
    
    /**
     * Solution 2: Alternative approach without HashMap
     * Uses simple if-else conditions
     * 
     * @param s Input string containing brackets
     * @return true if parentheses are valid, false otherwise
     */
    public static boolean isValidAlternative(String s) {
        if (s == null || s.length() % 2 != 0) {
            return false;
        }
        
        Stack<Character> stack = new Stack<>();
        
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                // Opening bracket: push to stack
                stack.push(c);
            } else {
                // Closing bracket: check for match
                if (stack.isEmpty()) {
                    return false;
                }
                
                char top = stack.pop();
                
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        
        return stack.isEmpty();
    }
    
    /**
     * Helper method to print test results
     */
    private static void testCase(String s, boolean expected) {
        boolean result = isValid(s);
        String status = (result == expected) ? "✓ PASS" : "✗ FAIL";
        System.out.printf("%s | Input: %-15s | Output: %-5s | Expected: %-5s%n", 
                         status, "\"" + s + "\"", result, expected);
    }
    
    /**
     * Main method with comprehensive test cases
     */
    public static void main(String[] args) {
        System.out.println("=".repeat(70));
        System.out.println("LeetCode #20: Valid Parentheses");
        System.out.println("=".repeat(70));
        
        System.out.println("\nRunning test cases...\n");
        
        // Test cases from problem description
        testCase("()", true);
        testCase("()[]{}", true);
        testCase("(]", false);
        testCase("([)]", false);
        testCase("{[]}", true);
        
        // Additional edge cases
        testCase("", true);                    // Empty string
        testCase("(", false);                  // Single opening bracket
        testCase(")", false);                  // Single closing bracket
        testCase("((", false);                 // Only opening brackets
        testCase("))", false);                 // Only closing brackets
        testCase("(())", true);                // Nested brackets
        testCase("()[]", true);                // Multiple pairs
        testCase("([{}])", true);              // Complex nesting
        testCase("[({})]", true);              // More complex nesting
        testCase("([{()}])", true);            // Very complex nesting
        testCase("((((()))))", true);          // Deep nesting same type
        testCase("([(]))", false);             // Invalid interleaving
        testCase("{[()]}", true);              // Valid complex structure
        testCase("(){}}{", false);             // Extra closing then opening
        
        System.out.println("\n" + "=".repeat(70));
        
        // Performance test
        System.out.println("\nPerformance Test:");
        String longValid = "()".repeat(5000);  // 10000 characters
        long startTime = System.nanoTime();
        boolean result = isValid(longValid);
        long endTime = System.nanoTime();
        double duration = (endTime - startTime) / 1_000_000.0;
        
        System.out.printf("Processed %d characters in %.3f ms%n", 
                         longValid.length(), duration);
        System.out.printf("Result: %s%n", result);
        
        System.out.println("\n" + "=".repeat(70));
        
        // Comparison between two approaches
        System.out.println("\nComparing both implementations:");
        String testStr = "({[]})";
        System.out.println("Test string: " + testStr);
        System.out.println("Method 1 (HashMap): " + isValid(testStr));
        System.out.println("Method 2 (If-Else): " + isValidAlternative(testStr));
        
        System.out.println("\n" + "=".repeat(70));
        System.out.println("All tests completed!");
        System.out.println("=".repeat(70));
    }
}

/*
 * EXPLANATION OF THE SOLUTION:
 * 
 * 1. Stack Data Structure:
 *    - Perfect for this problem because of Last-In-First-Out (LIFO) property
 *    - Opening brackets go in, closing brackets must match the top
 * 
 * 2. Algorithm Steps:
 *    a) Check if string length is odd (immediate false)
 *    b) Iterate through each character:
 *       - Opening bracket → push to stack
 *       - Closing bracket → check if matches top of stack
 *    c) At the end, stack must be empty
 * 
 * 3. Why This Works:
 *    - Opening brackets create "expectations" for future closing brackets
 *    - Stack naturally handles the "most recent unmatched" opening bracket
 *    - Correct order is maintained by stack's LIFO property
 * 
 * 4. Edge Cases Handled:
 *    - Empty string (valid)
 *    - Odd length (always invalid)
 *    - Only opening or only closing brackets
 *    - Mismatched types: (], {), etc.
 *    - Wrong order: ([)]
 *    - Extra brackets: ())(
 * 
 * 5. Complexity Analysis:
 *    - Time: O(n) - single pass through string
 *    - Space: O(n) - stack size in worst case (all opening brackets)
 * 
 * 6. Optimizations:
 *    - Early exit for odd-length strings
 *    - Using HashMap for cleaner matching logic
 *    - Avoiding unnecessary operations
 * 
 * This solution is optimal and commonly used in interviews!
 */
