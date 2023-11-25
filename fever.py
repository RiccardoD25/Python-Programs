def fever():
    temperature=float(input("Which is your corporal tempreature? :"))
    if temperature>=98.6:
        print("You might have fever")
        print("You should rest")
    if temperature==98.6:
        print("You are happy and healthy")
        print("Keep it that way")
    print("Health check for fever ended")
fever()
