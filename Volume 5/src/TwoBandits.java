/*
task #1409
Difficulty 19
 */
import java.util.Scanner;
public class TwoBandits {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int g = in.nextInt();
        int l = in.nextInt();
        int all = g+l-1;
        System.out.printf("%d %d",all-g,all-l);
    }
}
