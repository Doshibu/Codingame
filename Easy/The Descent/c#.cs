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
        while (true)
        {
            Dictionary<int, int> key = new Dictionary<int, int>();
            for (int i = 0; i < 8; i++)
            {
                int mountainH = int.Parse(Console.ReadLine());
                key.Add(i, mountainH);
                if(i==7){
                    Console.WriteLine(key.Aggregate((l, r) => l.Value > r.Value ? l : r).Key);
                }
            }
        }
    }
}