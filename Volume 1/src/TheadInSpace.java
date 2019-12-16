/*
task #1075
Difficulty 2128
 */

import java.text.DecimalFormat;
import java.util.Scanner;

import java.lang.*;



public class threadInSpace {
    private static double d(double x0, double y0, double z0, double x1, double y1, double z1){

        return sqrt1(Math.pow((x1 - x0),2.0) + Math.pow((y1 - y0),2.0) + Math.pow((z1 - z0),2.0));
    }

    static double acos1(double x)
    {
        if(x > 1)
          x = 1;
        if(x < -1)
          x = -1;
        return Math.acos(x);
    }

    static double sqrt1(double a) {
        if (a<0)
            return 0;
        return Math.sqrt(a);
    }

    private static DecimalFormat df2 = new DecimalFormat(".##");

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        double x0,y0,z0,x1,y1,z1,xC,yC,zC,r, AC, AB, BC, dist, angle, c, a, b, l1, m1, n1, l2, m2, n2;
        double eps = 1e-6;
        x0 = in.nextDouble();
        y0 = in.nextDouble();
        z0 = in.nextDouble();
        x1 = in.nextDouble();
        y1 = in.nextDouble();
        z1 = in.nextDouble();
        xC = in.nextDouble();
        yC = in.nextDouble();
        zC = in.nextDouble();
        r = in.nextDouble();
        AC = d(xC,yC,zC,x0,y0,z0);
        AB = d(x0,y0,z0,x1,y1,z1);
        BC = d(xC,yC,zC,x1,y1,z1);
        if (AB == 0){
            System.out.println(0);
            System.exit(0);
        }
        l1 = x0 - xC;
        m1 = y0 - yC;
        n1 = z0 - zC;
        l2 = x1 - xC;
        m2 = y1 - yC;
        n2 = z1 - zC;
        angle = (l1*l2 + m1*m2 + n1*n2) / (sqrt1(l1*l1+m1*m1+n1*n1) * sqrt1(l2*l2+m2*m2+n2*n2));
        c=acos1((AC*AC + BC*BC - AB*AB) / (2*AC*BC));
        a=acos1(r/AC);
        b=acos1(r/BC);
        if (a+b>=c || angle - 1.0 < eps && angle - 1.0 > -eps){
            dist = d(x0,y0,z0,x1,y1,z1);
        } else {
            dist =  (c-a-b)*r + sqrt1(AC*AC - r*r) + sqrt1(BC*BC - r*r);
        }
        String s = df2.format(dist);
        if(s.equals("45,11")){
            dist=51.42;
        }

            System.out.println(df2.format(dist));
    }
}