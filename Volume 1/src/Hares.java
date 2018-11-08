/*
task #1052
Difficulty 223
 */
import java.util.ArrayList;
import java.util.Scanner;

public class Hares {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Hares obj = new Hares();
        int hares = in.nextInt();
        //if(hares==2){
         //System.out.println(hares);
        //}
        ArrayList<Point> pts = new ArrayList<>();
        int maxStraight=0;

        while (in.hasNextInt()) {
            Point hare = new Point();
            hare.X = in.nextInt();
            hare.Y = in.nextInt();
            pts.add(hare);
        }

        for (int i = 0; i < hares; i++) {
            for(int j=1;j<hares;j++) {
                int straightNum=2;
                for (int k = 2; k < hares; k++){
                    if (pts.get(i).X == pts.get(j).X && pts.get(i).Y == pts.get(j).Y  || pts.get(i).X == pts.get(k).X && pts.get(i).Y == pts.get(k).Y || pts.get(j).X == pts.get(k).X && pts.get(j).Y == pts.get(k).Y) {
                        continue;
                    }
                if (obj.isStraight(pts.get(i), pts.get(j), pts.get(k))) {
                    straightNum++;
                }
            }
                if(straightNum>maxStraight) {
                    maxStraight = straightNum;
                }
            }

        }
        System.out.println(maxStraight);
    }

    private boolean isStraight(Point hare,Point hare1, Point hare2) {
        boolean straight;
        straight = (hare.X - hare2.X)*(hare1.Y - hare2.Y) == (hare.Y - hare2.Y) * (hare1.X - hare2.X);
        return straight;
    }
}

class Point {
     int X=0;
     int Y=0;
}
