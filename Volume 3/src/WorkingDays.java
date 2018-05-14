/*
task #1264
Difficulty 26
 */
import java.util.Scanner;
public class WorkingDays {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n=in.nextInt();
        int m=in.nextInt();
        int count = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<=m;j++) {
                count++;
            }
        }
        System.out.println(count);
    }
}
