using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Player
{
    static void Main(string[] args)
    {
        string[] inputs;
        inputs = Console.ReadLine().Split(' ');
        int W = int.Parse(inputs[0]); // width of the building.
        int H = int.Parse(inputs[1]); // height of the building.
        int N = int.Parse(Console.ReadLine()); // maximum number of turns before game over.
        inputs = Console.ReadLine().Split(' ');
        int X0 = int.Parse(inputs[0]);
        int Y0 = int.Parse(inputs[1]);

        int xa=0, ya=0, xz=W-1, yz=H-1;

        while (true)
        {        
            while(N>0)
            {
                string bombDir = Console.ReadLine(); // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
                
                if(bombDir.Contains("R"))
                    xa=X0+1;
                
                if(bombDir.Contains("L"))
                    xz=X0-1;
                
                if(bombDir.Contains("D"))
                    ya=Y0+1;
                    
                if(bombDir.Contains("U"))
                    yz=Y0-1;
                    
                X0 = ((xz-xa)/2) + xa;
                Y0 = ((yz-ya)/2) + ya;                
                Console.WriteLine(X0+" "+Y0);
            }
        }
    }
}