text = input("Enter some thing (bye to quit): ")
while text != "bye":
    print(text)
    text = input("Enter some thing : ")


while True:
    text = input("Enter some thing (stop to quit): ")
    if text != 'stop':
        print(text)
    else:
        break

