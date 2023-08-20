algo-leetcode:
	sh ./command/daily-commit/leetcode.sh

algo-boj:
	sh ./command/daily-commit/boj.sh

lc-easy:
	sh ./command/leetcode/createFile.sh easy ${problem} ${lang}

lc-medium:
	sh ./command/leetcode/createFile.sh medium ${problem} ${lang}

lc-hard:
	sh ./command/leetcode/createFile.sh hard ${problem} ${lang}

.PHONY: algo-leetcode algo-boj lc-easy lc-medium lc-hard