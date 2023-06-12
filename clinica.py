patients = [{"nome": "Luis", "telefone": "98991842214"}]

def menu():
    print("\n=========Clinica Ágil=========")
    print("[1] Cadastrar paciente")
    print("[2] Marcações de consultas")
    print("[3] Cancelamento de consultas")
    print("[0] Sair")
    print("==============================")

def registerPatient():
    print("Forneça as informações abaixo:")

    patient = {}
    patient["Nome"] = input("Nome do paciente: ").strip().title()
    patient["Telefone"] = input("Telefone do paciente: ").strip()
    print("Paciente cadastrado com sucesso!")

    patients.append(patient)

def listPatients():
    index = 0

    for patient in patients:
        print(f"Paciente: {index}", end=" - ")
        index += 1

        for key, value in patient.items():
          print(f"{key}: {value}", end=" - ")
        print("\n")

def consultationAppointments():
    listPatients()

    print("Selecione o paciente para agendar a consulta")
    option = int(input("Número do paciente: "))


    
while True:
    menu()
    option = int(input("Escolha uma opção: "))

    if option < 0 or option > 3:
        print("Digite uma opção válida!!")

    if option == 1:
        registerPatient()
    
    elif option == 2:
        consultationAppointments()
    
    elif option == 3:
        break
    
    elif option == 0:
        break
