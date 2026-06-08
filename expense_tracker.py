import json
import os
file_name="savelist.json"
def load_data():
    if os.path.exists(file_name):
        with open(file_name,"r") as file:
            return json.load(file)
    
    return []

expense_list = load_data()

def main():
    while True:
        print("1. Add Expense")
        print("2. View All Expense")
        print("3. Exit")
        try:

            user_choice = int(input("Enter choice 1/2/3: "))

        except Exception:
            print("something went wrong")
            continue
        
        if user_choice == 1:
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("you haven'nt enter integer")
                continue
            
            category = input("Enter category: ")
            single_dict = {"amount": amount, "category": category}
            expense_list.append(single_dict)
            with open(file_name,"w") as file:
                json.dump(expense_list,file)
            print("Submitted!")

        elif user_choice == 2:
            if len(expense_list) == 0:
                print("No data")
            else:
                for i in expense_list:
                    print(i["category"], ":", i["amount"], "Tk")
                total=sum(i["amount"] for i in expense_list)
                print("Total:",total,"Tk")
        elif user_choice == 3:
            print("Exit")
            break

        else:
            print("Invalid")

main()
