package main

import "fmt"

type TrieNode struct {
	Children map[rune]*TrieNode
	IsEnd    bool
}

type WordDictionary struct {
	Root *TrieNode
}

func Constructor() WordDictionary {
	return WordDictionary{
		Root: &TrieNode{
			Children: make(map[rune]*TrieNode),
			IsEnd:    false,
		},
	}
}

func (this *WordDictionary) AddWord(word string) {
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

func (this *WordDictionary) Search(word string) bool {
	var helper func(int, *TrieNode) bool

	helper = func(index int, cur *TrieNode) bool {
		if index == len(word) {
			return cur.IsEnd
		}

		target := rune(word[index])

		if target == '.' {
			for key := range cur.Children {
				if helper(index+1, cur.Children[key]) {
					return true
				}
			}
			return false
		} else {
			if _, e := cur.Children[target]; !e {
				return false
			}

			return helper(index+1, cur.Children[target])
		}
	}

	return helper(0, this.Root)
}

func main() {
	obj := Constructor()
	obj.AddWord("word")
	fmt.Println(obj.Search("word"))
	fmt.Println(obj.Search(".o.d"))
}
