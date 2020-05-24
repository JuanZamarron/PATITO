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
Para ejecutar un probrama en patito++ es necesario:



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


### Tipo de Datos

### Strings

### Condicionales

### Asignacion

### Repeticion

### Expresiones

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

### Nuestro Timeline

### Conclusiones










* lex.py => reserved, tokens y expresiones regulares
* yacc.py => gramatica
