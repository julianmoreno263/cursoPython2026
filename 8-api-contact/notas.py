"""

Una API REST es, explicada de forma sencilla, un "puente" o un traductor que permite que dos aplicaciones o sistemas informáticos se comuniquen entre sí a través de Internet para compartir datos.

Para entenderlo sin tecnicismos, imagina que vas a un restaurante:

Tú (el cliente): Eres la aplicación móvil o la página web.

La cocina: Es el servidor donde están guardados todos los datos.

El mesero: Es la API REST. Toma tu pedido (petición), va a la cocina, y te trae la comida (los datos) en un plato que entiendes.

Las siglas API significan Application Programming Interface (Interfaz de Programación de Aplicaciones), y REST (Representational Stateiter Transfer) es simplemente el conjunto de reglas y buenas prácticas que ese "mesero" debe seguir para que la comunicación sea limpia, rápida y ordenada.

¿Cómo funciona en el día a día?
Cada vez que usas tu teléfono, estás interactuando con decenas de APIs REST. Por ejemplo:

Cuando abres una app del clima, esta le pide los datos actualizados al servidor de un instituto meteorológico mediante una API REST.

Cuando ves Uber y el mapa te muestra dónde viene el auto, la app se comunica con la API de Google Maps para pintar el mapa en tu pantalla.

Las 4 peticiones básicas (Los "Verbos" HTTP)
Una API REST funciona usando el mismo protocolo que usas para navegar por internet (HTTP), y se basa principalmente en cuatro acciones:

Acción	Verbo HTTP	¿Qué hace el "mesero"?
Leer	GET	Trae información del servidor (ej. ver tu feed de Instagram).
Crear	POST	Envía información nueva al servidor (ej. publicar una foto nueva).
Actualizar	PUT o PATCH	Modifica algo que ya existe (ej. editar tu biografía de perfil).
Eliminar	DELETE	Borra un dato del servidor (ej. borrar un tweet).
¿Por qué son tan populares?
Hablan un idioma universal: Casi todas las APIs REST devuelven la información en un formato llamado JSON, que es texto plano que cualquier lenguaje de programación (Python, JavaScript, Java, etc.) puede entender fácilmente.

Son independientes: Al servidor no le importa si el usuario está conectado desde un iPhone, una computadora con Windows o una televisión inteligente; la API REST entrega los datos de la misma manera para todos.

¿Te gustaría ver un ejemplo real de cómo se ve el código de una petición a una API?

 Las APIs REST viven y se ejecutan en el servidor (lo que en programación llamamos el Backend).Cuando un programador dice "voy a crear una API", lo que realmente está haciendo es escribir código (en lenguajes como Node.js, Python, PHP, Java o C#) y guardarlo en una computadora conectada a internet las 24 horas: el servidor.Para entender exactamente dónde se ubica y qué hace cada parte, podemos dividir el proceso en tres capas:1. El Cliente (El Front-end)Es lo que el usuario ve y toca. Puede ser una aplicación móvil en tu teléfono, una página web en tu navegador o la pantalla de un cajero automático. El cliente no tiene los datos (no guarda la lista de productos de Amazon ni las fotos de Instagram); solo sabe cómo mostrarlos de forma bonita.2. El Servidor y la API REST (El Back-end)Aquí es donde vive la API. El servidor está escuchando atentamente a internet. Cuando tú entras a una app y buscas algo, el cliente le envía una señal al servidor. La API REST recibe esa señal, verifica quién eres (por seguridad), procesa lo que estás pidiendo y decide qué responder.3. La Base de DatosEs el "almacén" o disco duro del servidor donde están guardados físicamente todos los textos, contraseñas, imágenes y registros. La API REST es la encargada de ir a buscar la información a la base de datos, ordenarla y empaquetarla.Un ejemplo visual de la ruta:Tu teléfono (Cliente): Envía una petición GET que dice: "Quiero ver el perfil de Juan".El Servidor (Donde vive la API REST): Recibe la orden. Va a la Base de Datos, saca la foto y el nombre de Juan, los convierte a un formato de texto universal (JSON) y se los envía de vuelta al teléfono.Tu teléfono: Recibe ese texto, lo interpreta y te muestra la foto y el nombre en la pantalla.En resumen: La API REST es el motor y el cerebro que está oculto en el servidor. El cliente (tu teléfono o computadora) es solo la carrocería y el volante que tú usas para manejarlo.

 Para que una API REST que vive en el servidor no sea una puerta abierta para que cualquiera robe o altere la información, se utilizan mecanismos de seguridad y autenticación.Básicamente, el servidor actúa como el guardia de un club exclusivo: antes de dejarte pasar o darte información, te pide tu "identificación".Aquí tienes los 3 métodos más comunes que utiliza el servidor para protegerse:1. API Keys (Llaves de API)Es el método más sencillo. El servidor te da una cadena de texto larga y secreta (como una contraseña larga, por ejemplo: api_key_abc123xyz).Cómo funciona: Cada vez que tu aplicación le pide algo al servidor, debe incluir esa llave en la petición. Si la llave es correcta, el servidor responde; si no, bloquea el acceso.Uso común: Se usa mucho en APIs públicas o de consulta (como la API del clima o de Google Maps), principalmente para saber quién está consumiendo sus datos y cobrarles o ponerles un límite si hacen demasiadas preguntas por minuto.2. Tokens JWT (JSON Web Tokens) — El pase de abordarEste es el estándar de la industria para aplicaciones donde los usuarios inician sesión (como Facebook, Netflix o tu app del banco).El proceso es el siguiente:Inicio de sesión: Envías tu usuario y contraseña al servidor una sola vez.La entrega del Token: Si tus datos son correctos, la API REST en el servidor genera un Token JWT (un código encriptado ultra seguro) y te lo devuelve. Este token es como un pase de abordar.Peticiones protegidas: A partir de ese momento, tu teléfono ya no vuelve a enviar tu contraseña. Cada vez que quieres ver tus fotos o hacer un pago, el teléfono le muestra ese Token al servidor.Expiración: Estos tokens tienen fecha de caducidad (por ejemplo, expiran en 1 hora). Si alguien te lo roba, dejará de funcionar muy pronto.3. OAuth 2.0 — El permiso de invitado¿Has visto cuando entras a una página web nueva y te sale un botón que dice "Iniciar sesión con Google" o "Iniciar sesión con Facebook"? Eso es OAuth.Cómo funciona: En lugar de darle tu contraseña de Google a esa página nueva, Google te pregunta: "¿Le das permiso a esta app de ver tu nombre y correo?". Al decir que sí, Google le da un token de acceso limitado a la API de esa app para que solo pueda ver lo que tú autorizaste, sin comprometer tu contraseña real.Un escudo extra: El cifrado HTTPSSin importar cuál de los métodos anteriores se use, toda API REST moderna debe viajar a través de HTTPS (el candadito verde del navegador). Esto asegura que toda la información que viaja desde tu teléfono hasta el servidor vaya "encriptada" o codificada. Si un hacker intenta interceptar el mensaje en el Wi-Fi de una cafetería, solo verá símbolos raros sin sentido.En resumen: El servidor protege la API REST exigiendo que cada petición lleve una "credencial" válida (Key o Token) y asegurándose de que toda la comunicación viaje de forma secreta gracias al cifrado.

 El formato JSON (JavaScript Object Notation) es el estándar absoluto que usan las APIs REST para enviar y recibir información.

Aunque lleva "JavaScript" en el nombre, hoy en día es un formato universal. Es tan popular porque logra el equilibrio perfecto: es ultra ligero para las computadoras y, al mismo tiempo, es muy fácil de leer para nosotros los humanos.

Básicamente, un JSON es una lista de datos encerrada entre llaves { } que funciona con el concepto de Clave : Valor (el nombre del dato y su contenido).

Así se ven los datos de un usuario en formato JSON:
Imagina que la API de LinkedIn en el servidor procesa tu perfil y se lo envía a tu teléfono. El teléfono recibe un texto plano que se ve exactamente así:

JSON
{
  "id": 84729,
  "nombre_completo": "Ana Martínez",
  "profesion": "Desarrolladora Back-end",
  "esta_activa": true,
  "habilidades": ["Python", "APIs REST", "Bases de Datos"],
  "contacto": {
    "email": "ana.martinez@email.com",
    "ciudad": "Bogotá"
  }
}
Anatomía de un JSON (Las reglas del juego):
Si miras el código de arriba, notarás que la API estructura la información siguiendo unas reglas muy sencillas:

Todo va entre comillas: Tanto las claves ("nombre_completo") como los textos ("Ana Martínez") deben llevar comillas dobles obligatoriamente.

Soporta diferentes tipos de datos:

Texto: Entre comillas.

Números: Sueltos, sin comillas (como el 84729).

Booleanos: Valores de verdadero o falso (true o false), ideales para saber si una cuenta está activa o verificada.

Listas (Arrays): Van entre corchetes [ ]. Sirven para agrupar cosas, como la lista de "habilidades".

Objetos anidados: Puedes meter un JSON dentro de otro JSON usando llaves internas, como hicimos con la sección de "contacto".

¿Por qué la API REST ama el JSON?
Antes de que existiera JSON, las APIs usaban un formato llamado XML, que llenaba el mensaje con etiquetas de apertura y cierre (muy parecido a las páginas web en HTML).

Mira la diferencia de peso y claridad para decir exactamente lo mismo:

Viejo formato (XML) - Pesado y difícil de leer	Formato Moderno (JSON) - Limpio y ligero
<usuario>


<nombre>Ana</nombre>


<id>84729</id>


</usuario>

{


"nombre": "Ana",


"id": 84729


}

Al eliminar todas esas etiquetas repetitivas, el archivo se vuelve muchísimo más pequeño. Multiplica ese ahorro de espacio por los millones de usuarios que usan una app al mismo tiempo, y el resultado es un internet muchísimo más rápido y aplicaciones que consumen menos datos en tu celular.


serializar:

Serializar en Python es el proceso de convertir un objeto complejo que vive en la memoria de tu programa (como una lista, un diccionario, o una clase personalizada) en un formato de texto o de bytes que se pueda guardar en un archivo o enviar a través de internet.

El proceso inverso (tomar ese archivo o texto y volver a transformarlo en un objeto de Python) se llama deserializar.

Para entenderlo de forma muy simple: imagina que construyes una figura compleja con piezas de Lego.

Serializar es desarmar la figura y meter las piezas ordenadas en una caja con un manual de instrucciones para poder mandarla por correo.

Deserializar es abrir la caja en el destino y volver a armar la figura exactamente como estaba usando las instrucciones.

¿Para qué se usa en la vida real?
Para guardar el estado de tu programa: Si estás jugando un videojuego en Python y quieres guardar la partida, necesitas serializar los datos del jugador (vida, nivel, inventario) en un archivo de texto para poder cerrarlo y continuar mañana.

Para enviar datos a una API REST: Como vimos antes, el servidor no puede mandarle un "diccionario de Python" directamente a un navegador web. Necesita serializarlo a formato JSON (texto plano) para que viaje por internet.

Las 2 formas más comunes de serializar en Python
Python incluye herramientas nativas para hacer esto dependiendo de lo que necesites:

1. Serializar a JSON (Texto - El estándar para la web)
Ideal cuando quieres que los datos sean legibles por humanos o por otros lenguajes de programación. Se usa la librería nativa json.

Python
import json

# Un diccionario común y corriente de Python (Objeto en memoria)
usuario = {
    "nombre": "Carlos",
    "edad": 30,
    "es_programador": True
}

# SERIALIZAR: Lo convertimos a una cadena de texto (String) estilo JSON
texto_json = json.dumps(usuario)

print(texto_json)
# Resultado: '{"nombre": "Carlos", "edad": 30, "es_programador": true}'
# Nota cómo True cambió a true (formato universal)
2. Serializar con Pickle (Bytes - Exclusivo de Python)
Si necesitas guardar objetos muy complejos (como un modelo de Inteligencia Artificial o una función entera), JSON no te servirá porque solo entiende texto. Para eso usas pickle, que convierte el objeto en una cadena de bytes (símbolos raros que solo Python entiende).

Python
import pickle

datos_complejos = [1, 2, {"clave": "valor"}, (5, 6)]

# SERIALIZAR: Lo convierte a un formato binario listo para guardarse en un archivo .pkl
datos_serializados = pickle.dumps(datos_complejos)

print(datos_serializados)
# Resultado: b'\x80\x04\x95!\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02}\x94\x8c\x05clave\x94\x93...'
⚠️ Nota de seguridad importante: Nunca deserialices un archivo hecho con pickle si te lo pasó un desconocido en internet. Al deserializarlo, ese archivo podría ejecutar código malicioso dentro de tu computadora. Para compartir datos con externos, siempre es mejor usar JSON.
"""