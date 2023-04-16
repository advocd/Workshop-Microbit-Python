import microbit
import testMartin
from mb_i2c_lcd1602 import LCD1620

rocket = testMartin.myfile.Rocket()
print(rocket.say_my_name())
# l = LCD1620()
# l.puts(rocket.say_my_name())