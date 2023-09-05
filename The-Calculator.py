import math
print("This is a crappy calc for rectangles/squares")
print(("""            (slx)   
       - - - - - - - -
       |             | 
       |             |
  (sly)|      a      |(sly)
       |             |
       |             |
       - - - - - - - - 
            (slx)
    p = slx * 2 + sly * 2"""))
        
choice = input("Please enter what you want to calculate out of: Side Length X (slx), Side Length Y (sly), the Perimeter (p) and the Area (a)\n")
inputChoice1 = input("Please enter what types of information you already have 1 at a time (you need 2 bits of info and dont choose p aswell as a when calculating a side length) \n")
inputChoice2 = input("Please enter a second type of information you have\n")
slxa = "Side Length X = "
slya = "Side Length Y = "
aa = "The Area = "
pa = "The Perimeter = "

if choice == "slx":
    if inputChoice1 == "slx":
        print("you already have the answer then")

    elif inputChoice1 == "sly":
        if inputChoice2 == "slx":
            print("you already have the answer then")
        elif inputChoice2 == "sly":
            print("you already chose this type of info")
        elif inputChoice2 == "p":
            sly = int(input("Please enter Side Length Y:\n"))
            p = int(input("Please enter the perimeter Length:\n"))
            print(slxa, (p-sly-sly)/2)
        elif inputChoice2 == "a":
            sly = int(input("Please enter Side Length Y:\n"))
            a = int(input("Please enter the Area:\n"))
            print(slxa, a/sly)

    elif inputChoice1 == "p":
        if inputChoice2 == "slx":
            print("you already have the answer then")
        elif inputChoice2 == "p":
            print("you already chose this type of info")
        elif inputChoice2 == "sly":
            sly = int(input("Please enter Side Length Y:\n"))
            p = int(input("Please enter the perimeter Length:\n"))
            print(slxa, (p-sly-sly)/2)
        elif inputChoice2 == "a":
            print('You cant get acurately get slx with only a and p')

    elif inputChoice1 == "a":
        if inputChoice2 == "slx":
            print("you already have the answer then")
        elif inputChoice2 == "a":
            print("you already chose this type of info")
        elif inputChoice2 == "p":
            print('You cant get acurately get slx with only a and p')
        elif inputChoice2 == "sly":
            sly = int(input("Please enter Side Length Y:\n"))
            a = int(input("Please enter the Area:\n"))
            print(slxa, a/sly)

elif choice == "sly":
    if inputChoice1 == "sly":
        print("you already have the answer then")

    elif inputChoice1 == "slx":
        if inputChoice2 == "sly":
            print("you already have the answer then")
        elif inputChoice2 == "slx":
            print("you already chose this type of info")
        elif inputChoice2 == "p":
            slx = int(input("Please enter Side Length X:\n"))
            p = int(input("Please enter the perimeter Length:\n"))
            print(slya, (p-slx-slx)/2)
        elif inputChoice2 == "a":
            slx = int(input("Please enter Side Length X:\n"))
            a = int(input("Please enter the Area:\n"))
            print(slya, a/slx)

    elif inputChoice1 == "p":
        if inputChoice2 == "sly":
            print("you already have the answer then")
        elif inputChoice2 == "p":
            print("you already chose this type of info")
        elif inputChoice2 == "slx":
            slx = int(input("Please enter Side Length X:\n"))
            p = int(input("Please enter the perimeter Length:\n"))
            print(slya, (p-slx-slx)/2)
        elif inputChoice2 == "a":
            print('You cant get acurately get sly with only a and p')

    elif inputChoice1 == "a":
        if inputChoice2 == "sly":
            print("you already have the answer then")
        elif inputChoice2 == "a":
            print("you already chose this type of info")
        elif inputChoice2 == "p":
            print('You cant get acurately get sly with only a and p')
        elif inputChoice2 == "slx":
            slx = int(input("Please enter Side Length X:\n"))
            a = int(input("Please enter the Area:\n"))
            print(slya, a/slx)

elif choice == "p":
    if inputChoice1 == "p":
        print("you already have the answer then")

    elif inputChoice1 == "slx":
        if inputChoice2 == "p":
            print("you already have the answer then")
        elif inputChoice2 == "slx":
            print("you already chose this type of info")
        elif inputChoice2 == "sly":
            slx = int(input("Please enter Side Length X:\n"))
            sly = int(input("Please enter the Side Length Y:\n"))
            print(pa, (slx * 2)+(sly * 2))
        elif inputChoice2 == "a":
            slx = int(input("Please enter Side Length X:\n"))
            a = int(input("Please enter the Area:\n"))
            sly = a/slx
            print(pa, (slx * 2)+(sly * 2))

    elif inputChoice1 == "sly":
        if inputChoice2 == "p":
            print("you already have the answer then")
        elif inputChoice2 == "sly":
            print("you already chose this type of info")
        elif inputChoice2 == "slx":
            slx = int(input("Please enter Side Length X:\n"))
            sly = int(input("Please enter the Side Length Y:\n"))
            print(pa, (slx * 2)+(sly * 2))
        elif inputChoice2 == "a":
            sly = int(input("Please enter Side Length Y:\n"))
            a = int(input("Please enter the Area:\n"))
            slx = a/sly
            print(pa, (slx * 2)+(sly * 2))

    elif inputChoice1 == "a":
        if inputChoice2 == "p":
            print("you already have the answer then")
        elif inputChoice2 == "a":
            print("you already chose this type of info")
        elif inputChoice2 == "sly":
            sly = int(input("Please enter Side Length Y:\n"))
            a = int(input("Please enter the Area:\n"))
            slx = a/sly
            print(pa, (slx * 2)+(sly * 2))
        elif inputChoice2 == "slx":
            slx = int(input("Please enter Side Length X:\n"))
            a = int(input("Please enter the Area:\n"))
            sly = a/slx
            print(pa, (slx * 2)+(sly * 2))

elif choice == "a":
    if inputChoice1 == "a":
        print("you already have the answer then")

    elif inputChoice1 == "slx":
        if inputChoice2 == "a":
            print("you already have the answer then")
        elif inputChoice2 == "slx":
            print("you already chose this type of info")
        elif inputChoice2 == "sly":
            slx = int(input("Please enter Side Length X:\n"))
            sly = int(input("Please enter the Side Length Y:\n"))
            print(aa, slx*sly)
        elif inputChoice2 == "p":
            slx = int(input("Please enter Side Length X:\n"))
            p = int(input("Please enter the Perimeter:\n"))
            sly = (p - slx - slx)/2
            print(aa, slx*sly)

    elif inputChoice1 == "sly":
        if inputChoice2 == "a":
            print("you already have the answer then")
        elif inputChoice2 == "sly":
            print("you already chose this type of info")
        elif inputChoice2 == "slx":
            slx = int(input("Please enter Side Length X:\n"))
            sly = int(input("Please enter the Side Length Y:\n"))
            print(aa, slx * sly)
        elif inputChoice2 == "p":
            sly = int(input("Please enter Side Length Y:\n"))
            p = int(input("Please enter the Perimeter:\n"))
            slx = (p - sly - sly)/2
            print(aa, sly * slx)

    elif inputChoice1 == "p":
        if inputChoice2 == "a":
            print("you already have the answer then")
        elif inputChoice2 == "p":
            print("you already chose this type of info")
        elif inputChoice2 == "sly":
            p = int(input("Please enter the Perimeter:\n"))
            sly = int(input("Please enter Side Length Y:\n"))
            slx = (p - sly - sly)/2
            print(aa, sly * slx)
        elif inputChoice2 == "slx":
            p = int(input("Please enter the Perimeter:\n"))
            slx = int(input("Please enter Side Length X:\n"))
            sly = (p - slx - slx)/2
            print(aa, sly * slx)
