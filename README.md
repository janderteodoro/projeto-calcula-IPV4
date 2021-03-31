# projeto-calcula-IPV4 #
### Funcionamento e Objetivo ###
O objetivo deste pequeno projeto em Pythonm alémd e colocar os conhecimentos de POO em prática... É fazer com que nosso programa retorne configurações importantes como:
1. Números de hosts
2. Prefixo 
3. Número de Ips usados pela rede

Isso passando apenas o IP, máscara da redee e/ou prefixo. 

# Para essa mágica acontecer teremos que validar os IPs usando Expressões regulares e muita conversão de binário para decimal dentro do nosso programa. Aqui no README trarei um *resumão* do que vai rolar e seu funcionamento. #
---
### Você vai precisar de.. ###
* Conhecimentos da Linguagem Python 
    * POO 
    * Expressões Regulares 
    * List Compreenshion
* Ter a mesma instalada em seu computador 
* Entender o básico de Redes 
---

## Vamos lá ##
- [x] Nesta primeira parte da Nossa classe estou apenas validando nosso valores. Note que ja no inicializador ja chamei duas funções que faz com que eu já objetenha os valores desejáveis de cara, assim fica mais fácim eu rodar em app.py
![classe](https://user-images.githubusercontent.com/79011974/112920777-0374ea80-90e0-11eb-89ea-4c34fa8558e6.PNG)
---
- [x] Já nesta etapa já estamos fazendo a configuração de algumas coisas importantes da nossa classe. tais como:
* Prefixo não pode ser maior que 32 
* Configuramos alguns valores para binários com métodos que veremos a seguir 
* Forçamos alguns erros de Tipo e Valor quando as condições estabelecidas não são atendidas
![classe](https://user-images.githubusercontent.com/79011974/112922519-fdccd400-90e2-11eb-9438-bee8da77f8de.PNG)
---
- [x] Aqui realizamos algumas configurações interessantes como:
* Configuração do nosso IP através de expressões regulares 
* Convertemos IPs para binários, poré como precisamos de byte, ou seja (octetos) completamos com 0's restantes. 
* Utilizamos fatiamento e list compreenshions
![Capturar](https://user-images.githubusercontent.com/79011974/112923023-e0e4d080-90e3-11eb-997c-c98f194e7431.PNG)
---
## Exemplo de Runing ##
![rodando](https://user-images.githubusercontent.com/79011974/112923775-4a191380-90e5-11eb-8c85-f946c80d7cc8.PNG)
![res](https://user-images.githubusercontent.com/79011974/112923420-a891c200-90e4-11eb-9bbe-28319360ce91.PNG)4456256ce.PNG)
---
Ja em app.py eu imprimo as informações que eu preciso, no meun caso para exemplificar eu mostrei todas. 








