text = input()
text = text.lower()
secondText = text.split()
secondText = secondText[0]
secondText = secondText.replace(",","")
if secondText == 'hello':
    print("0$")
elif text[0] == 'h':
    print("20$")
else:
    print("100$")