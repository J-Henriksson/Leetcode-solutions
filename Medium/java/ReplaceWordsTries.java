package Medium.java;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEnd = false;
}

class Trie {
    private final TrieNode root;

    public Trie() {
        root = new TrieNode();
    }


    public void insert(String word) {
        TrieNode current = root;
        for (char ch : word.toCharArray()) {
            if (!current.children.containsKey(ch)) {
                current.children.put(ch, new TrieNode());
            }
            current = current.children.get(ch);
        }

        current.isEnd = true;
    }

    public String getRoot(String word) {
        TrieNode current = root;
        StringBuilder root = new StringBuilder();

        for (char ch : word.toCharArray()) {
            if (!current.children.containsKey(ch)) {
                return word;
            }
            root.append(ch);
            if (current.children.get(ch).isEnd) {
                break;
            }
            current = current.children.get(ch);
        }

        return root.toString();
    }
}






public class ReplaceWordsTries {

    public String replaceWords(List<String> dictionary, String sentence) {
        return rootReplacer(dictionary, sentence);
    }

    public String rootReplacer(List<String> dictionary, String sentence) {
        Trie trie = new Trie();
        StringBuilder newSentence = new StringBuilder();

        for (String root : dictionary) {
            trie.insert(root);
        }
        for (String word : sentence.split(" ")) {
            newSentence.append(trie.getRoot(word) + " ");
        }
        newSentence.deleteCharAt(newSentence.length() - 1);

        return newSentence.toString();
    }


    public static void main(String[] args) {
        ReplaceWords replacer = new ReplaceWords();
        ReplaceWordsTries replacerTries = new ReplaceWordsTries();

        List<String> dictionary = new ArrayList<>(
            List.of(
                "a", "aa", "aaa", "aaaa"
            )
        );

        String sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa";

        System.out.println(replacer.wordReplacer(dictionary, sentence));
        System.out.println(replacer.rootReplacer(dictionary, sentence));
        System.out.println(replacerTries.replaceWords(dictionary, sentence));
    }
}
