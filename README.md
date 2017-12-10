Desarrollador: **Ricardo Pereira**

## **krono_test**
    Se presenta la prueba técnica para Krono Group realizada en django.

## **Requisitos**
    1.Django
    2.Django Rest Framework (DRF)
    3.Git
---

## **Iniciar proyecto**
    -Crear entorno virtual
           Caso windows:
                Ejecutar archivo activate.bat en la carpeta Scripts del proyecto.

           Caso linux o mac:
                Ejecutar el comando: λ virtualenv .env
               
    -Correr el proyecto     
           λ python prueba/manage.py runserver


## **Especificaciones técnicas**
    Se crearon tres (3) entidades denominadas: Ciudad, Tienda y Usuario.

    Ciudad: id, nombre.
    Tienda: id, nombre, ciudad.
    Usuario: id, nombre, email, passw (opcional), tiendas.

    Donde una tienda posee solo una ciudad y un usuario está registrado en una o más tiendas.

    Se implementó de esa manera para establecer la relación de uno a muchos (ciudad => tiendas) y la relación de muchos a muchos (tiendas <=> usuarios).

---

## **RestAPI**
### *Obtener todos los usuarios de una tienda*
    URL: http://domain:port/api_test/users/{id_tienda}/
    Method: GET
    Response: [{ user1 }, {user2}, ... {userN} ]
        
### *Obtener todas las tiendas de una ciudad*
    URL: http://domain:port/api_test/shops/{id_user}/
    Method: GET
    Response: ["shop_name1", "shop_name2", ... "shop_nameN"]

### *Obtener todas las tiendas de una ciudad, asociadas a un usuario*
    URL: http://domain:port/api_test/shops_city/user={id_user}&city={id_city}/
    Method: GET
    Response: ["shop_name1", "shop_name2", ... "shop_nameN"]

##**Ejemplos:**

###Endpoint 1
*URL*: **http://127.0.0.1:8000/api_test/users/1/**

*Method*: **GET**

*Response*:    
         
        [{"nombre": "Ricardo", "email": "ricardo@hotmail.com"}, {"nombre": "Marcos", "email": "marcos@gmail.com"}, {"nombre": "Joao", "email": "joao@gmail.com"}]

###Endpoint 2
*URL*: **http://127.0.0.1:8000/api_test/shops/1/**

*Method*: **GET**

*Response*:    
         
        ["Todo a mil", "Facilito", "Alfombras Shop"]


###Endpoint 3
*URL*: **http://127.0.0.1:8000/api_test/shops_city/user=6&city=4/**

*Method*: **GET**

*Response*:    
         
        ["Mercadito", "Licoreros", "Informaticos y mas"]


