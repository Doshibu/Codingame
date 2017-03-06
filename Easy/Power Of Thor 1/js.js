var init = readline().split(" ");
const LX = parseInt(init[0]);
const LY = parseInt(init[1]);
var TX = parseInt(init[2]);
var TY = parseInt(init[3]);

function moveNORTH()
{
    TY -= 1;
    print('N');
}

function moveNORTH_EAST()
{
    TX -= 1;
    TY -= 1;
    print('NE');
}

function moveEAST()
{
    TX -= 1;
    print('E');
}

function moveSOUTH_EAST()
{
    TX -= 1;
    TY +=1
    print('SE');
}

function moveSOUTH()
{
    TY += 1;
    print('S');
}

function moveSOUTH_WEST()
{
    TX += 1;
    TY += 1;
    print('SW');
}

function moveWEST()
{
    TX += 1;
    print('W');
}

function moveNORTH_WEST()
{
    TX += 1;
    TY -= 1;
    print('NW');
}


while (1) {
    // Read information from standard input
    var E = readline();

    var xaxis = TX - LX;
    var yaxis = TY - LY;
    
    var nextDirectionX = "";
    var nextDirectionY = "";
    
    
    
    if ( xaxis !== 0)
    {
        nextDirectionX  = xaxis < 0 ? "E" : "W";
    }
    if( yaxis !== 0 )
    {
        nextDirectionY  = yaxis < 0 ? "S" : "N";
    }
    
    var nextDirection = nextDirectionY + nextDirectionX;
        
    switch (nextDirection) {
        case "N":
            moveNORTH();
            break;
        case "NE":
            moveNORTH_EAST();
            break;
        case "E":
            moveEAST();
            break;
        case 'SE':
            moveSOUTH_EAST();
            break;
        case 'S':
            moveSOUTH();    
            break;
        case 'SW':
            moveSOUTH_WEST();
            break;
        case 'W':
            moveWEST();
            break;
        case 'NW':
            moveNORTH_WEST();
            break;
        default:
            // code
    }
}