/*
task #1001
Difficulty 16
 */

import java.util.Collections;
import java.util.Scanner;
import java.util.ArrayList;

public class reverseRoot {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        ArrayList <Double> roots = new ArrayList<>();
        while(in.hasNext()){
            long a = in.nextLong();
            double root = Math.sqrt(a);
            roots.add(root);
        }
        Collections.reverse(roots);
        for(Double object:roots){
            System.out.printf("%.4f\n",object);
        }
    }
}
