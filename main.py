import typer
import menus
import cleanTerminal

def main():
    cleanTerminal.limpiar_terminal()
    menus.menu_principal()


if __name__ == "__main__":
    typer.run(main)

