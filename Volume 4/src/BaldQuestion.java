/*
task #1355
Difficulty 229
 */

import java.util.ArrayList;
import java.util.Scanner;
public class BaldQuestion {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ArrayList<Integer> arr = new ArrayList<>();
        int tests = in.nextInt();
        for(int i=tests;i>0;i--){
            int a=in.nextInt();
            int b=in.nextInt();
            if (b % a != 0) {
                arr.add(0);
                continue;
            }
            b /= a;
            int count = 1;
            for (int j = 2; j * j <= b; j++) {
                while (b % j == 0) {
                    b /= j;
                    count++;
                }
            }
            if (b > 1) {
                count++;
            }
            arr.add(count);
        }
        for (Integer anArr : arr) {
            System.out.println(anArr);
        }

    }
}
