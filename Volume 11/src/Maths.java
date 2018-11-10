/*
task #2001
Difficulty 25
 */
import java.util.Scanner;
public class Maths {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a1=in.nextInt();
        int b1=in.nextInt();
        in.nextInt();
        int b2=in.nextInt();
        int a3=in.nextInt();
        in.nextInt();
        System.out.printf("%d %d",a1-a3,b1-b2);
    }
}
