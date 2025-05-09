import pyfiglet
from rich import print
from rich.table import Table
import typer
import cowsay
import checker

## Principal
def menu_principal():

    print("=" * 100)
    print(pyfiglet.figlet_format("MENU PRINCIPAL"))
    print("=" * 100)

    table = Table("Comando", "Descripción")
    table.add_row("1", "Registrar nuevo usuario")
    table.add_row("2", "Ver TODOS los correos registrados")
    table.add_row("3", "Buscar un usuario por su correo")
    table.add_row("4", "Salir de la aplicación")

    print(table)
    print("=" * 100)

    try:
        while True:
            prompt = typer.prompt("Seleccione una opción [1-4]")
            prompt = checker.check_valid_option(prompt, 1, 4)
            if not prompt:
                print("La opcion seleccionada no es valida, vuelve a intentar")
                continue

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
        print(f"[bold green]Successfull exit[/bold green]")


def add_user_menu():
    pass


def list_all_users():
    pass


def search_user_by_email():
    pass