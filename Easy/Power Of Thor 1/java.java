import java.util.*;
import java.io.*;
import java.math.*;

class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lX = in.nextInt(); // the X position of the light of power
        int lY = in.nextInt(); // the Y position of the light of power
        int iTX = in.nextInt(); // Thor's starting X position
        int iTY = in.nextInt(); // Thor's starting Y position

        while (true) {
            int remainingTurns = in.nextInt(); // The remaining amount of turns Thor can move. Do not remove this line.
            String action = "";
            int x = 0;
            int y = 0;
            
            while(iTX!=lX || iTY!=lY)
            {
                x=lX - iTX;
                y=lY - iTY;
                action="";
                
                if(y<0)
                {
                    iTY--;
                    action="N";
                }
                else if(y>0)
                {
                    iTY++;
                    action="S";
                }
                
                if(x<0)
                {
                    iTX--;
                    action+="W";
                }
                else if(x>0)
                {
                    iTX++;
                    action+="E";
                }                
                
                System.out.println(action);
            }            
        }
    }
}