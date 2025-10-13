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
        filename = input("Escriba el nombre del archivo (en carpeta inputs Ejemplos: test_1.txt): ")
        try:
            self.controller.load_data_txt(f"./inputs/{filename}")
            print("\nDatos cargados correctamente!!!")
            print("\nEstos son los datos cargados:")
            self.controller.print_loaded_data()
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
                case 4: self.controller.load_data.clear_data()
                case 5: self.exit_app()
                case _: print("Elija una opción válida"); return
        except ValueError:
            print("Entrada inválida")

        

    def show_results(self):
        print(f"\nSolución usando {self.controller.executed_algorthrim}:")
        print("----------------------------------")
        self.controller.print_solution()
        self.controller.write_FB_solution()
        print("----------------------------------\n")

    def exit_app(self):
        print("Gracias por usar este programa")
        self.loop = False

    
        
       


             
                    
                


