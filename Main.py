import DoublyLinkedList
import AppConstants

if __name__ == '__main__':
    print("\n\nDoctor Consultation App Started")
    print('_________________________________')

    patients = []
    current_patients = []
    next_patients = []

    """
        Read File, Load Current Patients Record & Create PatientRecord Object
    """
    currentPatientFile = open(AppConstants.CURRENT_PATIENT_FILE_NAME, "r")
    print('\n\n1A. Reading Current Patients From File: \'' + AppConstants.CURRENT_PATIENT_FILE_NAME + '\'')
    print('=============================================================================')
    list = DoublyLinkedList.DoublyLinkedList()
    for patientRow in currentPatientFile:
        patientData = patientRow.rstrip().split(",")
        list.registerPatient(patientData[0].lstrip().rstrip(), patientData[1].lstrip().rstrip())
    currentPatientFile.close()

    """
       Sort Current Patients Based On The Age In Descending Order
    """
    list.sort_queue()

    """
       Write To outputPS5.txt with Refreshed Patient Queue
    """
    print('\n\n1B. After Patient Sorting, Writing To File: \'' + AppConstants.CURRENT_PATIENT_OUTPUT_FILE_NAME + '\'')
    print('=============================================================================')
    current_patient_output_file = open(AppConstants.CURRENT_PATIENT_OUTPUT_FILE_NAME, "w")
    file_content = list.traverse(list.head, True)
    file_content = file_content + "\t----------------------------------"
    print(file_content)
    current_patient_output_file.writelines(file_content)
    current_patient_output_file.close()

    """
        Read File, Load New Patients Record & Create PatientRecord Object
    """
    nextPatientFile = open(AppConstants.NEW_PATIENT_FILE_NAME, "r")
    print('\n\n1C. Reading New Patients From File: \'' + AppConstants.NEW_PATIENT_FILE_NAME + '\'')
    print('=============================================================================')

    all_patients_file = open(AppConstants.ALL_PATIENT_OUTPUT_FILE_NAME, "w")
    all_patients_file.writelines('')
    all_patient_output_file = open(AppConstants.ALL_PATIENT_OUTPUT_FILE_NAME, "a")
    for patientRow in nextPatientFile:
        patientRow = patientRow.lstrip().rstrip()
        if "newPatient:" in patientRow and "," in patientRow:
            validPatientData = patientRow.rstrip().split(":")
            patientData = validPatientData[1].lstrip().rstrip().split(",")
            new_patient = list.registerPatient(patientData[0].lstrip().rstrip(), patientData[1].lstrip().rstrip())
            list.enqueuePatient(new_patient.PatId)
            file_content = "\n\t--------- new patient entered ---------\n" \
                           + "\tPatient details: " \
                           + new_patient.name + ", " + new_patient.age + ", " + new_patient.PatId + "\n"
            list.sort_queue()

            """
               Write To outputPS5.txt with Refreshed Patient Queue
            """
            print('\n\n1B. After Patient Sorting, Writing To File: \''
                  + AppConstants.CURRENT_PATIENT_OUTPUT_FILE_NAME + '\'')
            print('=============================================================================')
            file_content += list.traverse(list.head, False)
            file_content += "\t----------------------------------\n"
            print(file_content)
            all_patient_output_file.writelines(file_content)
        elif patientRow == "nextPatient":
            """
               Write To outputPS5.txt with Refreshed Patient Queue
            """
            print('\n\n3. After Next Patient, Writing To File: \''
                  + AppConstants.CURRENT_PATIENT_OUTPUT_FILE_NAME + '\'')
            print('=============================================================================')
            file_content += list.nextPatient()
            file_content += "\t---------------------------------------------\n"
            print(file_content)
            all_patient_output_file.writelines(file_content)

    all_patient_output_file.close()