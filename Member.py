from Gym import Gym

class Member(Gym):
    
    def __init__(self):
        pass
    
    def vie_regimen(self, con_no, bmi):
        
        print("\n")
        
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        
        if con_no in Gym.custom_regimen:
            print("Your custom regimen is")
            for i in range(7):
                print("{} : {}".format(days[i], Gym.custom_regimen[con_no][i]))
            print("\n")
            return
            
        
        regimen_1 = sorted(Gym.regimen)
        bmi_1 = 0
        
        for key in regimen_1:
            if (bmi < key and bmi <30):
                bmi_1 = key
                break
        else:
            bmi_1 = 30.01
        
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