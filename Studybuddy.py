import random
import time
import webbrowser
import subprocess

class StudyBuddy:
    def __init__(self):
        self.greetings = ["Hello! Ready to hit the books?", 
                          "Hey there! Let's study together!", 
                          "Good day! Are you prepared for some learning?"]
        self.inspirations = ["You've got this!", 
                             "Every study session gets you closer to your goals!", 
                             "Learning is the key to unlocking your potential!",
                             "Success is the sum of small efforts repeated day in and day out.",
                             "Believe you can, and you're halfway there.",
                             "The only way to do great work is to love what you do.",
                             "The future belongs to those who believe in the beauty of their dreams.",
                             "It always seems impossible until it's done.",
                             "You are capable of more than you know.",
                             "Don't watch the clock; do what it does. Keep going.",
                             "Education is the passport to the future, for tomorrow belongs to those who prepare for it today."]

        self.study_tips = ["Try breaking your study sessions into smaller, manageable chunks.",
                           "Teach someone else the material you're studying. Teaching reinforces learning!",
                           "Use mnemonic devices to remember complex information more easily."]
    
    def greet_user(self):
        print(random.choice(self.greetings))
    
    def inspire(self):
        print(random.choice(self.inspirations))
    
    def offer_study_company(self):
        response = input("Would you like some company while you study? (yes/no): ").lower()
        if response == "yes":
            print("Great! I'll be here to help you out.")
        elif response == "no":
            print("No worries! I'll still be here if you change your mind.")
        else:
            print("Sorry, I didn't catch that. Let me know if you'd like some company.")
            self.offer_study_company()  # Recursive call to handle invalid input
    
    def provide_study_tip(self):
        print("Here's a study tip for you:")
        print(random.choice(self.study_tips))
    
    def ask_study_doubt(self):
        response = input("Do you have any study doubts? (yes/no): ").lower()
        if response == "yes":
            self.answer_study_doubt()
        elif response == "no":
            print("Feel free to ask me anytime if you have any doubts!")
        else:
            print("Sorry, I didn't catch that. Please answer with 'yes' or 'no'.")
            self.ask_study_doubt()  # Recursive call to handle invalid input
    
    def answer_study_doubt(self):
        doubt = input("What's your doubt? ")
        try:
            # Try importing googlesearch library
            import googlesearch
        except ImportError:
            # If googlesearch library is not found, install it
            print("Installing googlesearch library...")
            subprocess.run(["pip", "install", "google"])
            print("googlesearch library installed. Let me search for your doubt.")
            import googlesearch
        
        search_results = googlesearch.search(doubt, num=1, stop=1, pause=2)
        if search_results:
            print(f"Here's what I found: {search_results[0]}")
            webbrowser.open(search_results[0])
        else:
            print("I couldn't find an answer to your doubt. Keep exploring!")

    def study_session(self):
        self.greet_user()
        self.inspire()
        self.offer_study_company()
        self.provide_study_tip()
        self.ask_study_doubt()

# Main function to initiate the study session
def main():
    study_buddy = StudyBuddy()
    study_buddy.study_session()

if __name__ == "__main__":
    main()
