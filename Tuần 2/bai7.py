class Candidate:
    def __init__(self, code, name, dob, math_score, literature_score, english_score):
        self.code = code
        self.name = name
        self.dob = dob
        self.math_score = math_score
        self.literature_score = literature_score
        self.english_score = english_score

    def display_info(self):
        print("Candidate Information:")
        print("Code:", self.code)
        print("Name:", self.name)
        print("Date of Birth:", self.dob)
        print("Math Score:", self.math_score)
        print("Literature Score:", self.literature_score)
        print("English Score:", self.english_score)

    @staticmethod
    def test_candidate(candidate):
        total_score = candidate.math_score + candidate.literature_score + candidate.english_score
        if total_score > 15:
            return True
        else:
            return False

# Get the number of candidates from the user
n = int(input("Enter the number of candidates: "))

# Create a list to store the candidates
candidates = []

# Input information for each candidate
for i in range(n):
    print("Candidate", i+1)
    code = input("Enter code: ")
    name = input("Enter name: ")
    dob = input("Enter date of birth: ")
    math_score = float(input("Enter math score: "))
    literature_score = float(input("Enter literature score: "))
    english_score = float(input("Enter english score: "))

    candidate = Candidate(code, name, dob, math_score, literature_score, english_score)
    candidates.append(candidate)

# Test each candidate and display information for those who meet the condition
print("Candidates who meet the condition:")
for candidate in candidates:
    if Candidate.test_candidate(candidate):
        candidate.display_info()