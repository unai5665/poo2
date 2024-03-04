## Apunted de Programación Orientada a Objetos
https://aprendepython.es/core/modularity/oop/

### Encapsulamiento
Permite empaquetar el código dentro de una unidad (objeto) donde se puede determinar el ámbito de actuación.
### Abstracción
Permite generalizar los tipos de objetos a través de las clases y simplificar el programa.
### Herencia
Permite generalizar los tipos de objetos a través de las clases y simplificar el programa.
### Polimorfismo
Permite crear múltiples objetos a partir de una misma pieza flexible de código.
## Apuntes de Markdown
https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax



![](https://aprendepython.es/_images/oop.jpg)


### Diagram Class
https://mermaid.js.org/syntax/classDiagram.html

---
title: Animal example
---
classDiagram
    note "From Duck till Zebra"
    Animal <|-- Duck
    note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
    class Fish{
        -int sizeInFeet
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }

    