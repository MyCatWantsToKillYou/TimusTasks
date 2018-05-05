/*
task #1014
Difficulty 103
 */

import java.util.Collections;
import java.util.Scanner;
import java.util.ArrayList;

public class multiplex {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int num=in.nextInt();
        ArrayList<Integer> digit = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        if(num==0){
            System.out.println(10);
            return;
        }
        if(num>=1&&num<=9){
            System.out.println(num);
            return;
        }
        int n=num;
        for(int i=9;i>1;--i){
            while(num%i==0){
                num/=i;
                digit.add(i);
            }
        }
        int mul=1;
        for (Integer aDigit1 : digit) {
            mul *= aDigit1;
        }
        if(mul==n) {
            Collections.reverse(digit);
            for (Integer aDigit : digit) {
                sb.append(aDigit);
            }
        }
        String str = sb.toString();
        if(str.isEmpty()){
            System.out.println(-1);
        } else {
            long total = Long.parseLong(str);
            System.out.println(total);
        }
    }
}
