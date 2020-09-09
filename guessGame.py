secret = "Bar"
max_tries = 5
user_guess = ""
while user_guess != secret:
    if max_tries == 0:
        print("you loosed !")
        break
    user_guess = input("guess the password:")
    max_tries = max_tries - 1
if user_guess == secret:
    print("Congrats !! you guessed the right word \"" + user_guess + "\"")
    print("Your remaining tries: " + str(max_tries))
