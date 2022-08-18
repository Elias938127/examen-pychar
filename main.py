diccionario  = { "codigo" : [ "001" , "002" , "003" , "004" , "005" ],
               "nombre" : [ "Juan" , "Carlos" , "Jay" , "Pedro" , "Matías" ],
               "cursos" : [ "Inglés" , "Ciencias Sociales" , "Matemática" ]}

listaproductos  = []
promedio  =  0
respuesta  =  "s"
mientras  resp  ==  "s" :
    codigoIn  =  input ( "Ingrese el codigo del alumno: " )
    cursoTemp  =  input ( "Ingrese el nombre del curso: " )
    nota  =  int ( input ( "Ingrese la primera nota: " ))
    nota1  =  int ( input ( "Ingrese la segunda nota: " ))
    nota2  =  int ( input ( "Ingrese la tercera nota: " ))
    x  =  0
    para  i  en  diccionario [ "codigo" ]:
        si  i  ==  codigoIn :
            codigoTemp  =  i
            nombreTemp  =  diccionario [ "nombre" ][ x ]
            promTemp  =  nota  +  nota1  +  nota2
            promedio  =  promTemp  /  3
            registro  = [ str ( codigoTemp ), ' \t ' ' \t ' , nombreTemp , ' \t ' ' \t ' , cursoTemp , ' \t ' ' \t ' ,
                        str ( nota ), ' \t ' , str ( nota1 ), ' \t ' , str ( nota2 ), ' \t ' ' \t ' , str ( promedio )]
            imprimir ()
            imprimir ( "________________________________________" )
            listaproductos . adjuntar ( registro )
            cadenavalores  =  "" . unirse ( registro )
            f  =  abrir ( "archivo demo.txt" , "a" )
            F. _ escribir ( " \n "  +  cadenavalores )
            F. _ cerrar ()
        X  + =  1
    resp  =  input ( "¿Desea seguir ingresando datos?: " )
    imprimir ( "________________________________________" )
    f  =  abrir ( "demofile.txt" )
    imprimir ( f . leer ())
    F. _ cerrar ()
imprimir ()
imprimir ( "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ -_-_-_-_-_-_-_" )
print ( "Código" , ' \t ' ' \t ' , "Nombre" , ' \t ' , "Curso" , ' \t ' ' \t ' ' \t ' , "Notas" , ' \t ' ' \t ' ' \t ' ' \t ' ' \t ' ' \t ' , "Promedio")
para  x  en  listaproductos :
    imprimir ( * x , fin = " \n " )
print ( "El promedio es: " , promedio )
