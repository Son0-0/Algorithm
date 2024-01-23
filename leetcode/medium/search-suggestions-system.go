package main

import (
	"fmt"
	"sort"
)

type TrieNode struct {
	Children   map[rune]*TrieNode
	Suggestion []string
}

type Trie struct {
	Root *TrieNode
}

func Constructor() Trie {
	return Trie{
		Root: &TrieNode{
			Children:   make(map[rune]*TrieNode),
			Suggestion: make([]string, 0),
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
		cur.Suggestion = append(cur.Suggestion, word)
		// sort.Strings(cur.Suggestion)
		// if len(cur.Suggestion) > 3 {
		// 	cur.Suggestion = cur.Suggestion[:3]
		// }
	}
}

func suggestedProducts(products []string, searchWord string) [][]string {
	obj := Constructor()

	for _, product := range products {
		obj.Insert(product)
	}

	result := [][]string{}

	cur := obj.Root
	for _, c := range searchWord {
		if cur != nil {
			cur = cur.Children[c]
		}

		if cur == nil {
			result = append(result, []string{})
		} else {
			// result = append(result, cur.Suggestion)
			sort.Strings(cur.Suggestion)
			if len(cur.Suggestion) > 3 {
				result = append(result, cur.Suggestion[:3])
			} else {
				result = append(result, cur.Suggestion)
			}
		}
	}

	return result
}

func main() {
	fmt.Println(suggestedProducts([]string{"mobile", "mouse", "moneypot", "monitor", "mousepad"}, "mouse"))
}
