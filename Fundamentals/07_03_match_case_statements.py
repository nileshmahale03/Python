#match case

color = input("enter color: ")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Caution")
    case "Red":
        print("Stop")
    case _:
        print("Wrong color")


if color == "Green":
    print("Go")
elif color == "Yellow":
    print("Caution")
elif color == "Red":
    print("Stop")
else:
    print("Wrong color") 
