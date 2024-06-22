        mediana = st.median(numeros)
        promedio = sum(numeros) / len(numeros)
        promFinal = round(promedio,1)

        modas = st.mode(numeros)

except:
    print("ERROR: ERROR EN EL PROGRAMA. CONSULTAR AL DUEÑO")