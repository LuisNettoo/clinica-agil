patients = [
    {"nome": "Luis", "telefone": "98991842214"},
    {"nome": "Marcos", "telefone": "98991843321"},
    {"nome": "Danilo", "telefone": "98987842214"}
    ]
schedules = [
    {"paciente": "Luis", "dia": "12/07", "hora": "14:50", "especialidade": "Cardiologista"}
]

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
    patient["nome"] = input("Nome do paciente: ").strip().title()
    patient["telefone"] = input("Telefone do paciente: ").strip()

    print(patient["telefone"])

    for i in patients:
        if i.get("telefone") == patient["telefone"]:
            print("Paciente já cadastrado")
            break
        else:
            patients.append(patient)
            print("Paciente cadastrado com sucesso!")
            break

def listArray(list, type):
    index = 0

    for i in list:
        if type == "pacientes":
            print(f"Paciente: {index}", end=" - ")
        elif type == "agendamentos":
            print(f"Agendamento: {index}", end=" - ")
        index += 1

        for key, value in i.items():
          print(f"{key.title()}: {value}", end=" - ")
        print("\n")

def consultationAppointments():
    listArray(patients, "pacientes")

    print("Selecione o paciente para agendar a consulta")
    option = int(input("Número do paciente: "))

    consulta = {}
    consulta['paciente'] = patients[option]["Nome"]
    consulta['dia'] = input("Digite o dia da consulta (dd/mm): ")
    consulta['hora'] = input("Digite a hora da consulta (00:00): ")
    consulta['especialidade'] = input("Digite a especialidade: ")

    schedules.append(consulta)

    print(schedules)

def cancellationAppointments():
    listArray(schedules, "agendamentos")
    

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
        cancellationAppointments()
    
    elif option == 0:
        break
