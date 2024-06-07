


#!/usr/bin/env python3


with open("dracula.txt", "r")  as foo:
    with open("vampiry.txt", "w") as fang:
         for line in foo:
             count = 0
             if "vampire" in line.lower():
                 print(line)
                 count += 1
                 fang.write(line)
            


