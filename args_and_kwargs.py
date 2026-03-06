# ---------*args-----------
# En Python es posible colocar argumentos dinámincos a las funciones. Esto le permite recibir una cantidad indefinida de argumentos, los cuales los convierte en una tupla para luego poder utilizarse según su orden en la lógica de la función.
# Por ejemplo:


def ejemplo_args(*args):
    print(f"Todos los argumentos: {args}")
    print(f"Tipo de *args: {type(args)}")


# ejemplo_args("argumento 1", "argumento 2", "argumento 3", "parámetro 4")

# Como vemos, la funcionalidad se escribe con un asterisco seguido de cualquier nombre de variable y convierte todos los argumentos en una tupla, una lista ordenada inmutable. Por tanto pueden ser identificadas por su posición en la tupla.


def suma_con_args(*nums):
    """
    Función que utiliza argumentos dinámincos para retornar la suma de ellos.
    """
    cont = 0
    for num in nums:
        cont += num
    return cont


# print(suma_con_args(1,2,3,4,5,6)) #21
# print(suma_con_args(11, 2, 3, 7)) #23

# ---------**kwargs-----------


def ejemplo_kwargs(**kwargs):
    print(f"Todos los argumentos: {kwargs}")
    print(f"Tipo de **kwargs: {type(kwargs)}")


# ejemplo_kwargs(uno="argumento 1", dos="argumento 2", tres="argumento 3", cuatro= "parámetro 4")

# A diferencia de los *args, los **kwargs trabajan con pares clave-valor. Lo que hace que conforme un diccionario con cada argumento que se pasa a la función.
#Por tanto es importante diferenciar que, en el caso de que tengamos argumentos de caracter homogéneo e indistinto, como en el caso de la suma de números, es conveniente usar *args. Pero, si tenemos una función que distingue entre distintos datos, o tiene algunos argumentos que son de caracter opcional. Entonces es conveniente usar **kwargs para poder trabajarlo como variables dentro de un diccionario, estableciendo los valores de cada clave directamente en el llamado a la función:  

def perfil (**kwargs):
    print("Su perfil de usuario contiene la siguiente información:")
    print(f"Usuario: {kwargs["user_name"]}")
    print(f"Contraseña: {kwargs["password"]}")

perfil(user_name = "Lauchita007", password = "cotr1234")   