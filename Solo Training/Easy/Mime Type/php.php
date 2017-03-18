<?php
/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

fscanf(STDIN, "%d",
    $N // Number of elements which make up the association table.
);
fscanf(STDIN, "%d",
    $Q // Number Q of file names to be analyzed.
);

$arr = array();

for ($i = 0; $i < $N; $i++)
{
    fscanf(STDIN, "%s %s",
        $EXT, // file extension
        $MT // MIME type.
    );
    $arr[strtolower($EXT)] = $MT;
}

$FNAME = array();
for ($i = 0; $i < $Q; $i++)
{
    $FNAME[] = stream_get_line(STDIN, 500, "\n"); // One file name per line.
    $tmp = explode(".",$FNAME[$i]);
    $ext[] = array_pop($tmp);

}


for ($i = 0; $i < $Q; $i++)
{
    if (count(explode(".",$FNAME[$i])) > 1)
    {
    if(array_key_exists(strtolower($ext[$i]),$arr))
    {
    echo ($arr[strtolower($ext[$i])]."\n");    
    }
    else echo ("UNKNOWN\n");

    } else echo ("UNKNOWN\n");

}
// Write an action using echo(). DON'T FORGET THE TRAILING \n
// To debug (equivalent to var_dump): error_log(var_export($var, true));
//error_log(var_export(print_r($arr)));
// For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
?>