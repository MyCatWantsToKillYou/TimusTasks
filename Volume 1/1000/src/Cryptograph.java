/*
task #1086
Difficulty 114
 */
import java.util.Scanner;
import java.util.ArrayList;

public class Cryptograph {

    public static void main(String[] args) {
        Cryptograph crypt = new Cryptograph();
        Scanner in = new Scanner(System.in);
        int k = in.nextInt();
        int[] arr = new int[k];
        int j=0;
        ArrayList <Integer> simple = new ArrayList<>();
        simple.add(2);
        simple.add(3);
        for(int i = 5;i<163847;i+=2){
            if(crypt.isSimple(i)) {
                simple.add(i);
            }
        }
        while(in.hasNextInt()){
            arr[j]=in.nextInt();
            j++;
        }
        for (int anArr : arr) {
           System.out.println(simple.get(anArr - 1));
       }
    }
    private boolean isSimple(int num){
        boolean simpleNumber=false;
        for(int i=2;i<=Math.sqrt(num);i++){
            if(num%i==0&&i!=num){
                simpleNumber=false;
                return simpleNumber;
            } else {
                simpleNumber=true;
            }
        }
        return simpleNumber;
    }

}
