package main

type TrieNode struct {
	Children map[rune]*TrieNode
	IsEnd    bool
}

type Trie struct {
	Root *TrieNode
}

func Constructor() Trie {
	return Trie{
		Root: &TrieNode{
			Children: make(map[rune]*TrieNode),
			IsEnd:    false,
		},
	}
}

func (this *Trie) Insert(word string) {
	cur := this.Root

	for _, r := range word {
		if _, e := cur.Children[r]; !e {
			cur.Children[r] = &TrieNode{
				Children: make(map[rune]*TrieNode),
			}
		}
		cur = cur.Children[r]
	}

	cur.IsEnd = true
}

func (this *Trie) Search(word string) bool {
	cur := this.Root

	for _, r := range word {
		if _, e := cur.Children[r]; !e {
			return false
		}

		cur = cur.Children[r]
	}

	return cur.IsEnd
}

func (this *Trie) StartsWith(prefix string) bool {
	cur := this.Root

	for _, r := range prefix {
		if _, e := cur.Children[r]; !e {
			return false
		}

		cur = cur.Children[r]
	}

	return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
