import AppConstants
import DoublyLinkedList


class PatientRecord:

    def __init__(self, name, age, Pid):
        self.PatId = str(Pid) + str(age)
        self.name = name
        self.age = age
        self.left = None
        self.right = None







