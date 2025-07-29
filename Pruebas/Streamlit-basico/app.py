import streamlit as st
import pandas as pd

# Título principal
st.title("📊 Visualizador de CSV con Streamlit")

# Subida de archivo
archivo = st.file_uploader("Subí tu archivo CSV", type="csv")

if archivo is not None:
    df = pd.read_csv(archivo)

    st.success("Archivo cargado correctamente ✅")

    # Mostrar una vista previa de los datos
    st.subheader("👀 Vista previa del archivo")
    st.dataframe(df)

    # Mostrar estadísticas básicas
    st.subheader("📈 Estadísticas básicas")
    st.write(df.describe())

    # Selección de columna para gráfico
    columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns
    if len(columnas_numericas) > 0:
        col = st.selectbox("Seleccioná una columna numérica para graficar", columnas_numericas)
        st.line_chart(df[col])
    else:
        st.warning("⚠️ No hay columnas numéricas para graficar.")
else:
    st.info("Esperando un archivo CSV para comenzar...")
