def inverter_string(s):
    l_caracteres = list(s)
  
    for i in range(len(l_caracteres) // 2):
        temp = l_caracteres[i]
        print(f"estado inicial {i+1} {l_caracteres}")
        l_caracteres[i] = l_caracteres[-i - 1]
        print(f"passo a passo {l_caracteres}")
        l_caracteres[-i - 1] = temp
        print(f"estado final {l_caracteres}")
    
    return ''.join(l_caracteres)

entrada = input("Digite uma string: ")

saida = inverter_string(entrada)

print("String invertida: ", saida)
