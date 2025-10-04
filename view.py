from controller import Controller


class View:

    def __init__(self):
        self.controller = Controller()
        self.loop = True
        

    def app_init(self):
        while self.loop:
            try:
               
               if self.controller.load_data.filename is  None:
                    self.load_data_menu()
                
               self.algorithm_menu()


                   
            except ValueError:
                print("Entrada inválida: escriba solo números")
                return
            except Exception as e:
                print("Ocurrió un error inesperado:", str(e))
                return

    def load_data_menu(self):
        filename = input("Escriba el nombre del archivo (en carpeta inputs): ")
        try:
            self.controller.load_data_txt(f"./inputs/{filename}")
            print("Datos cargados correctamente")
        except FileNotFoundError:
            print("No se encontró el archivo, intente de nuevo")

    def algorithm_menu(self):
        print("\nEscoja el número del algoritmo:")
        print("1. rocFB\n2. rocV\n3. rocPD\n4. cargar una nueva entrada\n5. salir")

        try:
            choice = int(input("> "))
            match choice:
                case 1: 
                    self.controller.find_solution("rocFB")
                    self.show_results()
                case 2: 
                    self.controller.find_solution("rocV")
                    self.show_results()         
                case 3: 
                    self.controller.find_solution("rocPD")
                    self.show_results()
                case 4: self.load_new_input()
                case 5: self.exit_app()
                case _: print("Elija una opción válida"); return
        except ValueError:
            print("Entrada inválida")

        

    def show_results(self):
        print("\nEstos son los datos cargados:\n")
        self.controller.print_loaded_data()
        print(f"\nSolución usando {self.controller.executed_algorthrim}:")
        self.controller.print_solution()
        self.controller.write_solution()

    def exit_app(self):
        print("Gracias por usar este programa")
        self.loop = False

    def load_new_input(self):
        self.controller.load_data.clear_data()
        self.load_data_menu()


             
                    
                


