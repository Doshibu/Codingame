<?php
fscanf(STDIN, "%d",$N);
$list = array();
for ($i = 0; $i < $N; $i++){
    fscanf(STDIN, "%d",$Pi);
    if($Pi>0 && $Pi!==NULL) array_push($list, $Pi);
}

sort($list);
$minDiff=$list[0];
for($i=1; $i<count($list); $i++)
{
    $diff=$list[$i]-$list[$i-1];
    if($diff<$minDiff) $minDiff=$diff;
}
echo($minDiff);
?>