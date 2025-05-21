import streamlit as st
import math

# Configuración
st.set_page_config(page_title="Informe Ecocardiograma", layout="wide")
st.title("📝 INFORME ECOCARDIOGRÁFICO")

# --- 1. DATOS DEL PACIENTE ---
st.header("📋 Datos del Paciente")
col1, col2, col3 = st.columns(3)
with col1:
    peso = st.number_input("Peso (kg)", min_value=30.0, value=70.0, step=0.1)
with col2:
    altura = st.number_input("Altura (cm)", min_value=100.0, value=170.0, step=1.0)
with col3:
    sc = ((peso**0.425) * (altura**0.725)) * 0.007184
    st.metric("SC (m²)", f"{sc:.2f}")

# --- 2. MEDICIONES ---
st.header("📏 Mediciones Bidimensionales")

# Ventrículo Izquierdo
st.subheader("Ventrículo Izquierdo")
vi_col1, vi_col2 = st.columns(2)
with vi_col1:
    sivd = st.number_input("SIVd (cm)", min_value=0.1, value=1.0, step=0.1)
    dvid = st.number_input("DVId (cm)", min_value=1.0, value=5.1, step=0.1)
    ppvid = st.number_input("PPVId (cm)", min_value=0.1, value=1.0, step=0.1)
    dvis = st.number_input("DVIs (cm)", min_value=1.0, value=2.9, step=0.1)
with vi_col2:
    vs = st.number_input("VS (ml)", min_value=0.0, value=80.0, step=1.0)
    masa_index = st.number_input("Masa index (g/m²)", min_value=0.0, value=88.9, step=0.1)
    epr = st.number_input("EPR", min_value=0.0, value=0.39, step=0.01)
    fevi = st.number_input("FEVI (%)", min_value=0.0, value=66.7, step=0.1)

# Aurícula Izquierda
st.subheader("Aurícula Izquierda")
ai_col1, ai_col2 = st.columns(2)
with ai_col1:
    vol_ai_4c = st.number_input("Vol AI 4c (ml)", min_value=0.0, value=40.0, step=1.0)
    vol_ai_2c = st.number_input("Vol AI 2c (ml)", min_value=0.0, value=40.0, step=1.0)
with ai_col2:
    vol_ai = (vol_ai_4c + vol_ai_2c) / 2
    vol_ai_index = vol_ai / sc if sc > 0 else 0
    st.metric("Volumen AI promedio (ml)", f"{vol_ai:.1f}")
    st.metric("Volumen AI index (ml/m²)", f"{vol_ai_index:.1f}")

# Aorta
st.subheader("Aorta")
ao_col1, ao_col2 = st.columns(2)
with ao_col1:
    raiz_ao = st.number_input("Raíz Ao (mm)", min_value=0.0, value=37.0, step=0.1)
    ao_ascend = st.number_input("Ao Ascend (mm)", min_value=0.0, value=30.0, step=0.1)
with ao_col2:
    ao_index = raiz_ao / sc if sc > 0 else 0
    st.metric("Ao index (mm/m²)", f"{ao_index:.1f}")

# Ventrículo Derecho
st.subheader("Ventrículo Derecho")
tapse = st.number_input("TAPSE (mm)", min_value=0.0, value=18.0, step=0.1)

# --- 3. DOPPLER ---
st.header("📡 Mediciones Doppler")

# Válvula Mitral
st.subheader("Válvula Mitral")
mitral_col1, mitral_col2 = st.columns(2)
with mitral_col1:
    vel_e = st.number_input("Vel E (cm/s)", min_value=0.0, value=80.0, step=1.0)
    vel_a = st.number_input("Vel A (cm/s)", min_value=0.0, value=60.0, step=1.0)
    rel_e_a = vel_e / vel_a if vel_a > 0 else 0
with mitral_col2:
    vel_e_prime = st.number_input("Vel e' lateral (cm/s)", min_value=0.0, value=7.0, step=0.1)
    e_e_prime = (vel_e/100) / (vel_e_prime/100) if vel_e_prime > 0 else 0

# Válvula Aórtica
st.subheader("Válvula Aórtica")
aortica_col1, aortica_col2 = st.columns(2)
with aortica_col1:
    vmax_ao = st.number_input("Vmax Ao (m/s)", min_value=0.0, value=1.5, step=0.1)
    g_max_ao = 4 * (vmax_ao**2) if vmax_ao > 0 else 0
with aortica_col2:
    st.metric("Gradiente máximo (mmHg)", f"{g_max_ao:.1f}")

# ... (El resto del código se mantiene igual, incluyendo Válvula Tricúspide y Pulmonar)

# --- 4. INFORME PARA COPIAR ---
st.header("📋 Informe para Copiar")

def mostrar_si(valor, texto, valores_normales=""):
    return f"- {texto}: {valor:.1f} {valores_normales}\n" if valor > 0 else ""

informe = f"""
MEDICIONES BIDIMENSIONALES:

Dimensiones de Ventrículo Izquierdo:
- SIVd: {sivd:.1f} cm (H:0,6-1,0 F:0,6-0,9cm)
- DVId: {dvid:.1f} cm (H:4,2-5,8 F:3,8-5,2cm)
- PPVId: {ppvid:.1f} cm (H:0,6-1,0 F:0,6-0,9cm)
- DVIs: {dvis:.1f} cm (H:2,5-4,0 F:2,2-3,5cm)
- VS: {vs:.1f} ml (60-100ml)
- Masa index: {masa_index:.1f} g/m² (H:46-115 F:43-95g/m2)
- EPR: {epr:.2f} (<0,42)
- FEVI: {fevi:.1f}% (H:>52% F:>54%)

Dimensiones de Aurícula Izquierda:
- Vol AI 4c: {vol_ai_4c:.1f} ml
- Vol AI 2c: {vol_ai_2c:.1f} ml
- Volumen AI promedio: {vol_ai:.1f} ml
- Volumen AI index: {vol_ai_index:.1f} ml/m² (<34)

# ... (El resto del informe se mantiene igual)

Válvula Aórtica:
- Vmax Ao: {vmax_ao:.1f} m/s (≤2,5)
- Gradiente máximo: {g_max_ao:.1f} mmHg

# ... (El resto del informe no cambia)
"""

st.text_area("Informe completo (copiar y pegar):", informe, height=600)
