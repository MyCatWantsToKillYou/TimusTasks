/*
task #1877
Difficulty 21
 */
import java.util.Scanner;
public class BiCodes {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int firstCode=in.nextInt();
        int secondCode=in.nextInt();
        if(firstCode%2==0 || secondCode%2!=0 ){
            System.out.println("yes");
        } else {
            System.out.println("no");
        }
    }
}
