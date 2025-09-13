import java.util.Scanner;
public class digitSwap {

    public static int digitSwapper(int integer)  throws  Exception{
        if (integer / 100 != 0) {
            throw new Exception("Integer must be 2 digits long");
        }

        Integer firstDigit = integer / 10;
        Integer lastDigit = integer % 10;

        return lastDigit * 10 + firstDigit;
    }

    public static void main(String args[]) throws Exception {
        System.out.println(digitSwapper(-52));
        Scanner myObj = new Scanner(System.in);
        Integer twoDigitNumber = digitSwapper(Integer.valueOf(myObj.nextLine()));
        System.out.println("Reversed digit is: " + twoDigitNumber);
    }
}
