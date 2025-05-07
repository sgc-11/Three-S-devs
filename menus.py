import pyfiglet
from rich import print
from rich.table import Table
import typer
import cowsay

def menu_principal():

    print("=" * 50)
    print(pyfiglet.figlet_format("MENU PRINCIPAL"))
    print("=" * 50)

    table = Table("Comando", "Descripción")
    table.add_row("1", "Registrar nuevo correo")
    table.add_row("2", "Ver TODOS los correos registrados")
    table.add_row("3", "Buscar UN correo registrado")
    table.add_row("4", "Salir de la aplicación")

    print(table)
    print("=" * 20)

    try:
        while True:
            prompt = typer.prompt("Seleccione una opción [1-4]")
            if prompt.lower() in ["4"]:
                if typer.confirm("¿Está seguro de que desea salir?"):
                    cowsay.ghostbusters("¡Que tengas un maravilloso día!")
                    raise typer.Exit() # Exit cleanly
                
    except Exception as e:
        print(f"[bold red]An error ocurred: {str(e)}[/bold red]")





