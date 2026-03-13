"""
El PEP257 establece algunas normativas con respecto a la documentación de proyectos. 
Siguiendo una de las filosofías de Python, se tiene en cuenta que el código es leído mucho más de lo que es escrito, y por tanto la importancia de la documentación. 

Un "docstring" es un texto entre tres comillas que describe la funcionalidad de módulos, funciones o clases.
Se utiliza la sintaxis de triple comilla porque, como lo estamos viendo, permite generar un comentario de varias líneas. 
Cada archivo puede empezar con un docstring de módulo que lo explique de manera clara y concisa. Pero además, cada función o clase debe tener docstring interno que explique su propósito y uso. 
"""

#Esta función solo sirve de ejemplo y retorna un saludo. Pero en su docstring se puede ver el formato que debe tener la documentación de cada función segun el PEP257.
def ejemplo():
    """
    DESCRIPTION: Breve descripción de la función.
    ARGS: lista de argumentos que recibe y  su tipo. 
    RETURN: dato de retorno o resultado de la función.
    """
    return "Hola Mundo!"

#Al tener un docstring, la función tiene la opción de llamarlo y mostrarlo por consola por medio de un atributo, de la siguiente forma:
print(ejemplo.__doc__)

#También existe el método 'help()' que nos muestra el docstring por consola:
help(ejemplo)

#En el caso de que la función no tenga docstring, en la pantalla se mostrará None. 

"""
Una forma fácil de automatizar estos formatos con ayuda de IA, como actualmente se realiza en la industria, es pasar la función a documentar a un agente o modelo como Claude, pasándole el siguiente prompt:

"Genera un docstring completo en [lenguaje del proyecto] siguiendo PEP 257 para esta función. Incluye descripción, parámetros, retorno, excepciones y ejemplos". 

Esto genera un docstring completo explicando la función, que luego se puede ir modificando para lograr que sea claro y conciso. La documentación no es una práctica obligatoria, pero si resulta muy útil, en especial cuando se utilizan funciones complejas que a simple vista son difíciles de leer. 
"""