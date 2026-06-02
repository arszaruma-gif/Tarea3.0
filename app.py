# Lógica de la calculadora básica
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

if __name__ == "__main__":
    print("--- Aplicación Calculadora Interactiva ---")
    
    try:
        # Solicitar datos por consola al usuario
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        print("\n--- Resultados ---")
        print(f"Suma: {num1} + {num2} = {sumar(num1, num2)}")
        print(f"Resta: {num1} - {num2} = {restar(num1, num2)}")
        print(f"Multiplicación: {num1} * {num2} = {multiplicar(num1, num2)}")
        
        try:
            print(f"División: {num1} / {num2} = {dividir(num1, num2)}")
        except ValueError as e:
            print(f"División: {e}")
            
    except (EOFError, ValueError):
        # Esto se ejecuta de forma automática si corre en GitHub Actions 
        # para evitar que el flujo se quede congelado esperando el teclado.
        print("\n[Modo No-Interactivo detectado o Datos Inválidos]")
        print("Ejecutando prueba automática con valores por defecto (10 y 5):")
        print(f"Suma: 10 + 5 = {sumar(10, 5)}")
        print(f"Resta: 10 - 5 = {restar(10, 5)}")
        print(f"Multiplicación: 10 * 5 = {multiplicar(10, 5)}")
        print(f"División: 10 / 5 = {dividir(10, 5)}")

    print("-----------------------------------------")