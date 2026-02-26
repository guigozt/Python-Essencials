import streamlit as st
import time

st.set_page_config(page_title='IHC DA ALEGRIA', layout='centered')

st.title('IHC - Principios de Norman')

st.markdown('---')

tab1, tab2 = st.tabs(['Interface infernal','Interface correta'])

with tab1:
    st.subheader('Tente realizar o cadastro...')
    #MAPEAMENTO - AÇÕES DIFERENTES
    col1, col2 = st.columns(2)

    with col1:
        btn_falso_confirmar = st.button('CONFIRMAR E SALVAR', use_container_width=True)

    with col2:
        btn_falso_cancelar = st.button('cancelar', use_container_width=True)

        #AFFORDANCE - FALTA DE INTUITO
        entrada_misteriosa = st.text_input('Digite: ')

        if btn_falso_confirmar:
            st.error('ERRO 0X000912: Ação inesperada.')

        #FEEDBACK - ATRASADO
        if btn_falso_cancelar:
            with st.empty():
                st.write('Processando...')
                time.sleep(3)
                #ambiguidade -  "Qual processo?"
                st.warning('Processo finalizado')

with tab2:
    st.subheader('Interface intuitiva')

    #AFFORDANCE E VISIBILIDADE
    nome_usuario = st.text_input('Digite o nome completo: ', placeholder= 'Megan Denise Fox')

    email_usuario = st.text_input('Email para contato: ', placeholder= 'megan@gmail.com')

    col_a, col_b = st.columns([1, 4])

    with col_a:
        #CONSISTENCIA - destaque visual
        if st.button('Salvar Dados', type='primary'):
            #validação dos dados
            if nome_usuario and email_usuario:
                #FEEDBACK - IMEDIATO
                with st.spinner('Comunicando-se com o servidor...'):
                    time.sleep(1)

                #FEEDBACK - SUCESSO
                st.sucess(f'Parabéns {nome_usuario}! Seu cadastro foi bem sucedido!')

            else:
                #FEEDBACK - ERRO
                st.error('Usuário, você esqueceu de preencher o nome ou email')

    with col_b:
        st.button('Limpar campos', type='secondary')

    
        
