from employee import Employee

class Tester(Employee):
    def run_tests(self):
        print(f"{self.name} is running tests...")
        print("All tests are done!")

employee1 = Tester("John Doe", 30, 8566)
employee1.run_tests()