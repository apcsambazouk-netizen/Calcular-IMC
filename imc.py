''' Calculadora de IMC '''
# pip install flet

import streamlit as st

st.title("Calculadora de IMC")

peso = st.number_input("Peso (kg)", min_value=1.0, step=0.1)
altura = st.number_input("Altura (m)", min_value=0.5, step=0.01)

if st.button("Calcular"):
    imc = peso / (altura ** 2)

    st.success(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        st.write("Classificação: Abaixo do peso")
    elif imc < 25:
        st.write("Classificação: Peso normal")
    elif imc < 30:
        st.write("Classificação: Sobrepeso")
    elif imc < 35:
        st.write("Classificação: Obesidade Grau I")
    elif imc < 40:
        st.write("Classificação: Obesidade Grau II")
    else:
        st.write("Classificação: Obesidade Grau III")