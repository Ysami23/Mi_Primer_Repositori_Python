# Nombre del estudiante: Yojan Samitr Palacios Quinto
# Grupo: 163 
# Programa: Fundamentos de programación 
# Código Fuente: Propia

# MENU DEL RESTAURANTE
menu = [
    ["Hamburguesa", "Comida rápida", 18000],
    ["Pizza", "Comida rápida", 25000],
    ["Ensalada Fresca", "Saludable", 15000],
    ["Jugos Naturales", "Bebidas", 8000],
    ["Sancocho trifasico", "Almuerzo", 30000],
    ["Pescado frito", "Marisco", 22000],
    ["Helado de Chocolate", "Postre", 28000]
]

# categoria_seleccionada y pago_minimo
categoria_seleccionada = input("Ingrese la categoría que desea" \
" (Comida rápida, Saludable, Bebidas, Almuerzo, Marisco, Postre): ")
pago_minimo = 25000


# Funcion para calcular el total a pagar
def calcular_total_a_pagar(categoria, categoria_seleccionada, pago_base):
    if categoria == categoria_seleccionada and pago_base > pago_minimo:
        descuento = pago_base * 0.15
        total_a_pagar = pago_base - descuento
    else:
        total_a_pagar = pago_base
    return total_a_pagar

# Mostrar resultados
print("Categoría seleccionada\n")

for item in menu:
    nombre = item[0]
    categoria = item[1]
    precio_base = item[2]

    total_a_pagar = calcular_total_a_pagar(categoria, categoria_seleccionada, precio_base)
    
    print("Nombre:", nombre)
    print("Categoría:", categoria)
    print("Precio Base:", precio_base)
    print("Total a Pagar:", total_a_pagar)