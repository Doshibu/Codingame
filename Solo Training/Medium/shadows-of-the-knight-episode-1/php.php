<?php
fscanf(STDIN, "%d %d",
    $W, // width of the building.
    $H // height of the building.
);
fscanf(STDIN, "%d",
    $N // maximum number of turns before game over.
);
fscanf(STDIN, "%d %d",$X0,$Y0);
$xa=0; $ya=0; $xz=$W-1; $yz=$H-1;

while (TRUE)
{
    fscanf(STDIN, "%s",
        $bombDir // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    );
    
    if(strstr($bombDir, "R"))
        $xa=$X0+1;
                
    if(strstr($bombDir, "L"))
        $xz=$X0-1;
                
    if(strstr($bombDir, "D"))
        $ya=$Y0+1;
                    
     if(strstr($bombDir, "U"))
        $yz=$Y0-1;
                    
    $X0 = (int)(($xz-$xa)/2) + $xa;
    $Y0 = (int)(($yz-$ya)/2) + $ya;                
    echo($X0." ".$Y0."\n");
}
?>