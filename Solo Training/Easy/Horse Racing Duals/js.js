var N = parseInt(readline())
var list = []
for (var i = 0; i < N; i++) {
  var pi = parseInt(readline())
  if (pi > 0 && pi !== null) list.push(pi)
}

list.sort(function (a, b) {
  return a - b
})

var minDiff = list[1] - list[0]
for (var i = 1; i < list.length; i++) {
  var diff = list[i] - list[i - 1]
  if (diff < minDiff) minDiff = diff
}
print(minDiff)
