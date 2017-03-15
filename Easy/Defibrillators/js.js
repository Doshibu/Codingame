function toFloat (s) {
  return parseFloat(s.replace(',', '.'))
}

var userLng = toFloat(readline())
var userLat = toFloat(readline())

var dist = Infinity
var defib = ''

for (var i = 0, n = readline(); i < n; i++) {
  var data = readline().split(';')
  var name = data[1]
  var lng = toFloat(data[4])
  var lat = toFloat(data[5])

  var x = (userLng - lng) * Math.cos((userLat + lat) / 2)
  var y = (userLat - lat)
  var d = Math.sqrt(x * x + y * y) * 6371

  if (d < dist) {
    dist = d
    defib = name
  }
}

print(defib)
