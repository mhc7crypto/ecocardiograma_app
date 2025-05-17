import streamlit as st
import math

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(layout="wide")
st.title("🩺 ECOCARDIOGRAMA - HOSPITAL SANTA MARÍA")
st.markdown("---")

# --- 1. DATOS DEL PACIENTE ---
st.header("📋 Datos del Paciente")
col1, col2, col3 = st.columns(3)
with col1:
    nombre = st.text_input("Nombre del paciente")
with col2:
    peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1)
with col3:
    altura = st.number_input("Altura (cm)", min_value=0.0, step=0.1)

# Cálculo de Superficie Corporal (SC)
sc = ((peso**0.425) * (altura**0.725)) * 0.007184 if peso and altura else 0
st.metric("**Superficie Corporal (SC)**", f"{sc:.2f} m²")

# --- 2. MEDICIONES ECOCARDIOGRÁFICAS ---
st.header("📏 Mediciones")
tab1, tab2, tab3, tab4 = st.tabs(["VI", "VD", "Válvulas", "Doppler"])

with tab1:  # VENTRÍCULO IZQUIERDO
    st.subheader("Ventrículo Izquierdo")
    sivd = st.number_input("SIVd (cm)", min_value=0.0, step=0.1)
    dvid = st.number_input("DVI diastólico (cm)", min_value=0.0, step=0.1)
    ppvid = st.number_input("PPVId (cm)", min_value=0.0, step=0.1)
    dvis = st.number_input("DVI sistólico (cm)", min_value=0.0, step=0.1)
    
    # Cálculos (fórmulas de tu Excel)
    vfd = (dvid ** 3) * 0.523  # Aproximación para VFD (ml)
    vfs = (dvis ** 3) * 0.523  # Aproximación para VFS (ml)
    fevi = ((vfd - vfs) / vfd) * 100 if vfd > 0 else 0
    masa_vi = 0.8 * (1.04 * ((sivd + dvid + ppvid)**3 - dvid**3)) + 0.6
    masa_vi_index = masa_vi / sc if sc > 0 else 0
    epr = (ppvid * 2) / dvid

    st.write(f"**FEVI:** {fevi:.1f}%")
    st.write(f"**Masa VI:** {masa_vi:.1f} g | Índice: {masa_vi_index:.1f} g/m²")
    st.write(f"**EPR:** {epr:.2f}")

with tab2:  # VENTRÍCULO DERECHO
    st.subheader("Ventrículo Derecho")
    tapse = st.number_input("TAPSE (mm)", min_value=0.0, step=0.1)
    diam_basal_vd = st.number_input("Diámetro basal VD (mm)", min_value=0.0, step=0.1)

with tab3:  # VÁLVULAS
    st.subheader("Válvula Aórtica")
    vmax_ao = st.number_input("Vmax Ao (m/s)", min_value=0.0, step=0.1)
    diam_tsvi = st.number_input("Diámetro TSVI (cm)", min_value=0.0, step=0.1)
    vti_tsvi = st.number_input("VTI TSVI (cm)", min_value=0.0, step=0.1)
    vti_ao = st.number_input("VTI Ao (cm)", min_value=0.0, step=0.1)
    
    # Área valvular aórtica (AVA)
    ava = (math.pi * (diam_tsvi/2)**2 * vti_tsvi) / vti_ao if vti_ao > 0 else 0
    st.write(f"**AVA:** {ava:.2f} cm²")

with tab4:  # DOPPLER
    st.subheader("Doppler Mitral")
    vel_e = st.number_input("Vel E (m/s)", min_value=0.0, step=0.1)
    vel_a = st.number_input("Vel A (m/s)", min_value=0.0, step=0.1)
    e_a = vel_e / vel_a if vel_a > 0 else 0
    st.write(f"**Relación E/A:** {e_a:.1f}")

# --- 3. GENERAR INFORME ---
st.header("📝 Informe Final")
if st.button("Generar Informe", type="primary"):
    # Textos de Hallazgos (copiados de tu Excel)
    hallazgos = """
    - Ventrículo izquierdo de dimensiones y espesores parietales normales. Función sistólica conservada.
    - Motilidad parietal segmentaria conservada.
    - Patrón diastólico de flujo mitral normal.
    - Aurícula izquierda de dimensiones normales.
    - Válvula aórtica trivalva con función valvular normal.
    - Válvula mitral sin alteraciones morfológicas.
    - Válvula pulmonar: sin alteraciones morfológicas. Sin estenosis ni insuficiencia.
    - Válvula tricúspide: sin alteraciones morfológicas. Sin estenosis ni insuficiencia.
    - Cavidades derechas normales. Función sistólica ventrículo derecho conservada.
    - Tabique interauricular de aspecto aneurismático sin evidencias de shunt mediante doppler color.
    - Vena cava inferior de dimensiones normales y con colapso inspiratorio.
    - Raíz aortica y Aorta ascendente de dimensiones conservadas.
    - Ausencia de derrame pericárdico.
    """
    
    # Conclusión (de tu Excel)
    conclusion = "ECOCARDIOGRAMA DOPPLER DENTRO DE LIMITES NORMALES."
    
    # Informe completo
    informe = f"""
    **PACIENTE:** {nombre}
    **SC:** {sc:.2f} m² | **Peso:** {peso} kg | **Altura:** {altura} cm
    ==================================
    **HALLAZGOS:**
    {hallazgos}
    **CONCLUSIÓN:**
    {conclusion}
    """
    st.code(informe, language="text")
    st.success("¡Informe generado! Copia el texto anterior a tu historia clínica.")

# --- FOOTER ---
st.markdown("---")
st.caption("Aplicación desarrollada para el Hospital Santa María - Cardiología")