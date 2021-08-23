from Gym import Gym

class superUser(Gym):
    
    def cre_member(self):
        
        tmp_array = []
        
        print("\n")
        try:
            
            tmp_array.append(input("Enter your full name: "))
            tmp_array.append(input("Enter your age: "))
            tmp_array.append(input("Enter your gender: "))
            no = input("Enter your mobile no: ")
            tmp_array.append(input("Enter your email: "))
            tmp_array.append(int(input("Enter your BMI: ")))
            tmp_array.append(int(input("Enter your membership duration: ")))
            print("\n")
            
            if no in Gym.member:
                print("Member already exist")
                print("\n")
                return
            
            Gym.member[no] = tmp_array
            
            print("Member has been created")
            
        except:
            print("\n")
            print("ERROR! Member could not be created")
            
        print("\n")
        
           
    def vie_member(self):
        
        print("\n")
        
        print("Choose out of this members' contact no")
        print(list(Gym.member.keys()))
        
        con_no = input("Enter: ")
        
        if con_no not in Gym.member:
            print("Member doesn't exist")
            print("\n")
            return
        
        print("\n")
        print("Name:", Gym.member[con_no][0])
        print("Age:", Gym.member[con_no][1])
        print("Gender:", Gym.member[con_no][2])
        print("Contact no:", con_no)
        print("Email Id:", Gym.member[con_no][3])
        print("BMI", Gym.member[con_no][4])
        print("Membership duration:", Gym.member[con_no][5])
        print("\n")
        
    
    def del_member(self):
        
        print("\n")
        
        print("Choose out of this members' contact no")
        print(list(Gym.member.keys()))
        
        con_no = input("Enter: ")
        
        if con_no not in Gym.member:
            print("Member doesn't exist")
            print("\n")
            return
        
        del Gym.member[con_no]
        
        print("Member has been deleted")
        print("\n")
    
    def upd_member(self):
        
        print("\n")
        
        print("Choose out of this members' contact no")
        print(list(Gym.member.keys()))
        
        con_no = input("Enter: ")
        
        if con_no not in self.member:
            print("Member doesn't exist")
            print("\n")
            return
        
        try:
            tmp_array = []
            
            tmp_array.append(input("Enter your full name: "))
            tmp_array.append(input("Enter your age: "))
            tmp_array.append(input("Enter your gender: "))
            no = input("Enter your mobile no: ")
            tmp_array.append(input("Enter your email: "))
            tmp_array.append(int(input("Enter your BMI: ")))
            tmp_array.append(int(input("Enter your membership duration: ")))
            print("\n")
            
            if con_no != no and no in Gym.member:
            
                print("Member already exist with similar mobile no")
                print("\n")
                return
            elif con_no != no:
                
                del Gym.member[con_no]
                Gym.member[no] = tmp_array
                
            elif con_no == no:
                
                Gym.member[no] = tmp_array
            else:
                
                print("Some error occured")
                print("\n")
                return
                
            print("\n")

            print("Member details has been updated")
            
        except:
            print("\n")
            print("ERROR! Member detail could not be updated")
            return
            
        print("\n")
        
        if Gym.member[no][5] == 0:
            
            del Gym.member[no]
            print("Since membership is revoked, member is deleted")
        
    
    def cre_regimen(self):
        
        print("\n")
        
        print("List of members")
        print(list(Gym.member.keys()))
        con_no = input("Choose contact number of member for custom regimen: ")
        
        
        if con_no not in Gym.member or con_no in Gym.regimen:
            print("\n")
            print("Either member doesn't exist or custom regimen is already there, please update it")
            print("\n")
            return
        
        regimen_list = []
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        
        try:
            print("\n")
            for i in range(7):
                regimen_list.append(input("{}: ".format(days[i])))
            print("\n")
        except:
            print("\n")
            print("ERROR! Regimen couldn't be created")
            return
                    
        Gym.custom_regimen[con_no] = regimen_list
            
    
    def vie_regimen(self):
        
        print("\n")
        
        regimen_1 = sorted(Gym.regimen)
        bmi_1 = 0
        
        print("View by\n1.Bmi\n2.Contact no")
        opt = int(input("Enter: "))
        
        if opt == 1:
            bmi = int(input("Enter bmi or contact number (10 digits): "))

            for key in regimen_1:
                if (bmi < key and bmi < 30):
                    bmi_1 = key
                    break
            else:
                bmi_1 = 30.01
        
            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        
            print("\n")
            print("The regimen for bmi {} is:".format(bmi))
            for i in range(7):
                print("{} : {}".format(days[i], self.regimen[bmi_1][i]))
            print("\n")
            
        if opt == 2:
            
            con_no = input("Enter contact number: ")
            
            if con_no not in Gym.custom_regimen:
                print("There is no custom regimen for you. Please create it")
                return
            
            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        
            print("\n")
            print("The custom regimen for youis:")
            for i in range(7):
                print("{} : {}".format(days[i], Gym.custom_regimen[con_no][i]))
            print("\n")
        
    
    def del_regimen(self):
        
        print("\n")
        
        print("Available list of members who have custom regimen)")
        print(Gym.custom_regimen)
        
        con_no = input("Enter contact: ")
        
        if con_no not in Gym.custom_regimen:
            print("Regimen doesn't exist")
            print("\n")
            return
        
        del Gym.custom_regimen[con_no]
        
        print("\n")
        print("Member doesn't exist or doesn't have custom regimen, please create it")
        print("\n")
    
    def upd_regimen(self):
        
        print("\n")
        
        print("Available list of members who have custom regimen)")
        print(Gym.custom_regimen.keys(
        ))
        
        con_no = input("Enter contact: ")       
        
        if con_no not in Gym.custom_regimen:
            print("Member doesn't exist or doesn't have custom regimen, please create it")
            print("\n")
            return
        
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        
        try:
            for i in range(7):
                Gym.custom_regimen[con_no][i] = input("{} ".format(days[i]))
            print("\n")
            print("Regimen has been updated")
            print("\n")
        except:
            print("ERROR! Regimen couldn't be updated")
            
            
    
    
            
    
    