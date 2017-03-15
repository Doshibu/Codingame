// Read inputs from Standard Input (use readline()).
// Write outputs to Standard Output (use print()).

function textToBin (text) {
  var length = text.length
  var output = ''
  for (var i = 0; i < length; i++) {
    var bin = text.charCodeAt(i).toString(2)

    if (bin.length < 7) {
      bin = '0' + bin
    }

    output += bin
  }
  return output
}

var encode = {
  '0': '00',
  '1': '0'
}

var binaryText = textToBin(readline())
var currentSign = binaryText[0]
var output = encode[currentSign] + ' ' + '0'

for (var i = 1; i < binaryText.length; i++) {
  var nextBit = binaryText[i]
  output += (nextBit != currentSign) ? ' ' + encode[nextBit] + ' ' + '0' : '0'
  currentSign = nextBit
}

print(output)
