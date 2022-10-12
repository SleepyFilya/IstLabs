import json

def andParams(*params):
    return all([el == True for el in params])

def eq(param, value):
    if not(param in fact):
        fact[param] = 0
    return fact[param] == value

def set(param, value):
    fact[param] = value
    return fact[param]

def yes_or_no(question):
    answer = ""
    while(answer != "yes" and answer != "no"):
        answer = input(question)
    return answer

def ask_question(question, *values):
    answer = ""
    while all([str(el) != answer for el in values]):
        answer = input(question)
    return answer

def printResult(text):
    print(text)

functions = {"and": andParams, "eq": eq, "set": set, "yes_or_no": yes_or_no, "ask_question": ask_question, "print": printResult}
fact = {"Solution": 0}

def ruleManager(part):
    final_arguments = []
    if(isinstance(part["arg"], str)):
        final_arguments.append(part["arg"])
    else:
        for arg in part["arg"]:
            if not(isinstance(arg, dict)):
                final_arguments.append(arg)
            else:
                final_arguments.append(ruleManager(arg))
    return functions.get(part["func"])(*final_arguments)

def ruleHandler():
    i = 0;
    while(fact["Solution"] == 0 and i < len(data)):
        if (ruleManager(data[i]["left"])):
            ruleManager(data[i]["right"])
        i += 1

with open("Base.json", "r", encoding="utf-8") as rules:
    data = json.load(rules)

ruleHandler()