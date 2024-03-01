# Ponderada Construção de Interface por Linha de Comando (CLI) para Controle do Robô

&emsp;Desenvolvido por Breno Arthur Guimarães Santos

## Descrição

&emsp; Nessa protópido pedido na ponderada, utilizei as bibliotecas recomendadas pelo professor (Uma adaptação do pydobot, yaspin, inquirer e o typer).

&emsp; O código foi todo segmentado em funções, que possuem as seguintes responsabilidades:

- `def interative_mode`: Comando/função que sera iniciado assim que o programa for rodado. Tem a função de checar a variável Running e rodar a função chosen_function enquanto running = True
- `def chosen_function`: Função responsável por deixar o usuário escolher qual funcionalidade do robo ele irá querer utilizar, além de chamar a função escolhida.
- `def initialize_tool`: Função responsável por iniciar a ferramenta conectado ao robo
- `def turn_off_tool`: Função responsável por desligar a ferramenta conectado ao robo
- `def home`: Função responsável por levar ao robo de volta a posição inicial
- `def move`: Função responsável por mover o robo para a distância e eixo escolhido pelo usuário
- `def actual_location`: Função responsável por mostrar no console a localização atual do robo
- `def turn_off_robot`: Função responsável fechar o looping e fechar a conexão com robo

&emsp;Os comandos disponíveis para o usuário são:
- `Initialize tool`
- `Turn off tool`
- `Home`
- `Move`
- `Actual location`
- `Turn off robot`

&emsp; Para executaro código, o usuário deve utilizar um terminal de sua preferência e apenas executar o comando: `python main.py`, então selecionar a porta conectada ao robo e portanto as funções de sua preferência. 

&emsp; Link para vissualização do funcinamento do robô com a CLI: [https://drive.google.com/file/d/1TU8oD0VU6_lfuAdFZrnXiPnQFrDfvq-5/view?usp=sharing]()
