import pdfkit
from jinja2 import Environment, FileSystemLoader
import os


def generate_pdf(data):
    # Configura o Jinja2 para buscar os templates no diretório atual
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('general_pdf.html')

    # Dados para preencher no template
    context = {
        'image_url': os.path.abspath('heraldica.jpg'),
        'header_line_1': 'MARINHA DO BRASIL',
        'header_line_2': 'ESCOLA NAVAL',
        'header_line_3': 'COMANDO DO CORPO DE ASPIRANTES',
        'title': 'Súmula da XXX Meia-Maratona de Canoagem da Escola Naval',
        'table_title': data['table_title'],
        'table_data': data['table_data']
    }

    # Renderiza o template com os dados
    html_content = template.render(context)

    # Gera o PDF com pdfkit
    pdf_bytes = pdfkit.from_string(html_content, False, options={'enable-local-file-access': ''})
    #pdfkit.from_file(html_content, 'output.pdf'
    return pdf_bytes


if __name__ == '__main__':
    # Exemplo de uso:
    data = {
        'image_url': os.path.abspath('heraldica.jpg'),
        'header_line_1': 'MARINHA DO BRASIL',
        'header_line_2': 'ESCOLA NAVAL',
        'header_line_3': 'COMANDO DO CORPO DE ASPIRANTES',
        'title': 'Súmula Oficial da XXX  Meia Maratona de Canoagem',
        'table_title': 'Surfski Individual Masculino Sub-20',
        'table_headers': ['Posição', 'Nome', 'Tempo'],
        'table_data': [
            ['1º', 'Atleta 1', '01:21:00'],
            ['2º', 'Atleta 2', '01:22:00'],
            ['3º', 'Atleta 3', '01:23:00'],
        ]
    }

    generate_pdf(data)
