

class User:

    def login(self):
        print('Login')

    def registraton(self):
        print('Registration')


class Student(User):
                         # Student Inheritaning all method of user class
    def enroll(self):
        print('Enroll')

    def review(self):
        print('Review')

s = Student()

s.login()
s.registraton()
s.enroll()
s.review()