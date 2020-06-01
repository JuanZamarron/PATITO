# Manual de Patito ++
El lenguaje de programación Patito++  es un lenguaje imperativo especial
que desarrollamos como parte de nuestro proyecto final de la materia de 
Diseño de Compiladores .

### Librerías usadas YACC & Lex
* lex.py => reserved, tokens y expresiones regulares
* yacc.py => gramatica

### Hola mundo
Una función simple que puede correrse con Patito ++ es parecida a la siguiente línea de código:

        programa holamundo;
        principal(){
            escribe("Hola mundo!");
        }
      

cada programa escrito en patito ++ debe contener un nombre de programa y
una "función" obligatoria llamada principal.

### Compilación y Running de Patito++
#### Last update: 29 may 2020 (esto puede cambiar)
Para ejecutar un probrama en patito++ es necesario:
- Ejecutar las siguientes funciones:´
            
            
            python3 yacc.py    


A continuación  el programa te pedirá un Programa de prueba para ejecutar.
Deberás ingresar el nombre del archivo que deseas probar. Este archivo debe estár 
situado dentro de la carpeta: **/Pruebas**  y debe tener extención: **.txt** 

El programa pocederá a compilar el programa y verificará la sintaxis y semantica del código. 
Una vez finalizada la verificación se generará un archivo dentro de la carpeta **/compiledCode**
con el mismo nombre que el archivo anteriormente ejecutado. Éste archivo será nuestro ejecutable para
llevar a cabo las tareas del programa. Para correrlo hay que ejecutar el siguiente comando:
            
            
            python3 maquinaVirtual/actions.py     


Finalmente nuestro archivo se ejecutará con las instrucciones llevadas a cabo en nuestro programa. Incluyendo errores.

### Declaración de variables
Para crear una variable en Patito ++ se encuentran un par de formas:
- Creando una variable global:

            programa ejemplouno;
            var
                int x;
                float y;
                char z;
                int matriz[3][3];
            
            principal()
            {
                escribe("Hola Variables!");
            }
              

- inicializando una funcion x a  100

            programa ejemplodos;
            var int x;
            
            principal()
            {
            x = 100;
                escribe("Hola Variables x con valor: ", x);
            }
  
  
- Llamando una función desde principal

            programa ejemplotres;
            var int x;
            
            funcion void mifuncion(int data)
            {
                escribe("Hola Desde funcion un parametro de valor :", data);
            }
            
            principal()
            {
            x = 123;
                mifuncion(x);
            }
                    
       
### Tipo de Datos y Operadores

Dentro del desarrollo de Patito++ contamos con 6 tipos de datos:
1. int

            programa integer;
            var int variable;
            
            principal()
            {
                variable = 200;
                escribe(variable);
            }

            
2. char
    
            programa charprogram;
            var char variable;
            
            principal()
            {
                variable = 'h';
                escribe(variable);
            }

3. float
    
            programa floatprogram;
            var float variable;
            
            principal()
            {
                variable = 2.0;
                escribe(variable);
            }
            

4. arreglos
            programa arreglosprogram;
            var int a[100], n,i;
            
            principal()
            {
                escribe("Ingresa el tamaño del arreglo:");
                lee(n);
                escribe("Ingresa los elementos del arreglo:");
            
                desde i=0 hasta (n-1) hacer {
                    lee(a[i]);
                }
                    escribe("El Arreglo es:");
            
                desde i=0 hasta (n-1) hacer {
                    escribe(a[i]);
                }
            }

5. arreglos (Ejemplo 2)

            programa arreglosprogram;
            var int a[100];
                char b[100];
                float c[100];
            
            principal()
            {
                a[0] = 10;
                b[0] = 'H';
                c[0] = 24.5;
                escribe( "Arreglo int: ", a[0]);
                escribe( "Arreglo char: ", b[0]);
                escribe( "Arreglo double: ", c[0]);
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
                        int i;
                        char j;
            
            principal()
            {
                i = 0;
                j = 'R';
            
                escribe("Valor de i: ",i);
                escribe("Valor de j: ",j);
            
                i = 3;
                j = 'J';
                escribe("Nuevo valor de i: ", i);
                escribe("Nuevo valor de j: ",j);
            }

 ### Repeticion
    programa patito;
        var int arr[10],i;
        principal()
        {
            desde i = 0 hasta (9) hacer {
                arr[i] = i;
            }
            desde i = 0 hasta (9) hacer {
                escribe(arr[i]);
            }
        }
        

### Condicionales (si.. sino)

        programa sinoejemplo;
        var int variable;
        principal()
        {
            variable = 10;
            si(variable == 10) entonces{
                escribe("Es igual a 10");
            }sino{
                escribe("Es diferente a 10");
            }
        }




### Ejemplo General FIBONACCI Iterativo y Recursivo
        programa fibonacci;
           var int x , i, des;
        
        funcion int fibrecursive(int j)
        {
           si(j <= 1) entonces
           {
            regresa(j);
           }sino {
              regresa( fibrecursive(j-1) + fibrecursive(j-2));
           }
        
        }
        
        funcion void fib(int n)
         var int x, y, z;
        {
            x = 0;
            y = 1;
            z = 0;
           desde i = 0 hasta (n-1) hacer {
              escribe(x);
              z = x + y;
              x = y;
              y = z;
            }
        }
        
        principal()
        {
           i = 0;
           escribe("Ingresa en número de repeticiones de la serie:");
           lee(x);
           escribe("Ingresa 1 si quieres que la función sea recursiva ó cualquier otro número si quieres que sea iterativa:");
            lee(des);
            escribe("Fibonnaci Serie: ");
            si(des == 1) entonces{
                mientras (i < x) haz
                   {
                      escribe(fibrecursive(i));
                      i = i + 1;
                   }
            }sino{
                escribe("Fibonnaci Series : ");
                fib(x);
            }
        
        }



