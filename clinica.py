import datetime
import json
import os

patients = []
schedules = []

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
            return
            break

    patients.append(patient)
    print("Paciente cadastrado com sucesso!")

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

def validateDate(data):
    currencyDate = datetime.datetime.now().date()

    formatedDate = datetime.datetime.strptime(data, '%d/%m/%Y').date()
    if formatedDate > currencyDate:
        return False
    else:
        print("Escolha uma data posterior a atual!")
        return True


def consultationAppointments():
    if len(patients) == 0:
        print("Não há pacientes cadastrados!")
        return

    listArray(patients, "pacientes")

    print("Selecione o paciente para agendar a consulta")
    option = int(input("Número do paciente: "))

    if option < 0 or option >= len(patients):
        print("Opção inválida!")
    else: 
        appointment = {}
        appointment["paciente"] = patients[option]["nome"]
        
        run = True

        while run:
            appointment["data"] = input("Digite o data da consulta (dd/mm/aaaa): ")
            run = validateDate(appointment["data"])
            
        appointment["hora"] = input("Digite a hora da consulta (00:00): ")
        appointment["especialidade"] = input("Digite a especialidade: ")

        for scheduling in schedules:
            if scheduling["data"] == appointment["data"] and scheduling["hora"] == appointment["hora"]:
                print("Já existe uma consulta agendada neste horário!")
                break
        else:
            schedules.append(appointment)
            print("Consulta agendada com sucesso!")

        print(schedules)

def cancellationAppointments():
    listArray(schedules, "agendamentos")

    if len(schedules) == 0:
        print("Não há nenhuma consulta agendada!")
        return

    option = int(input("Escolha um agendamento: "))

    for key, value in schedules[option].items():
        if key == "data" or key == "hora":
            print(f"{key.title()}: {value.title()}")

    choose = input("Você deseja cancelar a consulta (s/n): ").strip().lower()

    if choose == "s" or choose == "sim":
        schedules.pop(option)
        print("Ok! Consulta cancelada!")
    elif choose == "n" or choose == 'nao' or choose == "não":
        print("Ok! Consulta continua agendada.")
    else:
        print("Opção inválida! Digite uma opção válida.")

def saveData():
    clinic = {
        "patients": patients,
        "schedules": schedules
    }

    with open('database.json', 'w') as archive:
        json.dump(clinic, archive)

def loadData():
    if os.path.getsize('database.json') == 0:
        patients = []
        schedules = []
        return patients, schedules
    
    with open("database.json", "r") as archive:
        data = json.load(archive)

    patients = data["patients"]
    schedules = data["schedules"]

    return patients, schedules


patients, schedules = loadData()

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
        saveData()
        break