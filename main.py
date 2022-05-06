printer_connection = None
printer_commands = []
printer_response = []


def program_start():
    program_initialization()
    clear_values()
    connect_to_printer()
    send_printer_commands()
    retrieve_printer_response()
    report_results()
    terminate_program()


def program_initialization():
    printer_connection = Printer3D() # Connect to the printer
    printer_connection.initialize()

    printer_commands = argv[1:] # Load printer commands from arguments


def clear_values():
    printer_commands.clear()
    printer_response.clear()


def connect_to_printer(): # Connect to the 3D printer
    status = printer_connection.connect()
    assert status == 0, "Could not connect to the printer"


def send_printer_commands():
    for command in printer_commands: # Send print commands to the printer
        printer_connection.send_data(command)

def retrieve_printer_response():

    while printer_connection.has_data(): # Fetch status from the printer
        printer_response.append(printer_connection.receive())


def report_results():

    for i, result in enumerate(printer_response): # Print out the response from the printer
        print("Pass %s: %s" % (i, result))


def terminate_program():
    printer_connection.close() # Close connection with printer


if __name__ == '__main__':
    program_start()
