flashcard = [] 

def add():
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    print('\n')
    flashcard.append({"question": question, "answer": answer})  # Append as dictionary

    print("The flashcard has been added successfully!\n")


def review():
    if not flashcard:
        print("No flashcards available to review.\n")
        return
    
    for flash in flashcard: 
        print(f"Question: {flash['question']}")
        input("Press Enter to reveal the answer...")
        print(f"Answer: {flash['answer']}\n")


while True:
    print("1. Add Flashcard")
    print("2. Review Flashcards")
    print("3. Exit")

    try:
        user = int(input("Enter your option: "))
        
        if user == 1:
            add()
        elif user == 2:
            review()
        elif user == 3:
            print("Goodbye! \n")
            break
        else:
            print("Invalid option, please choose again.\n")
    
    except ValueError:
        print("Please enter a valid number.\n")
