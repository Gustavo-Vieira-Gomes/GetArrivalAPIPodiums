import streamlit as st
import requests
import get_podiums



def main():
   st.title("Gerador de PDFs por Categorias")
   api_url = 'https://api.sapn.com.br/api/v1/arrivals/podiums/list/'
   if st.button("Gerar PDFs"):
        
        response = requests.get(api_url)
        if response.status_code == 200:
            st.success("Dados recebidos com sucesso!")
            json_data = response.json()  # Recebendo o JSON

            # Iterando sobre as categorias no JSON
            pdf_files = {}
            for category in json_data:
                data = {
                    'table_title': category['category'],
                    'table_data': [[x['position'], x['name'], x['time']] for x in category['athletes']]
                    }
                pdf = get_podiums.generate_pdf(data)
                pdf_files[category['category']] = pdf
            
            st.session_state.pdf_files = pdf_files
        else:
            st.error(f"Erro ao acessar a API: {response.status_code}")
    
   if 'pdf_files' in st.session_state:
        st.subheader('Arquivos PDF Gerados:')
        for category, pdf_file in st.session_state.pdf_files.items():
            st.download_button(
                label=f"Baixar PDF da categoria {category}",
                data=pdf_file,
                file_name=f"{category}.pdf",
                        mime="application/pdf"
                    )


main()
