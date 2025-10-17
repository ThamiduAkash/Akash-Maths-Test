import random
import time

# create_question() function 
def create_question(min_num, max_num):
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)
    operator = random.choice(['+', '-', '*'])
    question = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return question, answer

# ask_question() function 
def ask_question(question, correct_answer):
    start_time = time.time()
    try:
        user_answer = input(f"What is {question}? ")
        user_answer = int(user_answer)  
        end_time = time.time()
        response_time = end_time - start_time
        is_correct = (user_answer == correct_answer)
        return is_correct, response_time
    except ValueError:
        end_time = time.time()
        response_time = end_time - start_time
        return False, response_time  

def main():
    while True:  
        # Requirement 1: Welcome message and difficulty selection
        print("Welcome to Akash's Maths Test!")
        print("Please choose a difficulty: Easy (1/e/easy), Medium (2/m/medium), Hard (3/h/hard), or Custom (4/c/custom)")

        # Requirement 2: Get valid difficulty choice
        while True:
            choice = input("Enter your choice: ").lower()
            if choice in ['1', 'e', 'easy']:
                difficulty = "Easy"
                questions = 5
                max_num = 10
                break
            elif choice in ['2', 'm', 'medium']:
                difficulty = "Medium"
                questions = 10
                max_num = 20
                break
            elif choice in ['3', 'h', 'hard']:
                difficulty = "Hard"
                questions = 15
                max_num = 50
                break
            elif choice in ['4', 'c', 'custom']:
                difficulty = "Custom"
                # Custom difficulty with input validation
                while True:
                    try:
                        questions = int(input("Enter the number of questions (minimum 1): "))
                        if questions < 1:
                            print("Error: Number of questions must be at least 1.")
                            continue
                        max_num = int(input("Enter the maximum number (minimum 2): "))
                        if max_num < 2:
                            print("Error: Maximum number must be at least 2.")
                            continue
                        break
                    except ValueError:
                        print("Error: Please enter valid numbers.")
                break
            else:
                print("Invalid choice. Please select Easy, Medium, Hard, or Custom.")

        print(f"You have selected {difficulty} difficulty.")

        # Initialize score and lists to store results
        score = 0
        correctness = []
        response_times = []
        questions_asked = []

        # Requirement 3: Loop for the specified number of questions
        for i in range(questions):
            print(f"\nScore: {score}")
            print(f"Question {i + 1} of {questions}")

            if i == questions - 1: 
                print("Challenge question!")
                min_num = max_num
                question_max_num = max_num * 2
            else:
                min_num = max_num // 2
                question_max_num = max_num

            question, correct_answer = create_question(min_num, question_max_num)
            questions_asked.append(question)

            # Ask the question
            is_correct, response_time = ask_question(question, correct_answer)
            correctness.append(is_correct)
            response_times.append(response_time)

            points = 0
            if is_correct:
                base_points = 20 if i == questions - 1 else 10
                points = max(1, base_points - int(response_time)) 
                score += points
                point_str = "point" if points == 1 else "points"
                second_str = "second" if int(response_time) == 1 else "seconds"
                print(f"Correct! You took {response_time:.1f} {second_str} and earned {points} {point_str}.")
            else:
                second_str = "second" if int(response_time) == 1 else "seconds"
                print(f"Incorrect. You took {response_time:.1f} {second_str} and earned 0 points.")

        correct_count = sum(correctness)
        percentage_correct = (correct_count / questions) * 100 if questions > 0 else 0
        avg_response_time = sum(response_times) / len(response_times) if response_times else 0

        print("\n=== Test Results ===")
        print(f"Final Score: {score}")
        print(f"Correct Answers: {correct_count}/{questions} ({percentage_correct:.1f}%)")
        print(f"Average Response Time: {avg_response_time:.1f} seconds")

        # Question-by-question breakdown
        print("\n=== Question Breakdown ===")
        for i in range(questions):
            status = "Correct" if correctness[i] else "Incorrect"
            second_str = "second" if int(response_times[i]) == 1 else "seconds"
            print(f"Question {i + 1}: {questions_asked[i]} - {status} ({response_times[i]:.1f} {second_str})")

        # Ask to restart
        restart = input("\nWould you like to start again? (y/yes to continue, anything else to exit): ").lower()
        if restart not in ['y', 'yes']:
            print("Thank you for playing Kavi's Maths Test!")
            break

if __name__ == "__main__":
    main()
