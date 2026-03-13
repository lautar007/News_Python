"""
Python es un lenguaje de tipado dinámico (o débil). Esto significa que cada variable recibe automáticamente un tipo cuando se le asigna un dato o estructura.
Esto se diferencia del tipado fuerte (en lenguajes como Java), donde es obligatorio, junto con la declaración de la variable, indicar también el tipo de dato que contendrá. 

Pero el creador de Python, a partir de la versión 3.5, decidió implementar un sistema de tipado basado en etiquetas a las que llamo 'type hints'. Estas etiquetas indican el tipo esperado por la variable. Pero, al igual que uno puede colocar sal en un pote de azúcar, no fuerza el cumplimiento de dicha etiqueta en tiempo de ejecución. 
Sin embargo, esta implementación aporta documentación y legibilidad al código. 
"""

variable = 24 #Automáticamente se asigna el tipo entero.

print(f"dato en la variable: {variable}; tipo de la variable: {type(variable)}")

variable = "Casa" #Automáticamente se sobreasigna el tipo de dato a string. 

print(f"dato en la variable: {variable}; tipo de la variable: {type(variable)}")

#Ahora vemos a utilizar type hints, cuya sintaxis es la siguiente:

variable: int = 42 
print(f"dato en la variable: {variable}; tipo de la variable: {type(variable)}")

#Algunas variables también pueden aceptar valores vacíos:

userId: str | None = None
print(f"dato en la variable: {userId}; tipo de la variable: {type(userId)}")

#Este tipado también se puede establecer en funciones: 
#Se pueden definir los tipos para los argumentos con la sintaxis ya mencionada, y también se puede definir el tipo del retorno de la función utilizando un operador flecha ->

def suma (a:int, b:int) -> int:
    return a + b

#Las estructuras más complejas también se pueden tipar: 

#En el caso de las listas podemos definir incluso qué tipo de datos contiene la misma:
articles: list[str] = ["aticle 1", "article 2", "article 3"]

#Los tipos más comunes que se utilizan son:
# 'int', 'str', 'list', 'dict', 'tuple'

#Luego, en caso de que una misma variable tenga más de un tipo de dato, se lo puede tipar como 'Any'
#Pero caso de usar 'Any' es preferible no tener tipado fuerte.

"""
En caso de no conocer el tipo de un determinado dato o estructura, siempre se puede pasar por consola el tipo utilizando el método 'type'. 
Esta implementación es útil para un código más prolijo, aunque no es muy útil para obtener esa capa de seguridad que es el objetivo del tipado fuerte, porque el lenguaje de todas formas me permite incumplir con lo declarado.
Sin embargo existe una extensión en VSC llamada "Mypy Type Checker" que genera errores para simular el tipado fuerte en Python. Esta extensión las lineas de código donde se realicen cambios en el tipo de variable que ya fue asignada (automáticamente o con type hints) antes. 
"""