// Read init information from standard input, if any
const N = parseInt(readline());

var maps = [];
var flatZone = [];

function Point( X, Y )
{
    this.X = X;
    this.Y = Y;
    
    this.toString = function ()
    {
        printErr( "X :" + this.X );
        printErr( "Y :" + this.Y );
    }
}

function MarsLander ( data )
{
    this.X   =  data[0];
    this.Y   =  data[1];
    this.HS  =  data[2];
    this.VS  =  data[3];
    this.F   =  data[4];
    this.R   =  data[5];
    this.P   =  data[6];
    
    this.toString = function () 
    {
        printErr( "X "+ this.X   );
        printErr( "Y "+ this.Y   );
        printErr( "HS"+ this.HS  );
        printErr( "VS"+ this.VS  );
        printErr( "F "+ this.F   );
        printErr( "R "+ this.R   );
        printErr( "P "+ this.P   );
	}
}     

for (var i = 0 ; i < N ; i++ )
{
    var input = readline();
    var coordinates = input.split(' ');
    
    var newPoint = new Point ( parseInt(coordinates[0]) , parseInt(coordinates[1]) );
    
    maps.push( newPoint );
    
    if( ! flatZone.lenght && i > 0 )
    {
        if( newPoint.Y == maps[i - 1].Y )
        {
            flatZone.push( maps[i - 1] );
            flatZone.push( newPoint  );
        }
    }
}


while (1) {
    // Read information from standard input
    var marsLander = new MarsLander (readline().split(' '));
    
    marsLander.toString();
    
    if( marsLander.VS < -36 )
    {
        print('0 4');
    }
    else
    {
        print('0 0');
    }
}