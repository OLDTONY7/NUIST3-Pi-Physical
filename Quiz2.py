import RPi.GPIO as GPIO
import time

# Setup GPIO
GPIO.setmode(GPIO.BCM)
RED_LED = 18    # GPIO pin for red LED
GREEN_LED =17   # GPIO pin for green LED
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)

def quiz():
    print("Welcome to the Python Knowledge Quiz!")
    print("Answer the following questions:")

    # Questions and Answers
    questions = [
        "1) Which of the following is NOT a python data type?\n"
        "a) int\nb) float\nc) rational\nd) string\ne) bool",
        
        "2) Which of the following is NOT a built-in operation in Python?\n"
        "a) +\nb) %\nc) abs()\nd) sqrt()",
        
        "3) In a mixed-type expression involving juts and floats, Python will convert:\n"
        "a) floats to juts\nb) juts to strings\n"
        "c) floats and juts to strings\nd) juts to floats",
        
        "4) The best structure for implementing a multi-way decision in Python is:\n"
        "a) if\nb) if-else\nc) if elif-else\nd) try",
        
        "5) What statement can be executed in the body of a loop to cause it to terminate?\n"
        "a) if\nb) exit\nc) continue\nd) break"
    ] 
    
    answers = ["c", "d", "d", "c", "d"]  # Correct answers
    score = 0

    # Ask questions
    for i in range(len(questions)):
        user_answer = input(questions[i] + "\nYour answer (a/b/c/etc): ").strip().lower()
        
        # Turn off both LEDs before checking answer
        GPIO.output(RED_LED, GPIO.LOW)
        GPIO.output(GREEN_LED, GPIO.LOW)
        
        if user_answer == answers[i]:
            print("Correct!")
            GPIO.output(GREEN_LED, GPIO.HIGH)  # Green LED on for correct answer
            score += 1
        else:
            print("Incorrect! The correct answer is:", answers[i])
            GPIO.output(RED_LED, GPIO.HIGH)    # Red LED on for incorrect answer
        
        time.sleep(1)  # Keep LED on for 1 second
        GPIO.output(RED_LED, GPIO.LOW)
        GPIO.output(GREEN_LED, GPIO.LOW)

    # Provide final score
    print("\nQuiz completed!")
    print(f"You got {score}/{len(questions)} questions correct.")

    # Blink both LEDs based on final score
    for _ in range(score):
        GPIO.output(GREEN_LED, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(GREEN_LED, GPIO.LOW)
        time.sleep(0.3)

try:
    quiz()
finally:
    # Clean up GPIO
    GPIO.cleanup()
