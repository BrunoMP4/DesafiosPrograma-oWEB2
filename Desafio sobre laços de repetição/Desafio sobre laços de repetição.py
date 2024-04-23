def calcular_reajuste(salario):
    if salario <= 280:
        percentual_aumento = 20
    elif salario <= 700:
        percentual_aumento = 15
    elif salario <= 1500:
        percentual_aumento = 10
    else:
        percentual_aumento = 5
    
    aumento = salario * (percentual_aumento / 100)
    novo_salario = salario + aumento
    
    # Considerando a inflação de 3.8%
    inflacao = 3.8 / 100
    aumento_real = aumento - (aumento * inflacao)
    
    return percentual_aumento, aumento, aumento_real, novo_salario

def main():
    salario = float(input("Digite o salário do colaborador: R$ "))
    
    while salario <= 0:
        print("Salário inválido. Por favor, digite um valor válido.")
        salario = float(input("Digite o salário do colaborador: R$ "))
    
    percentual_aumento, aumento, aumento_real, novo_salario = calcular_reajuste(salario)
    
    print("\nSalário antes do reajuste: R$ {:.2f}".format(salario))
    print("Percentual de aumento aplicado: {}%".format(percentual_aumento))
    print("Valor do aumento: R$ {:.2f}".format(aumento))
    print("Novo salário após o aumento: R$ {:.2f}".format(novo_salario))
    print("Valor do aumento real, descontado a inflação: R$ {:.2f}".format(aumento_real))

if __name__ == "__main__":
    main()
