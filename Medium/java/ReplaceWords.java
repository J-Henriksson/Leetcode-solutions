package Medium;

import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class ReplaceWords {

    public String replaceWords(List<String> dictionary, String sentence) {
        return wordReplacer(dictionary, sentence);
    }






    /**
     * Solution 1
     * Time limit exceeded :(
     * 
     * Replaces all words in a given String if they start with a "root"
     * the exists within a list.
     *
     * Sorts the roots based on length then loops through each root and uses regex to compare each root with the sentence.
     * If a root occurs at the start of any word then the entire word is replaced with the root.
     * 
     * @param dictionary A list of roots to be used when comparing and replacing words from the sentence String.
     * @param sentence A String of text.
     * @return An LinkedList containing the result of the addition.
     */
    public String wordReplacer(List<String> dictionary, String sentence) {
        List<String> roots = new ArrayList<>(dictionary);
        String replacedSentence = sentence;

        Collections.sort(roots, (s1, s2) -> Integer.compare(s1.length(), s2.length()));

        for (int i = 0; i < roots.size(); i++) {
            replacedSentence = replacedSentence.replaceAll("\\b" + roots.get(i) + "\\w*", roots.get(i));
        }

        return replacedSentence;
    }




    

    /**
     * Solution 2
     * Runtime: Beats 38.43% of all users
     * Memory: Beats 83.29% of all users
     * 
     * Replaces all words in a given String if they start with a "root"
     * the exists within a list.
     *
     * (Brute force solution) Splits the sentence into an array containing each word. 
     * Then loops through the entire array and for each word loops through every root and checks
     * if the substring of the word with the same length as the root (starting from the beginning of the word) 
     * matches the root. If the substring matches then the entire word is replaced with the root.
     * The root is only compared with the word is the length of the word is equal or greater than the root.
     * 
     * @param dictionary A list of roots to be used when comparing and replacing words from the sentence String.
     * @param sentence A String of text.
     * @return An LinkedList containing the result of the addition.
     */
    public String rootReplacer(List<String> dictionary, String sentence) {
        String[] sentenceArray = sentence.split(" ");
        String rootedString = "";

        for (int i = 0; i < dictionary.size(); i++) {
            for (int g = 0; g < sentenceArray.length; g++) {
                if (dictionary.get(i).length() <= sentenceArray[g].length()) {
                    if (sentenceArray[g].substring(0, dictionary.get(i).length()).equals(dictionary.get(i))) {
                        sentenceArray[g] = dictionary.get(i);
                    }
                }
            }
        }
        

        for (int i = 0; i < sentenceArray.length - 1; i++) {
            rootedString += sentenceArray[i] + " ";
        }
        rootedString += sentenceArray[sentenceArray.length - 1];

        return rootedString;
    }

    public static void main(String[] args) {
        ReplaceWords replacer = new ReplaceWords();

        List<String> dictionary = new ArrayList<>(
            List.of(
                "a", "aa", "aaa", "aaaa"
            )
        );

        String sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa";

        System.out.println(replacer.wordReplacer(dictionary, sentence));
        System.out.println(replacer.rootReplacer(dictionary, sentence));
    }
}
