'''
 * Given a string s, find the length of the longest substring without repeating
 *  characters.
 *
 * Example 1:
 * Input: s = "abcabcbb"
 * Output: 3
 * Explanation: The answer is "abc", with the length of 3.
 *
 * Example 2:
 * Input: s = "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 *
 * Example 3:
 * Input: s = "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3.
 * Notice that the answer must be a substring, "pwke" is a subsequence
 * and not a substring.
 *
 * Constraints:
 * 0 <= s.length <= 5 * 104
 * s consists of English letters, digits, symbols and spaces.
'''
class LongestSubstring:
    @staticmethod
    def run():
        s1 = "abcabcbb"
        s2 = "bbbbb"
        s3 = "pwwkew"

        result = LongestSubstring.get_max_length_substring(s1)
        print(f"LongestSubstring {s1} result: {result}")

        result = LongestSubstring.get_max_length_substring(s2)
        print(f"LongestSubstring {s2} result: {result}")

        result = LongestSubstring.get_max_length_substring(s3)
        print(f"LongestSubstring {s3} result: {result}")

    @staticmethod
    def get_max_length_substring(input):
        existing = set()
        left = 0
        max_length = 0

        for right in range(len(input)):
            while input[right] in existing:
                existing.remove(input[left])
                left+=1
            existing.add(input[right])
            max_length = max(max_length, right - left + 1)

        return max_length