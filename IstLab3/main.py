import yaml

def toIdConvert(name):
    for element in data['entity']:
        if element['name'] == name:
            id = element['id']
    return id

def toNameConvert(id):
    for element in data['entity']:
        if element['id'] == id:
            name = element['name']
    return name

def searchConnections(id, connectType):
    search_result = []
    for element in data['connection']:
        if element['parent'] == id and element['connect'] == connectType:
            search_result.append(element['child'])
    if len(search_result) == 0:
        search_result.append("Указанная сущность не поддерживает выбранную связь")
    return search_result

def processing(entity, connect):
    id = entity if "id" in entity else toIdConvert(entity)
    result = searchConnections(id, connect)
    final_answer = {}
    tmp = []
    for element in result:
        if element != "Указанная сущность не поддерживает выбранную связь":
            tmp.append(toNameConvert(element))
        else:
            tmp.append(element)
    final_answer[entity] = tmp
    return final_answer[entity]

def handler(entity, connect):
    result = {}
    result[entity] = processing(entity, connect)
    tmp = result.copy()
    intermediate_result = {}
    end = False
    while not(end):
        for key, value in tmp.items():
            for element in value:
                if element != "Указанная сущность не поддерживает выбранную связь":
                    intermediate_result[element] = processing(element, connect)
        result.update(intermediate_result)
        tmp.clear()
        tmp.update(intermediate_result)
        count = 0
        for key, value in intermediate_result.items():
            count = count + 1 if value == "Указанная сущность не поддерживает выбранную связь" else count
        end = True if count == len(intermediate_result) else False
        intermediate_result.clear()

    print("\nОтвет:")
    for key, value in result.items():
        print(key, ":", end=' ')
        for element in value:
            # if element != "Указанная сущность не поддерживает выбранную связь":
                print(element, end=', ')
        print()

with open("Base.yaml", "r", encoding="utf-8") as strokes:
    data = yaml.safe_load(strokes)

all_entities = []
for element in data['entity']:
    all_entities.append(element['id'])

entity = ""
correct = 0
while correct == 0:
    entity = input("Введите сущность: ")
    for element in data['entity']:
        correct = correct + 1 if element['name'] == entity else correct

correct = 0
while correct == 0:
    connect = input("Введите тип связи: ")
    for element in data['connection']:
        correct = correct + 1 if element['connect'] == connect else correct

handler(entity, connect)
