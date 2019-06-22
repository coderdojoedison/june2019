import requests
already_asked_questions = []

def classify(text):
    key = "bf0ccdb0-2da2-11e9-9bd9-6d74cb2262f9dca94532-bfda-4919-9b85-e581ed9e711e"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def check_if_already_asked( question ):

    if question in already_asked_questions:
        return True

    return False

def answer_question():
    question = input("< ")
    existing_question = check_if_already_asked( question )
    if ( existing_question):
        print("You already asked this question.")
        return "You already asked this question"
    else:
        print("This question has not been asked")
    
    answer = classify(question)
    already_asked_questions.append( question )
    
    answerclass = answer["class_name"]
    confidence = answer["confidence"]
    print("confidence is")
    print(confidence) 
    if confidence < 50:
        print ( "I don't understand.")

    elif answerclass == "food":
        print ("A dolphin's prey varies depending on species and habitat, but all dolphins eat a variety of fish, squid, shrimps, jellyfish, and octopi.")
    elif answerclass == "lifespan":
        print ("In the wild, Orcas can live for up to 70 years and bottlenose dolphins can live for at least 40 years.")
    elif answerclass == "speed":
        print ("Dolphins usually swim about 3 to 7 miles per hour, but they can reach higher speeds of over 20 miles per hour.")
    elif answerclass == "species":
        print("The dolphin family consists of 36 species, making it the most diverse family of the cetacean world. Some species are the Orca, the Bottlenose Dolphin, the Amazon River Dolphin, the Baiji Dolphin, and the Short-beaked Dolphin.")
    elif answerclass == "habitats":
        print("Th habitat of a dolphin depends on its species, but they are found in all oceans of the world and even in a few rivers. The bottlenose dolphin is found in every ocean in the world except the Arctic and Antarctic oceans. Most river dolphins live in the rivers of South American.")
    elif answerclass == "goodbye":
        print ("goodbye, have a nice day!")
        quit() 
print ("What would you like to know about dolphins?") 


while True:
    answer_question() 
