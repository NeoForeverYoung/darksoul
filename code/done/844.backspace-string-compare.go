/*
 * @lc app=leetcode id=844 lang=golang
 *
 * [844] Backspace String Compare
 */

// @lc code=start

// TODO官方题解还有另外的解法
package main

func backspaceCompare(s string, t string) bool {
	return getCleanStr(s) == getCleanStr(t)
}

func getCleanStr(s string) string {
	result := make([]byte, len(s))
	slow := 0
	for fast := 0; fast < len(s); fast++ {
		if s[fast] != '#' {
			result[slow] = s[fast]
			slow++
		} else {
			if slow > 0 {
				slow--
			}
		}
	}
	return string(result[:slow])
}

/*
func main() {
	fmt.Printf("%s\n", getCleanStr("a#c"))
}
*/

// @lc code=end
