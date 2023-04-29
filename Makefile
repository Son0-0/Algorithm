algo:
	sh daily-commit.sh

lc-easy:
	echo "make lc-easy 'problem'"
	sh leetcode.sh easy ${problem}

lc-medium:
	echo "make lc-medium 'problem'"
	sh leetcode.sh medium ${problem}

lc-hard:
	echo "make lc-hard 'problem'"
	sh leetcode.sh hard ${problem}

.PHONY: algo lc-easy lc-medium lc-hard