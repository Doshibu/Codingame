<?php
fscanf(STDIN, "%d",
    $N
);
fscanf(STDIN, "%s",
        $best
    );
if($N>1)
{
    for ($i = 0; $i <= $N; $i++)
    {
        fscanf(STDIN, "%s",
            $t
        );
        $a=explode(':', $t);
        $b=explode(':', $best);
        if($a[0]<$b[0]) $best=$t;
        else if($a[0]==$b[0])
            if($a[1]<$b[1]) $best=$t;
            else if($a[1]==$b[1])
                if($a[2]<$b[2]) $best=$t;
    }
}
echo $best;
?>