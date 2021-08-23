from Gym import Gym

class Member(Gym):
    
    def __init__(self):
        pass
    
    def vie_regimen(self, bmi):
        
        print("\n")
        
        regimen_1 = sorted(Gym.regimen)
        bmi_1 = 0
        
        for key in regimen_1:
            if (bmi <= key):
                bmi_1 = key
                break
        else:
            print("BMI not in range")
            print("\n")
            return
        
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        
        print("The regimen for bmi {} is:".format(bmi))
        for i in range(7):
            print("{} : {}".format(days[i], Gym.regimen[bmi_1][i]))
        print("\n")
    
    def vie_profile(self, con_no):
        
        print("\n")
        
        if con_no not in Gym.member:
            print("Member doesn't exist")
            print("\n")
            return
        
        print("Name:", Gym.member[con_no][0])
        print("Age:", Gym.member[con_no][1])
        print("Gender:", Gym.member[con_no][2])
        print("Contact no:", con_no)
        print("Email Id:", Gym.member[con_no][3])
        print("BMI", Gym.member[con_no][4])
        print("Membership duration:", Gym.member[con_no][5])
        print("\n")