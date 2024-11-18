
def a():
 displacement = float(input("what is your displacement?"))
 time = float(input("what is your time?"))
 velocity= displacement/time
 print(velocity)

def b():
 length = float(input("what is length?"))
 breadth = float(input("what is breadth?"))
 area= length*breadth
 print(area)

def c():
 mass = float(input("what is your mass?"))
 acceleration = float(input("what is your acceleration?"))
 force= mass*acceleration
 print(force)

def d():
 mass = float(input("what is your mass?"))
 velocity = float(input("what is your velocity?"))
 momentum= mass*velocity
 print(momentum)

def e():
 velocity = float(input("what is your velocity?"))
 time= float(input("what is your time?"))
 displacement= velocity*time
 print(displacement)

def main():
    choice = input("what do you want to do?")
    if choice == "a":
      a()
    elif choice == "b":
      b()
    elif choice =="c":
      c()
    elif choice == "d":
      d()
    elif choice == "e":
      e()
    else:
     input("invalid input")

if __name__ == "__main__":
 main()
