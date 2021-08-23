from Gym import Gym
from superUser import superUser
from Member import Member

def menu():
    
    su = superUser()
    member1 = Member()

    flag1 = True
    
    while flag1 == True:
        
        print("\n")
        print("1. Superuser")
        print("2. Member")
        print("3. Exit")
        
        print("\n")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            
            flag2 = True
            
            while flag2 == True:
                
                print("\n")
                print("1. Create member")
                print("2. View member")
                print("3. Update member")
                print("4. Delete member")
                print("5. Create regimen")
                print("6. View regimen")
                print("7. Update regimen")
                print("8. Delete regimen")
                print("9. Go back")
                
                print("\n")
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    
                    su.cre_member()
                    
                if choice == 2:
                    
                    su.vie_member()
                    
                if choice == 3:
                    
                    su.upd_member()
                    
                if choice == 4:
                    
                    su.del_member()
                    
                if choice == 5:
                    
                    su.cre_regimen()
                    
                if choice == 6:
                    
                    su.vie_regimen()
                    
                if choice == 7:
                    
                    su.upd_regimen()
                    
                if choice == 8:
                    
                    su.del_regimen()
                    
                if choice == 9:
                    break

        if choice == 2:
            
            print("\n")
            con_no = input("Enter contact number: ")
            
            flag3 = True
            
            while flag3 == True:

                if con_no not in Gym.member:
                    print("Member doesn't exist")
                    print("\n")
                    break

                bmi = Gym.member[con_no][4]
            
                print("\n")

                print("1. My regimen")
                print("2. My profile")
                print("3. Go back")

                print("\n")
                choice1 = int(input("Enter your choice: "))

                if choice1 == 1:

                    member1.vie_regimen(con_no, bmi)

                if choice1 == 2:
                    
                    member1.vie_profile(con_no)
                    
                if choice1 == 3:
                    
                    break

        if choice == 3:
            break