import streamlit as st
import controllers.ClienteController as ClienteController
import models.Cliente as cliente
import pandas as pd
import Pages.Cliente.Create as PageCreateCliente
import Pages.Cliente.List as PageListCliente


st.sidebar.title('Menu')
Page_Cliente = st.sidebar.selectbox('Cliente', ['Incluir', 'Consultar'])

if Page_Cliente == 'Consultar':
   PageListCliente.List()

if Page_Cliente == 'Incluir':
    st.experimental_set_query_params()
    PageCreateCliente.Create()
    































# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
# sss