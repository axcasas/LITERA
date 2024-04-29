import streamlit as st
import streamlit_book as stb

st.markdown("# Cuestionario de Cronotipos de Munich (MCTQ)")
st.markdown("#### Ahora te vamos a preguntar sobre tus hábitos de sueño durante tus días LIBRES (los que no trabajas y/o estudias)")
st.markdown("#### Recordá responder en formato de 24 Horas")

st.markdown("---")
st.write("1. En mis días libres (que no estudio y/o trabajo), me acuesto a las ...:... Horas")
BTf = st.time_input('Hora de acostarse:', value=None, key='time1')
st.markdown("---")

st.write("2. En mis días libres (que no estudio y/o trabajo), en realidad estoy listo/a para dormirme a las ...:... Horas")
SPrepf = st.time_input('Hora de estar listo para dormir:', value=None, key='time2')
st.markdown("---")

st.write("3. En mis días libres (que no estudio y/o trabajo), necesito ... minutos para conciliar el sueño")
SLatf = st.number_input('Minutos para conciliar el sueño:', value=None, step=60, key='time3')
st.markdown("---")

st.write("4. En mis días libres (que no estudio y/o trabajo), me despierto a las ...:... Horas")
SEf = st.time_input('Hora de despertarse:', value=None, key='time4')
st.markdown("---")

st.write("5. ¿Con despertador o sin despertador? ")
despertador_dia_libre = st.radio('Despertador:', options=["Con despertador", "Sin despertador"], key='time5')
st.markdown("---")

st.write("6. En mis días libres (que no estudio y/o trabajo), me levanto después de ... Minutos")
SIf = st.number_input('Minutos antes de levantarse:', value=None, key='time6')

'''
st.markdown("---")
stb.to_do_list(tasks={"a":True, "b":False, "c":False}, 
                header="Description 02",
                success="You did it!")

st.markdown("---")
stb.true_or_false("Question description", False)

st.markdown("---")
stb.single_choice("Select the correct answers", ["a", "b", "c"], 0)

st.markdown("---")
stb.multiple_choice("Select the correct answers", {"a":True, "b":False, "c":False})

st.markdown("---")
stb.share("My blog", "http://sebastiandres.xyz")
'''