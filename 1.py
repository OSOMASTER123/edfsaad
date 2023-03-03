import streamlit as st
import plotly.express as px
import pandas as pd

def main():
    st.title("Gráficos SASSTG")

    # Creación de un dataframe
    nombres=["ronald","david","joaquin","claudia","stefany","deysi","sofia","hugo","cesar","edwin","geraldine","enzo","dashboards","inputs","malos","querys","facturacion"]
    espacio_completo=[23.8,203,106,36.7,148,6.97,3.47,0.981,0,0,79.4, 14.1 ,0.0000011,2460,21.7,0.00828,0.216]
    espacio_total=[sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),
                   sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),
                   sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),sum(espacio_completo),
                   sum(espacio_completo),sum(espacio_completo)]
    espacio_sastg=[3420,3420,3420,3420,3420,3420,3420,3420,3420,3420,3420,3420,3420,3420,3420,3420,3420] #3.34 TERAS EN EL SASTG CONVERSION A GB

    df = pd.DataFrame({'nombres': nombres, 'espacio': espacio_completo, 'espacio_ocupado': espacio_total, 'espacio_total': espacio_sastg})
    df['sobrante'] = df['espacio_total']-df['espacio_ocupado']
    df['prc_sobrante'] = df['sobrante']/df['espacio_total']
    df['prc_lleno'] = 1-df['prc_sobrante']

    # Selector para elegir tipo de gráfico
    chart_type = st.selectbox("Elegir tipo de gráfico", ("Barras", "Torta"))

    if chart_type == "Barras":
        fig = px.bar(df, y='espacio', x='nombres', text='espacio', color='nombres', title='Cantidad de Gigabytes (GB) ocupados en el SASSTG')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_xaxes(categoryorder='total ascending')
        fig.update_layout(uniformtext_minsize=5, xaxis_tickangle=-60)

    elif chart_type == "Torta":
        fig = px.pie(df, values='espacio', names='nombres', title='Porcentaje de espacio ocupado en SASSTG en Gigabyte (GB)')
        fig.update_traces(textposition='inside', textinfo='percent+label')

    # Mostrar gráfico
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
    
