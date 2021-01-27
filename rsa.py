from math import *


# Verifica se o número é primo.
def check_prime(n):
    if (n == 1):
        return False
    i = 2
    while (i <= n - 1):
        if (n % i == 0):
            return False
        i += 1
    if (i == n):
        return True


def is_coprime(a, b):
    while b != 0:
        a, b = b, a % b
    if a == 1:
        return True
    return False


def mod_inverse(a, b):
    a = a % b
    i = 1
    while (i < b):
        if ((a * i) % b == 1):
            return i
        i += 1

prog = True

while prog == True:
    print("------------------------------------")
    print("          CRIPTOGRAFIA RSA")
    print("------------------------------------")
    print("<0> - Exibir informações")
    print("<1> - Criptografar uma mensagem")
    print("<2> - Descriptografar uma mensagem")
    print("<3> - Criar chaves")
    print("<4> - Finalizar programa")
    print("------------------------------------")
    op = input("Escolha uma opção: ")

    if op == '0':
        info_screen = True
        while info_screen == True:
            print("------------------------------------")
            print("<1> - Informações gerais")
            print("<2> - Geração de chaves")
            print("<3> - Retornar")
            print("------------------------------------")
            op2 = input("Escolha uma opção: ")

            if op2 == '1':
                print("\n--------------------------------------------------------")
                print("                   Informações Gerais")
                print("--------------------------------------------------------")
                print("A criptografia RSA é um dos algoritmos de encriptação")
                print("mais seguros e populares existentes. O funcionamento é")
                print("baseado em princípios matemáticos (numeros primos e")
                print("restos de divisao).")
                print("--------------------------------------------------------")
                try:
                    input("Pressione enter para continuar ")
                except SyntaxError:
                    pass

            if op2 == '2':
                print("\n-------------------------------------------------")
                print("                 Geração de Chaves")
                print("-------------------------------------------------")
                print("No RSA as chaves são geradas desta maneira: ")
                print("1.  Os números 'p' e 'q' devem ser números primos;")
                print("2.  Calcula-se n = p.q;")
                print("3.  Calcula-se tot.(n) = (p − 1).(q − 1);")
                print("4.  Escolhe-se um inteiro 'e', tal que 1 < e < tot.(n),")
                print("de forma que 'e' e tot.(n) sejam primos entre si;")
                print("5.  Calcula-se d, de forma que d.e ≡ 1 mod(tot. n).")
                print("-------------------------------------------------")
                try:
                    input("Pressione enter para continuar ")
                except SyntaxError:
                    pass

            if op2 == '3':
                info_screen = False

    elif op == '1':
        msg = input("Insira a mensagem a ser criptografada: ")

        e = int(input("Insira a chave pública 'e': "))
        n = int(input("Insira a chave pública 'n': "))

        # Converte o texto inicial para ASCII
        ascii = [ord(ele) for sub in msg for ele in sub]

        # Usar a fórmula bloco^e (mod n) para obter o bloco final
        final_message = ascii.copy()

        for i in range(len(ascii)):
            final_message[i] = ascii[i] ** e % n

        print("-------------------------------------")
        print("         Mensagem codificada")
        print("-------------------------------------")
        print(*final_message, sep = " ")

        try:
            input("\nPressione enter para continuar ")
        except SyntaxError:
            pass

    elif op == '2':
        rsa = [int(x) for x in input("Insira a mensagem criptografada: ").split()]
        p = int(input("p: "))
        q = int(input("q: "))
        e = int(input("e: "))
        n = p * q
        tn = (p - 1) * (q - 1)
        d = mod_inverse(e, tn)

        rsa_aux = rsa.copy()
        for i in range(len(rsa)):
            rsa_aux[i] = rsa[i] ** d % n

        print("-------------------------------------")
        print("      Mensagem descriptografada")
        print("-------------------------------------")
        print(''.join(chr(i) for i in rsa_aux))
        print("-------------------------------------")
        try:
            input("Pressione enter para continuar ")
        except SyntaxError:
            pass

    elif op == '3':
        p_q_prime = False
        while (p_q_prime == False):
            print("Insira duas chaves privadas (devem ser numeros primos) ")
            p = int(input("p: "))
            q = int(input("q: "))
            if (check_prime(p) == True and check_prime(q) == True):
                p_q_prime = True

        # A variável n é a primeira chave pública.
        n = p * q
        # Função totiente de n.
        tn = (p - 1) * (q - 1)

        e_is_coprime = False
        while (e_is_coprime == False):
            print("Insira uma chave pública")
            print("(deve ser um número tal que 1 < e < " + str(tn) + ",")
            print("de forma que " + str(tn) + " e o número sejam co-primos)")
            e = int(input("(e): "))
            if (is_coprime(e, tn) == True and (e > 1) and (e < tn)):
                e_is_coprime = True

        d = mod_inverse(e, tn)

        print("--------------------------------------")
        print("            Chaves Criadas")
        print("--------------------------------------")
        print("Chaves públicas:  e = " + str(e) + "; n = " + str(n) + ".")
        print("Chaves privadas:  p = " + str(p) + "; q = " + str(q) + "; d = " + str(d) + ".")
        print("--------------------------------------")

        try:
            input("Pressione enter para continuar ")
        except SyntaxError:
            pass

    elif op == '4':
        prog = False

