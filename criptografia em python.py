def cifra_cesar(texto, chave):
    resultado = ""

    for char in texto:
        if char.isalpha():
            # Verifica se o caractere é uma letra ou não
            deslocamento = ord('A') if char.isupper() else ord('a')
            resultado += chr(((ord(char) - deslocamento + chave) % 26) + deslocamento)
        else:
            resultado += char  # Mantém outros caracteres inalterados

    return resultado

#inserir o texto original para criptografar 
texto_original = input("Digite o texto original: ")
#chave = -3 texto criptografado volta ao normal
chave = +3
texto_criptografado = cifra_cesar(texto_original, chave)
print("Texto Criptografado:", texto_criptografado)

# Para descriptografar, use a mesma função com a chave negativa
texto_descriptografado = cifra_cesar(texto_criptografado, -chave)
print("Texto Descriptografado:", texto_descriptografado)
