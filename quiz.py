
from random import randrange


questions = [
    "What is the capital of Albania?",
    "What is the capital of Andorra?",
    "What is the capital of Austria?",
    "What is the capital of Belarus?",
    "What is the capital of Belgium?",
    "What is the capital of Bosnia and Herzegovina?",
    "What is the capital of Bulgaria?",
    "What is the capital of Croatia?",
    "What is the capital of Czech Republic?",
    "What is the capital of Denmark?",
    "What is the capital of Estonia?",
    "What is the capital of Finland?",
    "What is the capital of France?",
    "What is the capital of Germany?",
    "What is the capital of Greece?",
    "What is the capital of Hungary?",
    "What is the capital of Iceland?",
    "What is the capital of Ireland?",
    "What is the capital of Italy?",
    "What is the capital of Kosovo?",
    "What is the capital of Latvia?",
    "What is the capital of Liechtenstein?",
    "What is the capital of Luxembourg?",
    "What is the capital of Macedonia?",
    "What is the capital of Malta?",
    "What is the capital of Moldova?",
    "What is the capital of Monaco?",
    "What is the capital of Montenegro?",
    "What is the capital of Netherlands?",
    "What is the capital of Norway?",
    "What is the capital of Poland?",
    "What is the capital of Portugal?",
    "What is the capital of Romania?",
    "What is the capital of San Marino?",
    "What is the capital of Serbia?",
    "What is the capital of Slovakia?",
    "What is the capital of Slovenia?",
    "What is the capital of Spain?",
    "What is the capital of Sweden?",
    "What is the capital of Switzerland?",
    "What is the capital of Ukraine?",
    "What is the capital of United Kingdom?",
    "What is the capital of Vatican City?"
]


answers = [
    "tirana",
    "andorra la vella",
    "vienna",
    "minsk",
    "brussels",
    "sarajevo",
    "sofia",
    "zagreb",
    "prague",
    "copenhagen",
    "tallinn",
    "helsinki",
    "paris",
    "berlin",
    "athens",
    "budapest",
    "reykjavik",
    "dublin",
    "rome",
    "pristina",
    "riga",
    "vaduz",
    "luxembourg",
    "skopje",
    "valletta",
    "chisinau",
    "monaco",
    "podgorica",
    "amsterdam",
    "oslo",
    "warsaw",
    "lisbon",
    "bucharest",
    "san marino",
    "belgrade",
    "bratislava",
    "ljubljana",
    "madrid",
    "stockholm",
    "bern",
    "kiev",
    "london",
    "vatican city"
]


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

#----the list of objects----
questions_and_answers = []


#----the class which randomly selects questions to ask----
class Raffle:
    objects = []
    def __init__(self):
        while len(self.objects) < (len(questions_and_answers) // 4):
            number = randrange(len(questions_and_answers))
            if len(self.objects) == 0:
                self.objects.append(questions_and_answers[number])
            else:
                already_in_list = False
                for y in range(len(self.objects)):
                    if questions_and_answers[number].question == self.objects[y].question:
                        already_in_list = True
                        break
                if already_in_list == False:
                    self.objects.append(questions_and_answers[number])


#----method that asks questions----
    def quiz(self):
        points = 0
        for text in self.objects:
            answer = input(text.question +"\n")
            if answer.lower() == text.answer:
                points += 1
        print("\n" + str(points) + "/" + str(len(self.objects)) + " correct!")
        if points >= ((len(questions_and_answers) // 4) - 1):
            print("\nExcellent!")


#----main----
for q in range(len(questions)):
    questions_and_answers.append(Question(questions[q], answers[q]))
Raffle().quiz()
