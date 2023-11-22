"""
Autor:Cristian Mateo Jimenez Londoño
Fecha:21-11-2023
Objetivo:El programa deberá evaluar ambos porcentajes con la misma escala y mostrar el resultado en pantalla 
para ambos porcentajes:

o “NO PRESENTA SIGNOS”: porcentaje entre 0 y 40

o “PRESENTA ALGUNOS SIGNOS LEVES”: porcentaje entre 41 y 74

o “SIGNOS MODERADOS”: porcentaje entre 75 y 79

o “SIGNOS NOTORIOS SEVEROS”: porcentaje entre 80 y 100
"""

# Bienvenida
print("¡Bienvenido al programa de evaluación de estilo de aprendizaje!")

# Solicitar porcentajes de discalculia y dislexia al usuario
porcentaje_discalculia = float(input("Ingresa el porcentaje de discalculia: "))
porcentaje_dislexia = float(input("Ingresa el porcentaje de dislexia: "))

# Evaluar y mostrar resultados para discalculia
print("\nEvaluación de Discalculia:")
if 0 <= porcentaje_discalculia <= 40:
    print("NO PRESENTA SIGNOS de discalculia.")
elif 41 <= porcentaje_discalculia <= 74:
    print("PRESENTA ALGUNOS SIGNOS LEVES de discalculia.")
elif 75 <= porcentaje_discalculia <= 79:
    print("SIGNOS MODERADOS de discalculia.")
elif 80 <= porcentaje_discalculia <= 100:
    print("SIGNOS NOTORIOS SEVEROS de discalculia.")
else:
    print("Porcentaje de discalculia no válido.")

# Evaluar y mostrar resultados para dislexia
print("\nEvaluación de Dislexia:")
if 0 <= porcentaje_dislexia <= 40:
    print("NO PRESENTA SIGNOS de dislexia.")
elif 41 <= porcentaje_dislexia <= 74:
    print("PRESENTA ALGUNOS SIGNOS LEVES de dislexia.")
elif 75 <= porcentaje_dislexia <= 79:
    print("SIGNOS MODERADOS de dislexia.")
elif 80 <= porcentaje_dislexia <= 100:
    print("SIGNOS NOTORIOS SEVEROS de dislexia.")
else:
    print("Porcentaje de dislexia no válido.")
