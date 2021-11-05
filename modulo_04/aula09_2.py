## Separando arquivos em PDF

import PyPDF2


with open(r'C:\Users\joys-\OneDrive\FIAP\BI_FIAP.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f' r"C:\Users\joys-\OneDrive\FIAP\BI_FIAP.pdf"/{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)