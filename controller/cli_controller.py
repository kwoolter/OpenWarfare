import cmd
import model
import view
import utils

class OWControllerCLI(cmd.Cmd):

    intro = "Welcome to the Open Warfare.\nType 'start' to get going!"
    prompt = "What next?"

    def __init__(self):
        super(OWControllerCLI, self).__init__()

        self.model = None

    def do_start(self, args):
        self.model = model.OWGame()
        self.model.initialise()

    def do_print(self, args):
        """Print the game"""
        print("Printing...")

        if self.model is None:
            raise Exception("No game to print.")

        self.model.print()

        text_view = view.OWMapView(self.model)
        text_view.draw_map()


    def do_quit(self, args):
        """Quit the game"""
        if utils.confirm("Are you sure you want to quit?"):
            exit(0)
