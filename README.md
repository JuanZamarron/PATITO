# Manual de Patito ++
El lenguaje de programación Patito++  es un lenguaje imperativo especial
que desarrollamos como parte de nuestro proyecto final de la materia de 
Diseño de Compiladores .

### Hola mundo
Una función simple que puede correrse con Patito ++ es parecida a la siguiente línea de código:

        programa holamuno;
            { 
            principal(){
                escribir("Hola mundo!");
            }
        }    


cada programa escrito en patito ++ debe contener un nombre de programa y
una "función" obligatoria llamada principal.

### Compilación y Running de Patito++
#### Last update: 23 may 2020 (esto puede cambiar)
Para ejecutar un probrama en patito++ es necesario:
- Crear un archivo **txt**  en la carpeta /Pruebas y dentro del archivo
'lex.py', en la linea  137 agregar el nuevo nombre del archivo como se ve 
a continuación:

        prueba = open('Pruebas/MiNuevaPrueba.txt', "r")
        archivo = 'Pruebas/MiNuevaPrueba.txt'
Una vez cambiados el archivo .txt, procederemos a ejecutar el comando:
         
         python3 yacc.py    

Enseguida laterminal ejecutará lo que se encuentra en el código y mostrará si
las validaciones semanticas y sintácticas se ejecutan de maneta exitosa o no.

### Declaración de variables
Para crear una variable en Patito ++ se encuentran un par de formas:
- Creando una variable global:

        programa global;
        var int x, float y, char z, matriz[3][3];
         { 
            principal()
            {
                escribir("Hola Variables Gobales!");
            }
        }    

- Creando una variable local a la funcion principal

        programa local;
         { 
            principal()
              var int x_local, float y_local, char z_local, matriz_local[3][3];
            {
                escribir("Hola Variables Locales!");
            }
        }
- inicializando una funcion con x datos

        programa mifuncion;
         { 
            funcion mifuncion(int x, int y){
                escribir("Hola Iniciación de Variables en Funciones!");
            }
         
            principal()
            {
                mifuncion(3,5)
            }
        }


### Tipo de Datos y Operadores

Dentro del desarrollo de Patitp++ contamos con 6 tipos de datos:
1. int
    
            principal()
            var int variable = 1;
            {
                escribe(variable)
            }
    
2. string
    
            principal()
            var string variable = "hola string";
            {
                escribe(variable)
            }
3. char
    
            principal()
            var char variable = "a";
            {
                escribe(variable)
            }
4. float
    
            principal()
            var float variable = 45.0;
            {
                escribe(variable)
            }
5. boolean
    
            principal()
            var boolean variable = true;
            {
                escribe(variable)
            }
6. arreglos
    
            principal()
            int arr[10];
            {
                escribe("Así se instancía un arreglo.")
            }
            
          
De igual manera el lenguaje acepta los siguientes operadores logicos:
- "<"
- ">"
- "<="
- ">="
- "=="
- "!="
- &&
- ||

### Lectura y Escritura
El lenguaje soporta los estatutos **escribe()** y **lee()**, los cuales son los encargados de que el usuario pueda imprimir en pantalla y almacenar datos introducidos por el mismo

#### Lectura
La lectura se realiza a traves de la palabra `lee`, con la cual el usuario podra almacenar un valor ingresado, como se muestra a continuación:

    lee(variable);
    
El input solo puede tener una variable previamente declarada dentro del parentesis, en la cual se almacenara el valor introducido

#### Escritura
La escritura se realiza a traves de la palabra `escribe`, con la cual el usuario sera capaz de imprimir en pantalla el valor de una variable o un string, como se muestra a continuación:

    escribe("Esto imprime un string");
    
### Asignacion
    programa patito;
        var
            int i = 0;
            string j = "Nada";
            
        principal()
        {
        escribe("Valor de i: ",i);
        escribe("Valor de j: ",j);
        i=3;
        j = "valor de j";
        escribe("Nuevo valor de i: ", i);
        escribe("Nuevo valor de j: ",j);
        }

 ### Repeticion
    programa patito;
        var int arr[10]; %%Variable gobal
        principal()
        {
            for(i = 0; i < 10; ++i)
            {
               arr[i] = i;
            }
            
            for(i = 0; i < 10; ++i)
            {
               escribe(arr[i]);
            }
        }
        

### Condicionales (si.. sino)

        principal()
        var int variable 10;
        {
             si(variable == 10) entonces{
                escribe("Es igual a 10");
             }sino{
                escribe("Es diferente a 10");
             }
        }


### Otras caracteríticas


### Ejemplo General
        programa patito;
        var
            int i, j, p, k;
            int Arreglo[10], OtroArreglo[10];
            float valor;
            int Matriz[3][8], OtraMatriz[3][3];
        
            funcion int fact (int j)
            var int i;
            {
                i=j + (p-j*2+j);
                si(j==1) entonces{
                    regresa(j);
                }sino{
                    regresa(j * fact(j-1));
        
                }
            }
        
            funcion void inicia(int y)
            var int x;
            {
                x=0;
                mientras (x < 11) haz {
                   Arreglo[x] = y*x;
                   x=x+1;
                }
            }
        
           principal(){
           lee(p); j=p*2;
           inicia(p * j - 5);
           desde i = 0 hasta 9 hacer {
            Arreglo[i] = Arreglo[i] * fact(Arreglo[i] - p);
           }
           desde j = 0 hasta 2 hacer{
                desde k = 0 hasta 7 hacer{
                        escribe("loop");
                   }
           }
        
           desde j=0 hasta 2 hacer{
                desde k = 0 hasta 2 hacer{
                    OtraMatriz[j,k]=k + j;
                }
                valor = 2.0;
                escribe("el determinante es:", valor);
                mientras(i+2 >= 3+0)haz{
                    escribe("resultado", Arreglo[i], fact(i+2) * valor);
                    i = i - 1;
                }
           }



# Sobre el Desarollo
### Lenguaje báse

### Librerías usadas YACC & Lex
* lex.py => reserved, tokens y expresiones regulares
* yacc.py => gramatica

### Nuestro Timeline

### Conclusiones




