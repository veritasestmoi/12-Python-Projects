# string concatenation (how to put strings together)
string that says "subscribe to　＿＿＿"
youtuber = " I'm dead" <!--some string var-->

# a few ways to do this:
print ("subscribe to" + youtuber)
print ("subscribe to{}" .format(youtuber))
print (f"subscribe to {youtuber}") <!--Cleanest way -->

# Output
subscribe to I'm dead
subscribe to I'm dead
subscribe to  I'm dead 