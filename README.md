## Tabla de contenido

* [Acerca del proyecto](#acerca-del-proyecto)
    * [Para empezar](#para-empezar)
        * [Prerrequisitos](#prerrequisitos)
        * [Instalación](#instalación)
* [Autor](#autor)
* [Licencia](#licencia)

# Acerca del proyecto

Aplicación que a partir de las características de un crédito (monto y el plazo) muestre la TMC que corresponde.

## Para empezar

Es necesario bajarse el proyecto:

```
git pull git@github.com:joselrodrigues/TMC-app.git
```

### Prerrequisitos

Tener python 3 y virtualenv instalados, en caso de no tenerlos se pueden optener en: 

* [Python 3](https://www.python.org/downloads/)
* [Virtualenv](https://github.com/pypa/virtualenv)

Si te encuentras en linux(Ubuntu) se pueden instalar mediante:

```
sudo apt-get install python3.6
pip3 install virtualenv
```

### Instalación

Para generar un entorno virtual para el proyecto ejecutar:

```
virtualenv env
source env/bin/activate
```

Luego instalar las dependencias necesarias para la ejecución:

```
pip install requirements.txt
```

## Autor

* **Jose Luis Rodrigues** - [joselrodrigues](https://github.com/joselrodrigues)


## Licencia

Este proyecto esta bajo MIT License - para ver mas detalles puedes consultar [LICENSE](LICENSE) 

