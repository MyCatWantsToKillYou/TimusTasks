/*
task #1044
Difficulty 119
 */

import java.util.Scanner;

public class LuckyTickets {

    public static void main(String[] args)

    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        new LuckyTickets();
        System.out.println(numOfTickets(n));
    }

    private static int numOfTickets(int n) {
        int count = 0;
        int[] arr = new int[n];
        int a = maxNum(n);
        int[] summary = new int[a];
        for (int i = 0; i < summary.length; i++) {
            int div = i;
            int sum = 0;
            for (int j = 0; j < n; j++) {
                arr[j] = div % 10;
                div /= 10;
                sum += arr[j];
                summary[i] = sum;
            }
        }
        for (int i = 0; i < summary.length; i++) {
            for (int j = i; j < summary.length; j++) {
                if (summary[i] == summary[j] && i != j) count += 2;
                else if (i == j) count++;
            }
        }
        return count;
    }
    private static int maxNum(int n){
        if(n%2!=0) return 0;

        switch(n) {
            case 1:
                //return 10;
            case 2:
                return 10;
            case 3:
                //return 100;
            case 4:
                return 100;
            case 5:
                //return 100000;
            case 6:
                return 1000;
            case 7:
                //return 10000000;
            case 8:
                return 10000;
            case 9:
                //return 1000000000;
            default: return 0;
        }
    }
}
