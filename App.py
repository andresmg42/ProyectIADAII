import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # Para usar ComboBox
from controller import Controller

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto 1 ADAII")
        self.controller = Controller()

        # Crear widgets
        self.create_widgets()

    def create_widgets(self):
        # Botón para cargar datos
        self.load_button = tk.Button(self.root, text="Cargar Datos", command=self.load_data)
        self.load_button.pack(pady=10)

        # Área de texto para mostrar los resultados
        self.results_text = tk.Text(self.root, height=20, width=50)
        self.results_text.pack(pady=10)

        # ComboBox para seleccionar el algoritmo
        self.algorithm_label = tk.Label(self.root, text="Selecciona el algoritmo")
        self.algorithm_label.pack(pady=5)

        self.algorithm_combobox = ttk.Combobox(self.root, values=["Brute Force (rocFB)", "Dinámico (rocPD)", "Voraz (rocV)"])
        self.algorithm_combobox.set("Brute Force (rocFB)")  # Establece por defecto el algoritmo
        self.algorithm_combobox.pack(pady=5)

        # Botón para ejecutar las soluciones
        self.run_button = tk.Button(self.root, text="Ejecutar Pruebas", command=self.run_benchmark)
        self.run_button.pack(pady=10)

        # Botón para guardar los resultados en un archivo
        self.save_button = tk.Button(self.root, text="Guardar Informe", command=self.save_report)
        self.save_button.pack(pady=10)

    def load_data(self):
        # Mostrar un cuadro de diálogo para seleccionar un archivo
        file_path = filedialog.askopenfilename(title="Seleccionar archivo de datos", filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                self.controller.load_data_txt(file_path)
                self.display_results(f"Datos cargados desde: {file_path}\n{self.controller.load_data.content}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar datos: {e}")

    def run_benchmark(self):
        # Obtener el algoritmo seleccionado
        selected_algorithm = self.algorithm_combobox.get()
        
        # Mapear el nombre del algoritmo a la forma en que lo espera el controlador
        algorithm_map = {
            "Brute Force (rocFB)": "rocFB",
            "Dinámico (rocPD)": "rocPD",
            "Voraz (rocV)": "rocV"
        }
        
        selected_algorithm_key = algorithm_map.get(selected_algorithm, "rocFB")  # Default a Brute Force

        # Ejecutar el algoritmo seleccionado
        try:
            self.controller.find_solution(selected_algorithm_key)
            
            # Mostrar los resultados en el área de texto de la GUI
            # result_text = f"Solución: {self.controller.solution}\nTiempo de ejecución: {self.controller.time:.4f} segundos"

            text_sol=f'Algoritmo ejecutado: {self.controller.executed_algorthrim}\n'
            text_sol+=f'Valor Solucion: {self.controller.solution['min']}\n'
            text_sol=text_sol +'------------------------------------------------\n'
            text_sol=text_sol + 'Solucion: \n'
            for est in self.controller.solution['solution']:
                text_sol+=est.return_info_sol() +'\n'

            

            self.display_results(text_sol)
            

        except Exception as e:
            messagebox.showerror("Error", f"Error al ejecutar las pruebas: {e}")

    def display_results(self, text):
        # Mostrar los resultados en el área de texto de la GUI
        self.results_text.delete(1.0, tk.END)  # Limpiar el área de texto
        self.results_text.insert(tk.END, text)

    def save_report(self):
        # Guardar los resultados en un archivo

        print('excecuted algorithm:',self.controller.executed_algorthrim)
        try:
            match self.controller.executed_algorthrim:
                case 'rocFB':
                    path='outputs/brute_force'
                case 'rocPD':
                    path='outputs/dinamic'
                case 'Voraz':
                    path='outputs/voraz'
                case _: 
                    path='outputs'
             
            self.controller.write_solution_controller(path)
            messagebox.showinfo('Informacion guardado',f"Informe guardado exitosamente!")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el informe: {e}")

# Crear la ventana principal de la aplicación
root = tk.Tk()
app = App(root)
root.mainloop()


