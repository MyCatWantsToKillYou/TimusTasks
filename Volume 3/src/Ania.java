/*
task #1293
Difficulty 18
 */

import java.util.Scanner;
public class Ania {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int panels = in.nextInt();
        int A = in.nextInt();
        int B = in.nextInt();
        System.out.println(2*panels*A*B);
    }
}
