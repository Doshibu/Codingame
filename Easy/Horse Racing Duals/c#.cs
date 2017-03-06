using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        List<int> lList = new List<int>();
        
        String s;
        do {
             s = Console.ReadLine();       
             if(s!=null)
             {
                 int i= int.Parse(s);
                 if(i>0 && i<=10000000) lList.Add(i);
             }
         } while (s != null);
        
        lList= lList.OrderByDescending(i => i).ToList();
        
        int minDiff=int.MaxValue;
        for(int i=0; i<lList.Count; i++)
        {
            if(i==0)
                minDiff=lList[i]-lList[i+1];
            else if(lList[i-1]-lList[i] < minDiff)
                minDiff=lList[i-1]-lList[i];            
        }
        Console.WriteLine(minDiff.ToString());
    }
}