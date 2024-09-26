def Tasbeeh_Counter():
    count = 0
    while True:
        user_input = input("Enter tap 'd' to count or tap 'e' to reset: ")
        if user_input == "d":
            count +=1
            print(f"count: {count}")
        elif user_input == "e":
            count = 0
            print(f"Count reset to: {count}")
        else:
            print(f"Invalid input, kindly tap 'd' to count or tap 'e' to reset.")

Tasbeeh_Counter()

