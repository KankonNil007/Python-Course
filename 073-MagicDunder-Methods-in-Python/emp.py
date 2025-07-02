class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)
    
    def __str__(self):
        return f"The name of the Employee is {self.name}"
    
    def __repr__(self):
        return f"Employee(\"{self.name}\")"
    
    def __call__(self):
        print("I am calling this class as a Function")