package Easy.java;

import java.util.Map;

public class RomanToInteger {
    
    public int romanToInt(String s) {
        return(romanStringToInt(s));
    }






    /**
     * Solution 1
     * Runtime: Beats 100% of all users
     * Memory: Beats 96.21% of all users
     * 
     * Converts a string representation of roman numerals into an integer.
     *
     * Goes through the string from left to right, uses if statement to compute the
     * corresponding integer for each numeral. And whether they should be subtracted
     * from the next numeral or not.
     * 
     * @param s A String representing roman numerals.
     * @return An integer representation of the roman numerals.
     */
    public int romanStringToInt(String s) {
        int value = 0;
        for (int i = 0; i < s.length(); i++) {
            char numeral = s.charAt(i);
            boolean notLastNumeral = (i != s.length() - 1);

            switch (numeral) {
                case 'I':   
                if (notLastNumeral) {
                    if (s.charAt(i + 1) == 'V') {
                        value += 4;
                        i++;
                    }
                    else if (s.charAt(i + 1) == 'X') {
                        value += 9;
                        i++;  
                    }
                    else {
                        value += 1;
                    }
                }
                else {
                    value += 1;
                }  
                break;
                
                case 'V':
                value += 5;
                break;

                case 'X':
                if (notLastNumeral) {
                    if (s.charAt(i + 1) == 'L') {
                        value += 40;
                        i++;
                    }
                    else if (s.charAt(i + 1) == 'C') {
                        value += 90;
                        i++;  
                    }
                    else {
                        value += 10;
                    }
                }
                else {
                    value += 10;
                }
                break;

                case 'L':
                value += 50;
                break;

                case 'C':
                if (notLastNumeral) {
                    if (s.charAt(i + 1) == 'D') {
                        value += 400;
                        i++;
                    }
                    else if (s.charAt(i + 1) == 'M') {
                        value += 900;
                        i++;  
                    }
                    else {
                        value += 100;
                    }
                }
                else {
                    value += 100;
                }
                break;

                case 'D':
                value += 500;
                break;

                case 'M':
                value += 1000;
                break;
            }
        }

        return value;
    }






    
    private static final Map<Character, Integer> numeralValues = Map.of(
        'I', 1,
        'V', 5,
        'X', 10,
        'L', 50,
        'C', 100,
        'D', 500,
        'M', 1000);

    
    /**
     * Solution 2
     * Runtime: Beats 80.89% of all users
     * Memory: Beats 85.33% of all users
     * 
     * Converts a string representation of roman numerals into an integer.
     * 
     * Goes through the string from right to left. Uses a map to retrieve the corresponding 
     * integer value for each roman character and adds it to the total value. 
     * Stores each value for 1 iteration in the prevValue variable, if the current value
     * is less than the previous value and is at most two roman numerals away from it,
     * the current value is subtracted from the total value.
     * Calculates if the current value is two or less roman numerals away from the previous
     * value (while still being less than it) by checking if it is at most 1/10 less than the previous value.
     * Since each roman numeral is either 2 or 5 times greater than the previous numeral
     * it can at most always be 1/10th less. 
     * 
     *
     * @param s A String representing roman numerals.
     * @return An integer representation of the roman numerals.
     */
    public int romanNumeralConvertor(String s) {
        int value = 0;
        int prevValue = 0;
        for(int i = s.length() - 1; i >= 0; i--) {
            int numWorth = numeralValues.get(s.charAt(i));
            if (numWorth < prevValue && (numWorth * 10 >= prevValue)) {
                value -= numWorth;
            }
            else {
                value += numWorth;
            }
            prevValue = numWorth;
        }

        return value;
    }





    public static void main(String[] args) {
        RomanToInteger romanNumeralConvertor = new RomanToInteger();
        System.out.println(romanNumeralConvertor.romanNumeralConvertor("LVIII"));
    }
}
