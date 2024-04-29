import streamlit as st
import streamlit_book as stb
import datetime

st.markdown("# Cuestionario de Cronotipos de Munich (MCTQ)")
st.markdown("#### Acá te vamos a preguntar sobre tus hábitos de sueño durante tus días LABORALES (los que no trabajas y/o estudias)")
st.markdown("#### Recordá responder en formato de 24 Horas")

st.markdown("---")

st.write("1. En mis días laborales (estudio/trabajo), me acuesto a las ...:... Horas")
BTw = st.time_input('Hora de acostarse:', value=None, key='time1')
st.markdown("---")

st.write("2. En mis días laborales (estudio/trabajo), en realidad estoy listo/a para dormirme a las ...:... Horas")
SPrepw = st.time_input('Hora de estar listo para dormir:', value=None, key='time2')
st.markdown("---")

st.write("3. En mis días laborales (estudio/trabajo), necesito ... minutos para conciliar el sueño")
SLatw = st.number_input('Minutos para conciliar el sueño:', value=None, key='time3')
st.markdown("---")

st.write("4. En mis días laborales (estudio/trabajo), me despierto a las ...:... Horas")
SEw = st.time_input('Hora de despertarse:', value=None, step=60, key='time4')
st.markdown("---")

st.write("5. ¿Con despertador o sin despertador? ")
despertador_dia_laboral = st.radio('Despertador:', options=["Con despertador", "Sin despertador"], key='time5')
st.markdown("---")

st.write("6. En mis días laborales (estudio/trabajo), me levanto después de ... Minutos")
SIw = st.number_input('Minutos antes de levantarse:', value=None, key='time6')

# Check if any mandatory field is left blank
if not all([BTw, SPrepw, SLatw, SEw, SIw]):
    st.sidebar.error("Por favor, completa todas las preguntas obligatorias antes de continuar.")
else:
    st.markdown("Siguiente Página")

'''
st.markdown("---")
stb.to_do_list(tasks={"a":True, "b":False, "c":False}, 
                header="Description 02",
                success="You did it!")

st.markdown("---")
stb.true_or_false("Question description", False)

st.markdown("---")
stb.single_choice("¿Con despertador o sin despertador?", ["Con despetador", "Sin despertador"], 0)

st.markdown("---")
stb.multiple_choice("Select the correct answers", {"a":True, "b":False, "c":False})

# st.markdown("---")
# stb.share("My blog", "http://sebastiandres.xyz")
'''