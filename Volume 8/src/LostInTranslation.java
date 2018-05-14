/*
task #1785
Difficulty 17
 */

import java.util.Scanner;
public class LostInTranslation {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        switch ((1 <= num && num <= 4 ) ? 0 :
                (5 <= num && num <= 9) ? 1 :
                (10 <= num && num <= 19) ? 2 :
                (20 <= num && num <= 49) ? 3 :
                (50 <= num && num <= 99) ? 4 :
                (100 <= num && num <= 249) ? 5 :
                (250 <= num && num <= 499) ? 6 :
                (500 <= num && num <= 999) ? 7 :
                (num>=1000) ? 8 : 8
                ) {
            case 0:
                System.out.println("few");
                break;
            case 1:
                System.out.println("several");
                break;
            case 2:
                System.out.println("pack");
                break;
            case 3:
                System.out.println("lots");
                break;
            case 4:
                System.out.println("horde");
                break;
            case 5:
                System.out.println("throng");
                break;
            case 6:
                System.out.println("swarm");
                break;
            case 7:
                System.out.println("zounds");
                break;
            case 8:
                System.out.println("legion");
                break;
        }
    }
}
