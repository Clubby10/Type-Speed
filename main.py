import time
import random

def typing_speed_test():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "She sells seashells by the seashore.",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "The rain in Spain stays mainly in the plain.",
        "I scream, you scream, we all scream for ice cream.",
        "Peter Piper picked a peck of pickled peppers."
    ]
    print("Welcome to the typing speed test!")
    input("Press enter to start: ")
    random.shuffle(sentences)
    print("Type the following sentences and press enter:")
    for sentence in sentences:
        print(sentence)
        user_input = input().strip()
        start_time = time.time()
        end_time = 0
        while user_input != sentence:
            print("You made a mistake. Please try again.")
            user_input = input().strip()
        end_time = time.time()
        time_taken = end_time - start_time
        correct_chars = 0
        for i in range(min(len(sentence), len(user_input))):
            if sentence[i] == user_input[i]:
                correct_chars += 1
        accuracy = (correct_chars / len(sentence)) * 100
        wpm = len(sentence) / 5 / (time_taken / 60)
        print("Time taken: {:.2f} seconds".format(time_taken))
        print("Accuracy: {:.2f}%".format(accuracy))
        print("Your typing speed is {:.2f} words per minute.".format(wpm))
    print("Congratulations! You have completed the typing speed test.")

typing_speed_test()
