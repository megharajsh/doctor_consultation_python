import PatientRecord
import AppConstants


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    # Define the push method to add elements at the beginning
    def push(self, patient):
        patient_node = patient
        patient_node.right = self.head
        if self.head is not None:
            self.head.left = patient_node
        self.head = patient_node
        return patient_node

    # Define the append method to add elements at the end
    def append(self, patient):
        patient_node = patient
        patient_node.right = None
        if self.head is None:
            patient_node.left = None
            self.head = patient_node
            return
        last = self.head
        while last.right is not None:
            last = last.right
        last.right = patient_node
        patient_node.left = last
        return

    def registerPatient(self, name, age):
        new_node = PatientRecord.PatientRecord(name, age, AppConstants.PATIENT_ID_NUMBER + 1)
        AppConstants.PATIENT_ID_NUMBER = AppConstants.PATIENT_ID_NUMBER + 1
        print("\tSuccessfully Registered The Patient - " + new_node.name + ", " + new_node.age + ", " + new_node.PatId)
        self.append(new_node)
        return new_node

    def sort_queue(self):
        if self.head and self.head.right:
            i = self.head
            while i.right:
                selected = i
                j = i.right
                while j:
                    if j.age > selected.age:
                        selected = j
                    j = j.right
                if not selected == i:
                    temp1 = i.name
                    temp2 = i.age
                    temp3 = i.PatId
                    i.age = selected.age
                    i.name = selected.name
                    i.PatId = selected.PatId
                    selected.name = temp1
                    selected.age = temp2
                    selected.PatId = temp3
                i = i.right

    def traverse(self, node, current_patient_queue):
        patientContent = ""
        pointer = node
        patient_count = 0
        while pointer is not None:
            patientContent += "\t" + pointer.PatId + ', ' + pointer.name + '\n'
            pointer = pointer.right
            patient_count += 1
            if current_patient_queue is True:
                file_content = "\t--------- Initial Queue ---------\n" \
                               + "\tNo of patients added: " + str(patient_count) + "\n" \
                               + "\tRefreshed Queue:\n"
            else:
                file_content = "\tRefreshed Queue:\n"
        file_content += patientContent
        return file_content

    def nextPatient(self):
        pointer = self.head
        fileContent = "\t-------------next patient --------------\n"
        fileContent += "\t Next patient for consultation is: " + pointer.PatId + ", " + pointer.name + "\n"
        self.dequeuePatient(pointer.PatId)
        return fileContent

    def enqueuePatient(self, PatId):
        print("Execute Enqueue")

    def dequeuePatient(self, PatId):
        """
           Remove The Patient From Queue
        """
        elem = self.find(PatId)
        print('\t\t4. Remove The Patient From Queue: \''
              + elem.name + '\'')
        if not elem:
            return
        self.remove_elem(elem)

    def remove_elem(self, node):
        """
        Unlink an element from the list.
        Takes O(1) time.
        """
        if node.left:
            node.left.right = node.right
        if node.right:
            node.right.left = node.left
        if node is self.head:
            self.head = node.right
        node.left = None
        node.right = None

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.PatId != key:
            curr = curr.right
        return curr