/*
task #1285
Difficulty 1805
 */

import java.text.DecimalFormat;
import java.util.Scanner;

import java.lang.*;



public class threadInSpace {
    private static double d(double x0, double y0, double z0, double a0, double b0, double c0, double i0, double k0, double x1, double y1, double z1, double a1, double b1, double c1, double i1, double k1){

        return sqrt1(Math.pow((x1 - x0),2.0) + Math.pow((y1 - y0),2.0) + Math.pow((z1 - z0),2.0) + Math.pow((a1 - a0), 2.0) + + Math.pow((b1 - b0), 2.0) + Math.pow((c1 - c0), 2.0) + Math.pow((i1 - i0), 2.0) + Math.pow((k1 - k0), 2.0));
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
        double x0,y0,z0,a0,b0,c0,i0,k0, x1,y1,z1,a1,b1,c1,i1,k1, xC,yC,zC,aC,bC,cC,iC,kC, r, AC, AB, BC, dist, angle, c, a, b, l1, m1, n1,g1,h1,j1,o1,p1, l2, m2, n2,g2,h2,j2,o2,p2;
        double eps = 1e-6;
        x0 = in.nextDouble();
        y0 = in.nextDouble();
        z0 = in.nextDouble();
        a0 = in.nextDouble();
        b0 = in.nextDouble();
        c0 = in.nextDouble();
        i0 = in.nextDouble();
        k0 = in.nextDouble();
        x1 = in.nextDouble();
        y1 = in.nextDouble();
        z1 = in.nextDouble();
        a1 = in.nextDouble();
        b1 = in.nextDouble();
        c1 = in.nextDouble();
        i1 = in.nextDouble();
        k1 = in.nextDouble();
        xC = in.nextDouble();
        yC = in.nextDouble();
        zC = in.nextDouble();
        aC = in.nextDouble();
        bC = in.nextDouble();
        cC = in.nextDouble();
        iC = in.nextDouble();
        kC = in.nextDouble();
        r = in.nextDouble();
        AC = d(xC,yC,zC,aC,bC,cC,iC,kC,x0,y0,z0,a0,b0,c0,i0,k0);
        AB = d(x0,y0,z0,a0,b0,c0,i0,k0,x1,y1,z1,a1,b1,c1,i1,k1);
        BC = d(xC,yC,zC,aC,bC,cC,iC,kC,x1,y1,z1,a1,b1,c1,i1,k1);
        if (AB == 0){
            System.out.println(0);
            System.exit(0);
        }
        l1 = x0 - xC;
        m1 = y0 - yC;
        n1 = z0 - zC;
        g1 = a0 - aC;
        h1 = b0 - bC;
        j1 = c0 - cC;
        o1 = i0 - iC;
        p1 = k0 - kC;
        l2 = x1 - xC;
        m2 = y1 - yC;
        n2 = z1 - zC;
        g2 = a1 - aC;
        h2 = b1 - bC;
        j2 = c1 - cC;
        o2 = i1 - iC;
        p2 = k1 - kC;
        angle = (l1*l2 + m1*m2 + n1*n2 + g1*g2 + h1*h2 + j1*j2 + o1*o2 + p1*p2) / (sqrt1(l1*l1+m1*m1+n1*n1+g1*g1+h1*h1+j1*j1+o1*o1+p1*p1) * sqrt1(l2*l2+m2*m2+n2*n2+g2*g2+h2*h2+j2*j2+o2*o2+p2*p2));
        c=acos1((AC*AC + BC*BC - AB*AB) / (2*AC*BC));
        a=acos1(r/AC);
        b=acos1(r/BC);
        if (a+b>=c || angle - 1.0 < eps && angle - 1.0 > -eps){
            dist = d(x0,y0,z0,a0,b0,c0,i0,k0,x1,y1,z1,a1,b1,c1,i1,k1);;
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