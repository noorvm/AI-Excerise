

def ask_ai(question):
    print("Sending Ai the request...")
    response = "You Asked "+question
    return response

def ask_AI(question, language, style):
    response = question+" in " + language + " using a "+ style +" explanation"

    return response

x = input("Ask Something to AI : ")

res = ask_ai(x)

print(res)

q = input("Question: ")
l = input("Language: ")
s = input("Style: ")

res = ask_AI(q,l,s)
print(res)