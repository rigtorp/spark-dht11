spark-dht11
===========

Spark app to read a [DHT11
sensor](http://www.adafruit.com/products/386) and publish humidity and
temperature as Spark variables.

I got the [Spark Core device](https://www.spark.io/) from the
[Kickstarter project](https://www.kickstarter.com/projects/sparkdevices/spark-core-wi-fi-for-everything-arduino-compatible)
and this is my first project.

![](https://raw.github.com/rigtorp/spark-dht11/master/hardware.jpg =250x)

[The circuit is a DHT11 connected to 3v3, GND and a data
pin](https://raw.github.com/rigtorp/spark-dht11/master/hardware.jpg). I
use the internal pullup on the data pin.

I noticed a lot of people had issues with the DHT sensors and I could
not get the Adafruit library working myself. The [Adafruit
code](https://github.com/adafruit/DHT-sensor-library) is pretty iffy,
requires higher timing resolution than necessary and doesn't support
the internal pullup resistor. So I wrote my own simple version that
uses the internal pullup resistor. It reads the relative humidity and
temperature from a DHT11 sensor every 10 seconds and stores them in
the Spark variables `rh` and `temp` respectively.

There's also a Python script that reads the values every minute and
uploads them to [Xively](https://xively.com/).



