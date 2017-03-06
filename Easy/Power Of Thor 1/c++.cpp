#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int lX; // the X position of the light of power
    int lY; // the Y position of the light of power
    int iTX; // Thor's starting X position
    int iTY; // Thor's starting Y position
    cin >> lX >> lY >> iTX >> iTY; cin.ignore();

    while (1) {
        int remainingTurns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remainingTurns; cin.ignore();
            string action="";
            int x=0;
            int y=0;
            
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
                
                cout << action << endl;
            }
    }
}