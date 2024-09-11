import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import tkinter as tk
from usuarios import Usuarios
from clientes import Cliente
from cidade import Cidade

def exportar_para_pdf():
    pdf_file = "conteudo_exportado.pdf"

    with PdfPages(pdf_file) as pdf:
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Gráfico do Relatorio')
        pdf.savefig()

        plt.close(fig)
    print("PDF exportado com sucesso.")


root = tk.Tk()
root.title("Exportar para PDF")
botao_exportar = tk.Button(root, text="Exportar gráfico para PDF", command=exportar_para_pdf)
botao_exportar.pack()
root.mainloop()
