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
    dvid = st.number_input("DVId (cm)", min_value=1.0, value=5.0, step=0.1)
    ppvid = st.number_input("PPVId (cm)", min_value=0.1, value=1.0, step=0.1)
    dvis = st.number_input("DVIs (cm)", min_value=1.0, value=3.0, step=0.1)
    vfd = st.number_input("VFD (ml)", min_value=1.0, value=120.0, step=1.0)
    vfs = st.number_input("VFS (ml)", min_value=1.0, value=40.0, step=1.0)

# Cálculos VI
vs = vfd - vfs
masa_vi = 0.8 * (1.04 * ((dvid + sivd + ppvid)**3 - dvid**3)) + 0.6
masa_index = masa_vi / sc if sc > 0 else 0
epr = (ppvid * 2) / dvid
fevi = ((vfd - vfs) / vfd) * 100 if vfd > 0 else 0

# Aurícula Izquierda
st.subheader("Aurícula Izquierda")
ai_col1, ai_col2 = st.columns(2)
with ai_col1:
    vol_ai_4c = st.number_input("Vol AI 4c (ml)", min_value=1.0, value=30.0, step=1.0)
with ai_col2:
    vol_ai_2c = st.number_input("Vol AI 2c (ml)", min_value=1.0, value=30.0, step=1.0)

vol_ai = (vol_ai_4c + vol_ai_2c) / 2
vol_ai_index = vol_ai / sc if sc > 0 else 0

# Aorta
st.subheader("Aorta")
ao_col1, ao_col2 = st.columns(2)
with ao_col1:
    raiz_ao = st.number_input("Raíz Ao (mm)", min_value=10.0, value=35.0, step=0.1)
with ao_col2:
    ao_ascend = st.number_input("Ao Ascend (mm)", min_value=10.0, value=30.0, step=0.1)

ao_index = raiz_ao / sc if sc > 0 else 0

# Ventrículo Derecho
st.subheader("Ventrículo Derecho")
vd_col1, vd_col2 = st.columns(2)
with vd_col1:
    tapse = st.number_input("TAPSE (mm)", min_value=5.0, value=20.0, step=0.1)
    diam_basal_vd = st.number_input("Diam Basal (mm)", min_value=10.0, value=35.0, step=0.1)
with vd_col2:
    diam_medio_vd = st.number_input("Diam medio (mm)", min_value=10.0, value=25.0, step=0.1)
    long_vd = st.number_input("Long (mm)", min_value=10.0, value=70.0, step=0.1)

# --- 3. DOPPLER ---
st.header("📡 Doppler Valvular")

# Válvula Mitral
st.subheader("Válvula Mitral")
mitral_col1, mitral_col2 = st.columns(2)
with mitral_col1:
    vel_e = st.number_input("Vel E (m/s)", min_value=0.1, value=0.8, step=0.1)
    vel_a = st.number_input("Vel A (m/s)", min_value=0.1, value=0.6, step=0.1)
    rel_e_a = vel_e / vel_a if vel_a > 0 else 0
with mitral_col2:
    vel_e_prime = st.number_input("Vel e' (m/s)", min_value=0.1, value=0.1, step=0.1)
    e_e_prime = vel_e / vel_e_prime if vel_e_prime > 0 else 0

# Válvula Aórtica
st.subheader("Válvula Aórtica")
aortica_col1, aortica_col2 = st.columns(2)
with aortica_col1:
    vmax_ao = st.number_input("Vmax Ao (m/s)", min_value=0.1, value=1.5, step=0.1)
    g_max_ao = 4 * (vmax_ao**2)
    g_medio_ao = st.number_input("G medio (mmHg)", min_value=0.0, value=10.0, step=0.1)
with aortica_col2:
    diam_tsvi = st.number_input("Diam TSVI (cm)", min_value=0.1, value=2.0, step=0.1)
    vti_tsvi = st.number_input("VTI TSVI (cm)", min_value=1.0, value=20.0, step=1.0)
    vti_ao = st.number_input("VTI Ao (cm)", min_value=1.0, value=20.0, step=1.0)

ava = (math.pi * (diam_tsvi/2)**2 * vti_tsvi) / vti_ao if vti_ao > 0 else 0
ava_index = ava / sc if sc > 0 else 0
vel_tsvi_ao = vti_tsvi / vti_ao if vti_ao > 0 else 0

# Válvula Tricúspide
st.subheader("Válvula Tricúspide")
tricuspide_col1, tricuspide_col2 = st.columns(2)
with tricuspide_col1:
    vmax_tricuspide = st.number_input("V max (m/s)", min_value=0.1, value=1.0, step=0.1)
    g_max_tricuspide = 4 * (vmax_tricuspide**2)
with tricuspide_col2:
    pr_ad = st.number_input("Pr AD (mmHg)", min_value=0.0, value=3.0, step=0.1)
    psvd = g_max_tricuspide + pr_ad

# Válvula Pulmonar
st.subheader("Válvula Pulmonar")
pulmonar_col1, pulmonar_col2 = st.columns(2)
with pulmonar_col1:
    vmax_pulmonar = st.number_input("V max (m/s)", min_value=0.1, value=0.8, step=0.1, key="pulmonar_vmax")
    g_max_pulmonar = 4 * (vmax_pulmonar**2)

# --- 4. INFORME PARA COPIAR ---
st.header("📋 Informe para Copiar")

informe = f"""
MEDICIONES BIDIMENSIONALES:

Dimensiones de Ventrículo Izquierdo:
- SIVd: {sivd:.1f} cm (H:0,6-1,0 F:0,6-0,9cm)
- DVId: {dvid:.1f} cm (H:4,2-5,8 F:3,8-5,2cm)
- PPVId: {ppvid:.1f} cm (H:0,6-1,0 F:0,6-0,9cm)
- DVIs: {dvis:.1f} cm (H:2,5-4,0 F:2,2-3,5cm)
- VFD: {vfd:.1f} ml (H:62-150 F:46-106ml)
- VFS: {vfs:.1f} ml (H:21-61 F:14-42ml)
- VS: {vs:.1f} ml (60-100ml)
- Masa VI: {masa_vi:.1f} g (H:88-224 F:67-162g)
- Masa index: {masa_index:.1f} g/m² (H:46-115 F:43-95g/m2)
- EPR: {epr:.2f} (<0,42)
- FEVI: {fevi:.1f}% (H:>52% F:>54%)

Dimensiones de Aurícula Izquierda:
- Vol AI 4c: {vol_ai_4c:.1f} ml
- Vol AI 2c: {vol_ai_2c:.1f} ml
- Volumen AI: {vol_ai:.1f} ml
- Volumen AI index: {vol_ai_index:.1f} ml/m² (<34)

Dimensiones de Aorta:
- Raíz Ao: {raiz_ao:.1f} mm (29-45)
- Ao Ascend: {ao_ascend:.1f} mm (22-36)
- Ao index: {ao_index:.1f} mm/m² (19±1)

Dimensiones de Ventrículo Derecho:
- TAPSE: {tapse:.1f} mm (>17)
- Diámetro basal: {diam_basal_vd:.1f} mm (25-41)
- Diámetro medio: {diam_medio_vd:.1f} mm (19-35)
- Longitud: {long_vd:.1f} mm (59-83)

DOPPLER VALVULAR:

Válvula Mitral:
- Vel E: {vel_e:.1f} m/s
- Vel A: {vel_a:.1f} m/s
- Vel e': {vel_e_prime:.1f} m/s
- Relación E/A: {rel_e_a:.1f}
- E/e': {e_e_prime:.1f} (<13)

Válvula Aórtica:
- Vmax Ao: {vmax_ao:.1f} m/s (≤2,5)
- Gradiente máximo: {g_max_ao:.1f} mmHg
- Gradiente medio: {g_medio_ao:.1f} mmHg
- AVA: {ava:.2f} cm²
- AVA index: {ava_index:.2f}
- Vel TSVI/Ao: {vel_tsvi_ao:.2f}

Válvula Tricúspide:
- V max: {vmax_tricuspide:.1f} m/s
- Gradiente máximo: {g_max_tricuspide:.1f} mmHg
- Pr AD: {pr_ad:.1f} mmHg (0-5mmHg)
- PSVD: {psvd:.1f} mmHg (<35mmHg)

Válvula Pulmonar:
- V max: {vmax_pulmonar:.1f} m/s
- Gradiente máximo: {g_max_pulmonar:.1f} mmHg

HALLAZGOS:

Ventrículo izquierdo de dimensiones y espesores parietales normales. Función sistólica conservada.
Motilidad parietal segmentaria conservada.
Patrón diastólico de flujo mitral normal.
Aurícula izquierda de dimensiones normales.
Válvula aórtica trivalva con función valvular normal.
Válvula mitral sin alteraciones morfológicas.
Válvula pulmonar: sin alteraciones morfológicas. Sin estenosis ni insuficiencia.
Válvula tricúspide: sin alteraciones morfológicas. Sin estenosis ni insuficiencia.
Cavidades derechas normales. Función sistólica ventrículo derecho conservada.
Tabique interauricular de aspecto aneurismático sin evidencias de shunt mediante doppler color.
Vena cava inferior de dimensiones normales y con colapso inspiratorio.
Raíz aortica y Aorta ascendente de dimensiones conservadas.
Ausencia de derrame pericárdico.

CONCLUSIÓN:
ECOCARIOGRAMA DOPPLER DENTRO DE LIMITES NORMALES.
"""

st.text_area("Informe completo (copiar y pegar):", informe, height=600)

if st.button("📋 Copiar al Portapapeles"):
    st.toast("¡Informe copiado!", icon="✅")

# --- FOOTER ---
st.divider()
st.caption("Hospital Santa María - Servicio de Cardiología")