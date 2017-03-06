<?php
fscanf(STDIN, "%d %d %d %d",
    $lX, // the X position of the light of power
    $lY, // the Y position of the light of power
    $iTX, // Thor's starting X position
    $iTY // Thor's starting Y position
);

while (TRUE)
{
    fscanf(STDIN, "%d",
        $remainingTurns // The remaining amount of turns Thor can move. Do not remove this line.
    );

    $action = "";
    $x = 0;
    $y = 0;
            
    while($iTX!=$lX || $iTY!=$lY)
    {
        $x=$lX - $iTX;
        $y=$lY - $iTY;
        $action="";
                
        if($y<0)
        {
            $iTY--;
            $action="N";
        }
        else if($y>0)
        {
            $iTY++;
            $action="S";
        }
                
        if($x<0)
        {
            $iTX--;
            $action.="W";
        }
        else if($x>0)
        {
            $iTX++;
            $action.="E";
        }                               
        echo($action."\n");    
    }
}   
?>