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
        string[] inputs = Console.ReadLine().Split(' ');
        int lightX = int.Parse(inputs[0]);
        int lightY = int.Parse(inputs[1]);
        int thorX = int.Parse(inputs[2]);
        int thorY = int.Parse(inputs[3]);

        while (true)
        {
            int remainingTurns = int.Parse(Console.ReadLine());

            string direction = "";
            if(thorY > lightY) {
                direction = "N";
                thorY--;
            } else if(thorY < lightY ) {
                direction = "S";
                thorY++;
            }
            
            if(thorX > lightX) {
                direction = direction + "W";
                thorX--;
            } else if(thorX < lightX ) {
                direction = direction + "E";
                thorX++;
            }
            Console.WriteLine(direction); 
        }
    }
}