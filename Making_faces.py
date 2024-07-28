def convert(text):
    print(text.replace(":)", "🙂"))
    print(text.replace(":(", "🙁"))


text = input("Enter your feeling / happy or sad ?")
print(convert(text))
