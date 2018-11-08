/*
task #1068
Difficulty 41
 */
import java.util.Scanner;
public class Sum {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int sum=0;
        if(n==0){System.out.println(1);}
        if(n>0){
            for(int i=1;i<=n;i++){
                sum+=i;
            }
            System.out.println(sum);
        } else if(n<0) {
            for(int i=1;i>=n;i--){
                sum+=i;
            }
            System.out.println(sum);
        }


    }
}
