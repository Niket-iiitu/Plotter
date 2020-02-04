import matplotlib.pyplot as plt
from colorama import Fore, init
init()
print(Fore.RED+"Welcome to Plotter v1.0")
print(Fore.BLUE+"Enter the co-ordinate in format 'x y'\nEnter 'BACK' to remove previous value and 'EXIT' when you are completed.")
print(Fore.WHITE, end="")
x=[]
y=[]
while True:
    try: 
        cor=input()
        cor=cor.split(" ")
        if "BACK" in cor:
            x.pop()
            y.pop()
        elif "EXIT" in cor:
            print(Fore.BLUE+"Co-ordinates entered succesfully!"+Fore.WHITE)
            break
        else:
            cor=[int(_) for _ in cor]
    except NameError:
        print(Fore.BLUE+"Please enter numbers."+Fore.WHITE)
    except:
        print(Fore.BLUE+"Wrong Input"+Fore.WHITE)
    finally:    
        try: 
            if "BACK" not in cor and "EXIT" not in cor:
                x.append(cor[0])
                y.append(cor[1])
        except:
            print(Fore.BLUE+"Enter only two numbers with a space in between."+Fore.WHITE)
plt.xlabel(input(Fore.BLUE+"Enter the X-axis label: "+Fore.GREEN))
plt.ylabel(input(Fore.BLUE+"Enter the Y-axis label: "+Fore.GREEN))
print("X:",end="")
print(x)
print("Y:",end="")
print(y)
plt.figtext(0.5, 0.01, input("Enter the caption: "), horizontalalignment='center', fontsize=12)
plt.plot(x,y,marker="o")
plt.show()
                