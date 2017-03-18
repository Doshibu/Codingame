using System;
using System.Linq;

class S
{
    static void Main(string[] args)
    {
        int n=int.Parse(Console.ReadLine());
        int[] T=n>0?Array.ConvertAll(Console.ReadLine().Split(null),s=>int.Parse(s)):new int[] {0};
        int min=T.OrderBy(x=>Math.Abs((long)x-0)).First();
        if(min<0 && T.Contains(min*-1)) min*=-1;
        Console.WriteLine(min);
    }
}
