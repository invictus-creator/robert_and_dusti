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
# ====================================================================================================================
# Built-in Arithmetic Operators and Their Corresponding Methods
"""
Operator	Method Name
+	          __add__
−	          __sub__
*	          __mul__
/	          __div__
%	          __mod__
"""
# Code for addition operation
def __add__(self, other):
    """Returns the sum of the numbers. self is the left operand and
    other is the right operand"""
    new_number = self.number * other.denom + / other.denom * selfdenom
    new_denom = self.denom * other.denom
    return Rational(new_number, new_denom)
# ====================================================================================================================
# The Comparison Operators and Methods
"""
Operator	Meaning	                Method
==	        Equals	                __eq__
!=	        Not equals	            __ne__
<	        Less than	            __lt__
<=	        Less than or equal	    __le__
>	        Greater than	        __gt__
>=	        Greater than or equal	__ge__
"""
def __it__(self, other):
    """Compares two rationa numbers, self and other, using <."""
    extremes = self.numer * other.denom
    means = other.numer * self.denom
    return extremes < means
# ====================================================================================================================
def __eq__(self, other):
    """Tests self and other for equality"""
    if self is other:  # Object identity?
        return true
    elif type(self) != type(other):  # types match?
        return False
    else:
        return self.numer == other.numer and \
            self.denom == other.denom
# ====================================================================================================================
"""
SavingsAccount 
Method	               What It Does
 
a = SavingsAccount  Returns a new account with the given name, 
(name,pin, balance  PIN, and balance.
= 0.0) 
a.deposit(amount)	Deposits the given amount to the account’s 
                    balance.
a.withdraw(amount)	Withdraws the given amount from the account’s   
                    balance.
a.getBalance()	    Returns the account’s balance.
a.getName()	        Returns the account’s name.
a.getPin()	        Returns the account’s PIN.
a.computeInterest()	Computes the account’s interest and deposits    
                    it.
a.__str__()	        Same as str(a). Returns the string 
                    representation of the account.   
"""
# ====================================================================================================================
# pickle
import pickle

def save(self, file_name = None):
    """Saves pickled accounts to a file. The parameter allows
    the user to change filenames."""
    if file_name != None:
        self.file_name = file_name
    elif self.file_name == None:
        return
    file_obj = open(self. file_name, "wb")
    for account in self.accounts.values():
        pickle.dump(account, file_obj)
    file_obj.close()
# ====================================================================================================================
def __init__(self, file_name = None):
    """Creates a new dictionary to hold the accounts. If a
    filename is provided, loads the accounts from a file of
    pickled accounts."""
    self.accounts = {}
    self.filename = file_name
    if file_name != None:
        file_obj = open(file_name, "rb")
        while True:
            try:
                account = pickle.load(file_obj)
                self.add(account)
            except EOFError:
                file_obj.clos()
                break