"""
Given the integer day denoting the day number, 
print on the screen which day of the week it is.
Week starts from Monday and for values greater than 7 or less than 1, print Invalid.
Ensure only the 1st letter of the answer is capitalised.
"""

class Solution:
    def whichWeekDay(self, day):
        match day:
            case 1:
                print("monday")
            case 2:
                print("tuesday")
            case 3:
                print("wensday")
            case 4:
                print("thursday")
            case 5:
                print("friday")
            case 6:
                print("saturday")
            case 7:
                print("sunday")
            case _:
                print("invalid day")

Solution_instance=Solution()
Solution_instance.whichWeekDay(9)
            


    
