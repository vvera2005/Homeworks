def add_quest_or_not():
    ans = input("Do you want to add a question? yes or not: ").lower()
    if ans == "yes":
        return True
    elif ans == "no":
        return False

def check_existence(quest):
    with open("quest.txt","r") as f:
        f_content = f.read()
        if quest in f_content:
            print("This question exist")
            return False
        return True

def adding_question(question, true_answer, false_answer):


    if question[-1] != "?":
        question += "?" 

    with open("quest.txt", "a") as f:    
        f.write(question + true_answer + false_answer+ "\n" )
        
        

def main():
    false_answer = ""
    while add_quest_or_not() == True:
        question = input("Enter your question: ").strip()
        while check_existence(question) == True:
            true_answer = input("Enter the True answer").strip()
            for i in range(3):
                f_ans = input("Enter an False answer: ").strip()
                false_answer += "," + f_ans

            adding_question(question, true_answer, false_answer)
        

main()
