<?php
fscanf(STDIN, "%d",
    $n // the number of temperatures to analyse
);
$tempLib = stream_get_line(STDIN, 256 + 1, "\n"); // the n temperatures expressed as integers ranging from -273 to 5526
$temps = explode(" ", $tempLib);

if($n!=0)
{
    $closestP = 5526;
    $closestN = -273;
    
    for($i=0; $i<$n; $i++)
    {
        $temp = $temps[$i];
        if($temp>0 && $temp<$closestP)
        {
            $closestP = $temp;
        }
        else if($temp<0 && $temp>$closestN)
        {
            $closestN = $temp;
        }          
    }
            
    $castN = $closestN * -1;
    if($closestP == 5526 && $closestN == -273)
    {
        echo $temps[0];
    }
    else if($closestP == $castN || $closestP<$castN)
    {
        echo($closestP);     
    }
    else
    {
        echo($closestN);   
    }
}
else
{
    echo(0);    
}
?>