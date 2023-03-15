def generar_contraseña(nombre, APP,APM, Fecha, Carrera):
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if especiales:
        caracteres += string.punctuation
    return ''.join(random.choice(caracteres) for i in range(long))
