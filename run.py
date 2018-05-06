import logging
import controller

def main():
    logging.basicConfig(level=logging.WARN)
    logging.info("Open Warfare starting...")

    c = controller.OWControllerCLI()
    c.cmdloop()

if __name__ == "__main__":
    main()


