class Student:
    def __init__(self, name: str, score1: float, score2: float, score3: float):
        self.name = name
        self.scores = [score1, score2, score3]

    def calculateAverage(self) -> float:
        return sum(self.scores) / len(self.scores)

    def getLetterGrade(self) -> str:
        average = self.calculateAverage()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'


def main():
    print("--- Student Grade System ---")
    name = input("Enter student's name: ")

    scores = []
    for i in range(1, 4):
        while True:
            try:
                score = float(input(f"Enter test score {i} (out of 100): "))
                if score < 0 or score > 100:
                    print("Error: Score must be between 0 and 100.")
                    continue
                scores.append(score)
                break
            except ValueError:
                print("Error: Please enter a valid number.")

    student = Student(name, scores[0], scores[1], scores[2])

    print("\n--- Grade Report ---")
    print(f"Student Name: {student.name}")
    print(f"Average Score: {student.calculateAverage():.2f}")
    print(f"Letter Grade: {student.getLetterGrade()}")


if __name__ == "__main__":
    main()