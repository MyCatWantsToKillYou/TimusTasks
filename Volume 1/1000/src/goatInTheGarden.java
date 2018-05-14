/*
task #1084
Difficulty 147
 */
import java.util.Scanner;
public class goatInTheGarden {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        final double pi = Math.PI;
        double a=in.nextDouble();
        double r=in.nextDouble();
        double D = Math.sqrt(2)*a;
        double S;
        double h = r-(a/2);
        double alpha = 2.0*Math.acos(1-(h/r));
        if((a/2)>=r){
            S=pi*r*r;
            System.out.printf("%.3f\n",S);
        }
        else if((D/2)<=r){
            S=a*a;
            System.out.printf("%.3f\n",S);
        }
        else {
            S=(pi*r*r) - (2*r*r*(pi*Math.toDegrees(alpha)/180 - Math.sin(alpha)));
            System.out.printf("%.3f\n",S);
        }

    }
}
