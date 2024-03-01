
import typer
from serial.tools import list_ports
import inquirer
from yaspin import yaspin

from robo import Arm

#Define alguns parâmetros (Instânciando Typer, Definindo o Spiner e Listanto as portas).
app = typer.Typer()
spinner = yaspin(text="Processando...", color="yellow")
available_ports = list_ports.comports()

#Cria a possibilidade do usuário escolher a porta de entrada do robo.
chosen_port = inquirer.prompt([
    inquirer.List("porta", message="Escolha a porta serial", choices=[x.device for x in available_ports])
])["porta"]

#Instancia a biblioteca do robo.
robot = Arm(port=chosen_port, verbose=False)

# Variável que será checada enquanto o robo estiver rodando
running = True

#Comando/função que sera iniciado assim que o programa for rodado
@app.command()
def interative_mode():
   
   #Tem a função de checar a variável Running e rodar a função chosen_function enquanto running = True
   global running
   while running:
       chosen_function()

# Função responsável por deixar o usuário escolher qual funcionalidade do robo ele irá querer utilizar, além de chamar a função escolhida.
def chosen_function():
    chosen_function = inquirer.prompt([
        inquirer.List("funcao", message="Escolha uma das ações a seguir:", choices=["Initialize tool", "Turn off tool","Home","Move", "Actual location", "Turn off robot"])
    ])["funcao"]

    if chosen_function == "Initialize tool":
       initialize_tool()

    elif chosen_function == "Turn off tool":
        turn_off_tool()

    elif chosen_function == "Home":
        home()

    elif chosen_function == "Move":
        move()

    elif chosen_function == "Actual location":
        actual_location()

    elif chosen_function == "Turn off robot":
        turn_off_tool()

# Função responsável por iniciar a ferramenta conectado ao robo
def initialize_tool():
    spinner.start()
    robot.wait(200)
    robot.suck(True)
    spinner.stop()

# Função responsável por desligar a ferramenta conectado ao robo
def turn_off_tool():
    spinner.start()
    robot.wait(200)
    robot.suck(False)
    spinner.stop()

# Função responsável por levar ao robo de volta a posição inicial
def home():
    spinner.start()
    robot.wait(300)
    robot.movej_to(230, 1, 159, 0, wait=True)
    spinner.stop()

# Função responsável por mover o robo para a distância e eixo escolhido pelo usuário
def move():
    actual_position = robot.pose()
    x,y,z,w = actual_position[:4]
    
    chosen_axle = inquirer.prompt([
    inquirer.List("axle",message="Para qual eixo você quer que o robo se mova: ", choices=["Eixo X","Eixo Y", "Eixo Z"])
    ])["axle"]

    chosen_distance = inquirer.prompt([
    inquirer.Text("distance",message="Digite a distância do movimento desejado: ")
    ])["distance"]

    if chosen_axle == "Eixo X":
        spinner.start()
        robot.wait(300)
        robot.movej_to(x + float(chosen_distance), y, z, w, wait=True)
        spinner.stop()
    
    elif chosen_axle == "Eixo Y":
        spinner.start()
        robot.wait(300)
        robot.movej_to(x, y + float(chosen_distance), z, w, wait=True)
        spinner.stop()
    
    elif chosen_axle == "Eixo Z":
        spinner.start()
        robot.wait(300)
        robot.movej_to(x, y, z + float(chosen_distance), w, wait=True)
        spinner.stop()

# Função responsável por mostrar no console a localização atual do robo
def actual_location():
    actual_position = robot.pose()
    print(f"The actual robot position is: {actual_position}")

# Função responsável fechar o looping e fechar a conexão com robo
def turn_off_robot():
    global running
    running = False

if __name__ == "__main__":
    app()