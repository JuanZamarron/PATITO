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
        { 
            principal(){
                escribir("Hola mundo!");
            }
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
        var int x;
            float y;
            char z; 
            int matriz[3][3];
        
         { 
            principal()
            {
                escribir("Hola Variables!");
            }
        }    

- inicializando una funcion x a  0

        programa ejemplodos;
        var int x;
   
        principal()
        {
        x = 100;
            escribir("Hola Variables Gobales con valor: ", x);
        }
  
  
- Llamando una función desde principal

        programa ejemplotres;
        var int x;
         { 
            funcion void nombreFuncion(int data)
              var 
                int x_local;
                float y_local;
                char z_local; 
                inr matriz_local[3][3];
            {
                escribir("Hola Desde funcion con valor:", data);
            }
            
            principal()
            {
            x = 1;
                nombreFuncion(x);
            }
        }
       


### Tipo de Datos y Operadores

Dentro del desarrollo de Patito++ contamos con 6 tipos de datos:
1. int
    
            principal()
            var int variable;
            {
                variable = 1;
                escribe(variable)
            }
    
2. char
    
            principal()
            var char variable;
            {
                variable = "a";
                escribe(variable)
            }
3. float
    
            principal()
            var float variable;
            {
                variable = 45.0;
                escribe(variable)
            }
4. boolean
    
            principal()
            var boolean variable;
            {
                variable = true;
                escribe(variable)
            }
5. arreglos
    
            principal()
            var int arr[10];
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
            int i;
            string j;
            
        principal()
        {
        i = 0;
        j = "Nada";
        
        escribe("Valor de i: ",i);
        escribe("Valor de j: ",j);
        
        i=3;
        j = "valor de j";
        escribe("Nuevo valor de i: ", i);
        escribe("Nuevo valor de j: ",j);
        }

 ### Repeticion
    programa patito;
        var int arr[10];
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

        principal()
        var int variable;
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



