#Credits: @rinnyanneko
print("Simple Temperature Converter")
print("Made by: @rinnyanneko")
print("Version: 1.0")
print("\n\n\n\n\n") # 5 new lines
#mode selection
print("Please enter mode: ")
print("Celsius to Fahrenheit (c2f)")
print("Fahrenheit to Celsius (f2c)")
mode = input()
#temperature conversion
if mode == "c2f":
    print("Please enter temperature in Celsius: ")
    temp = input()
    temp = int(temp)
    print (("Temperature in Fahrenheit: "), temp * 1.8 + 32)
elif mode == "f2c":
    print ("Please enter temperature in Fahrenheit: ")
    temp = input()
    temp = int(temp)
    print (("Temperature in Celsius: "), (temp - 32) / 1.8)
print("Press any key to exit")
input()
