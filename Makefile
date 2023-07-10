algo-leetcode:
	sh daily-commit-leetcode.sh

algo-boj:
	sh daily-commit-boj.sh

lc-easy:
	echo "make lc-easy 'problem'"
	sh leetcode.sh easy ${problem}

lc-medium:
	echo "make lc-medium 'problem'"
	sh leetcode.sh medium ${problem}

lc-hard:
	echo "make lc-hard 'problem'"
	sh leetcode.sh hard ${problem}

.PHONY: algo-leetcode algo-boj lc-easy lc-medium lc-hard