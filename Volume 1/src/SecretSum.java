/*
task #1021
Difficulty 141
 */
import java.util.Scanner;


public class SecretSum {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        boolean flag = false;
        boolean[] arr = new boolean[65536];
        int n = in.nextInt();

        for(int i = 0; i<n; i++){
            int number = in.nextInt();
            arr[number+32768] = true;
        }

        n = in.nextInt();

        for(int j=0,x; j<n; j++){
            x = in.nextInt();
            x = 42768 - x;
            if(x>=0 && x<65536 && arr[x]){
                System.out.println("YES");
                flag = true;
                break;
            }
        }

        if (!flag){
            System.out.println("NO");
        }
    }

}
