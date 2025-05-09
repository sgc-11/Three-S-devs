import time
import pyfiglet
from rich import print
from rich.table import Table
import typer
import cowsay
import base_datos
import checker
from cleanTerminal import limpiar_terminal

## Principal
def menu_principal():
    try:
        while True:
            limpiar_terminal()
            print("=" * 100)
            print(pyfiglet.figlet_format("MENU PRINCIPAL"))
            print("=" * 100)

            table = Table("Comando", "Descripción")
            table.add_row("1", "Registrar nuevo usuario")
            table.add_row("2", "Ver TODOS los usuarios registrados")
            table.add_row("3", "Buscar un usuario por su correo")
            table.add_row("4", "Salir de la aplicación")

            print(table)
            print("=" * 100)

            prompt = typer.prompt("Seleccione una opción [1-4]")
            prompt = checker.check_valid_option(prompt, 1, 4)
            while not prompt:
                print("La opcion seleccionada no es valida, vuelve a intentar")
                prompt = typer.prompt("Seleccione una opción [1-4]")

            match prompt:
                case 4:
                    if typer.confirm("¿Está seguro de que desea salir?"):
                        cowsay.ghostbusters("¡Que tengas un maravilloso día!")
                        raise typer.Exit(code = 1) # Exit cleanly
                
                case 3:
                    search_user_by_email()

                case 2: 
                    list_all_users()

                case 1:
                    add_user_menu()
       
    except typer.Exit as e:
        print(f"[bold green]Salida exitosa[/bold green]")


def add_user_menu():
    limpiar_terminal()

    print("=" * 100)
    print(pyfiglet.figlet_format("Registro de Usuario"))
    print("=" * 100)

    print("Recuerde que cada usuario debe contar con los siguientes atributos")
    user_table = Table("Atributos")
    user_table.add_row("nombre")
    user_table.add_row("correo electronico")
    user_table.add_row("numero de celular")
    print(user_table)

    print ("[bold red]Si en algun momento quieres devolverte al menu principal, escribe 4[/bold red]")
    print("-" * 100)
    
    name = typer.prompt("Ingrese el nombre")
    while not checker.is_valid_name(name):
        if name == "4":  return

        print("El nombre ingresado no es valido")
        name = typer.prompt("Ingrese el nombre")

    email = typer.prompt("Ingrese el correo")
    while not checker.classify_email(email):
        if email == "4":  return

        print("El email ingresado no es valido")
        email = typer.prompt("Ingrese el correo")

    number = typer.prompt("Ingrese el numero de celular")
    while not checker.is_valid_number(number):
        if number == "4":  return

        print("El numero ingresado no es valido")
        number = typer.prompt("Ingrese el numero de celular")

    print("Asi quedo el nuevo usuario")
    user_table = Table("Atributos", "Valos")
    user_table.add_row("nombre", name)
    user_table.add_row("correo electronico", email)
    user_table.add_row("numero de celular", number)
    print(user_table)

    if not typer.confirm("Esta seguro que lo quiere ingresar?"):
        add_user_menu()
        return
    
    base_datos.register_user(name, email, number)
    print("[bold green]Registro exitoso[/bold green]")

    time.sleep(2)


def list_all_users():
    limpiar_terminal()

    print("=" * 100)
    print(pyfiglet.figlet_format("Listado de usuarios"))
    print("=" * 100)

    users_table = Table("Rol", "Nombre", "Correo", "Numero celular")
    for user in base_datos.get_all_users():
        users_table.add_row(user.role.value, user.name, user.email, user.number)

    print(users_table)

    typer.prompt("Escriba cualquier cosa para retornar al menu principal")


def search_user_by_email():
    limpiar_terminal()

    print("=" * 100)
    print(pyfiglet.figlet_format("Buscar usuario(s) por correo"))
    print("=" * 100)

    input_email: str = typer.prompt("Ingrese el correo a buscar\nTenga en cuenta, que puede omitir (o no) la parte del dominio " \
    "del correo (derecha del @) y el @.\nEsto ya que siempre se va a poner el correo como terminado en '@utv.edu.co'")

    input_email = input_email.split("@")[0] + "@utv.edu.co"  # Get only the local part and append it the correct domain.


    users_table = Table("Rol", "Nombre", "Correo", "Numero celular")
    for user in base_datos.search_user_by_email(input_email):
        users_table.add_row(user.role.value, user.name, user.email, user.number)

    print("\n\nLos usuarios cuyos correos coinciden con lo buscado son")
    print(users_table)

    typer.prompt("Escriba cualquier cosa para retornar al menu principal")
