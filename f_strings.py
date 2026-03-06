#Una de las importaciones nativas más comunes es datetime para establecer una fecha. 
from datetime import datetime
#Lo usaremos más adelante, pero por buena práctica, todas las importaciones deben estar al comienzo del código.


#Los f-string son una sintaxis especial para formatear mejor las cadenas de texto. 
#Consiste en colocar una f por delante del string, para que así el lenguaje sepa que estamos utilizando este tipo de sintaxis. 
#Una vez hecho esto, se nos permitirá colocar cualquier tipo de variable por su nombre entre llaves. Por ejemplo: 

name = "Ana"
text = f"Hola {name}"
print(text)

#Es una mala práctica utilizar f-strings sin ningún tipo de variable en su contenido. Para eso simplemente podemos usar las cadenas de texto normales. 

#Otra forma que se utiliza para trabajar con variables dentro de strings es con el método 
#.format():

text_format = "Hola {}".format(name)
print("Texto con format: " + text_format)

#Aquí se colocan las llaves vacías en el lugar que debe ocupar el valor de la variable que se pasa como parámetro de la función. 

#Entre las llaves del f-string no solo podemos poner variables sino colocar cualquier funcionalidad lógica. Por ejemplo, una operación aritmética. 

text_product = f"El resultado de catorce veces doce es: {14 * 12}"
print(text_product)

#Incluso podríamos hacer llamadas a funciones y colocar condicionales, de la siguiente forma:
edad = 24
text_if = f"Hola {name}, eres {'mayor' if edad >= 18 else 'menor'} de edad."

#Claramente, el resultado de la lógica debe poder representarse por medio de un string. Cualquier tipo de dato representado dentro de las llaves de un f-string será transformado en cadena de texto. 

#Esta herramienta también tiene más opciones de formateo. 
#Por ejemplo, para el manejo de números grandes. Supongamos que la IA colapsa y nos va muy bien en la programación:

bank_balance = 34958000
text = f"El saldo disponible en su cuenta bancaria es de: ${bank_balance:,}"
print(text)

#Los dos puntos y coma que acompañan a la variable formatean el número para que sea más legible por un humano. Se leerá $34,958,000 

#También podremos controlar números decimales y la cantidad de cifras decimales que queremos mostrar:

pi = 3.1415
text = f"El valor de pi es: {pi:.1f}"
print(text) # Un solo decimal. :.1f
text = f"El valor de pi es: {pi:.2f}"
print(text) # 2 decimales. :.2f

#También, en el caso de mostrar contadores con un formato homogéneo, podemos agregar ceros antes de un valor predeterminado. 

user_id = 1
text = f"Su id de usuario es: {user_id:04d}" 
print(text) # Se agregan tres ceros antes del 1, para mantener 4 dígitos. :04d 


#Para crear una fecha, una vez importado datatime, podremos usarlo de la siguiente manera:
#datatime(año, mes, día, hs, min, s, ms)
date = datetime(2026, 3, 4, 16, 17)
text = f"Este texto fue escrito en: {date}"
print(text)
#Y podemos darle un formato más legible (en inglés):
text = text = f"Este texto fue escrito en: {date: %A %d of %B of %Y at %I:%M %p}"
print(text)