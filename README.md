# dtrepat_PAC44

## Introducció
Projecte corresponent a la PAC4 de l'assignatura de 22.403 - Programació per a la ciència de dades de la UOC.

Concretament, el projecte tracta i analitza dades sobre l'Orbea Monegros, una prova de ciclisme de muntanya (BTT) no competitiva que es realitza a Sariñena (Osca).


## Instal·lació i posada en funcionament
Passos per instal·lar el projecte:

1. Clona el repositori a la teva màquina local (en cas que l'hagis descarregat, saltat aquest pas)

```bash
git clone https://github.com/trepi93/dtrepat_PAC4
```

2. Navega fins al directori on s'ha descarregat el projecte (si l'has descarregat (sense usar git clone) descomprimeix-lo)
```bash
cd dtrepat_PAC4
```
3. Instal·la les dependències necessaries (es recomana crear un virtual enviroment per fer-ho)

(Opcional) Passos per crear un virtual enviroment 
a. Si s'executa amb linux
```bash
virtualenv venv
source venv/bin/activate
```
(Opcional)
b. Si s'executa amb Windows
```bash
python3 -m venv venv
venv\Scripts\activate
```
En qualsevol cas, instal·la les dependències fent:
```bash
python3 -m venv venv
venv\Scripts\activate
```





## Estructura del Projecte
Explicació de com està organitzat el codi.

```
nom-del-repositori/
├── src/             # Codi font
├── tests/           # Tests del projecte
├── docs/            # Documentació
├── README.md        # Aquest fitxer
└── package.json     # O requirements.txt
```

## Com executar-lo
Instruccions per iniciar l'aplicació:

```bash
npm start  # O python main.py, segons el llenguatge
```

## Tests
Com executar els tests:

```bash
npm test  # O pytest, unittest, etc.
```

## Contribucions
Guia per contribuir al projecte.

## Llicència
Tipus de llicència i drets d'ús.

