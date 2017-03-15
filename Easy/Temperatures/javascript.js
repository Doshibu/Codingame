    function sortTemperatures (a, b) {
      if (a == b) {
        return 0
      }

      if (Math.abs(a) == Math.abs(b)) {
        return a > 0 ? -1 : 1
      }
      return (Math.abs(a) > Math.abs(b)) ? 1 : -1
    }

    var n = readline()

    if (n == 0) {
      print(0)
    } else {
      var temperatures = readline().split(' ')
      print(temperatures.sort(sortTemperatures)[0])
    }
