# The Student Class Example
"""
     Student Method	              What It Does
s = Student(name, number)	Returns a Student object with the
given name and number of scores. Each score is initially 0.

s.getName()	                Returns the student’s name.
s.getScore(i)	            Returns the student’s ith score, i
must range from 1 through the number of scores.

s.setScore(i, score)	    Resets the student’s ith score to
score, i must range from 1 through the number of scores.
s.getAverage()	            Returns the student’s average score.
s.getHighScore()	        Returns the student’s highest score.
s.__str()__	Same as str(s). Returns a string representation of
the student’s information.
"""
from student import Student
s = Student("Mary", 5)
print(s)
"""
Name: Mary
Scores: 0 0 0 0 0
"""
s.setScore(1, 100)
print(s)
"""
Name: Maria
Scores: 100 0 0 0 0
"""
s.getHighScore()
"""100"""
s.getAverage()
"""20"""
s.getScore(1)
"""100"""
s.getName()
"""'Maria'"""

# Class syntax
"""
class <class name>(<parent class name>):
    <method definition-1>
    ....
    <method definition-n>
"""


class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))
