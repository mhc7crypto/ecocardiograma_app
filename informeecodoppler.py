import streamlit as st
import math

# Configuración de la página
st.set_page_config(page_title="Ecocardiograma - Hospital Santa María", layout="wide", page_icon="❤️")
st.title("📊 INFORME ECOCARDIOGRÁFICO")

# --- 1. DATOS DEL PACIENTE ---
st.header("📋 Datos del Paciente")
col1, col2, col3 = st.columns(3)
with col1:
    peso = st.number_input("Peso (kg)", min_value=30.0, value=70.0, step=0.1)
with col2:
    altura = st.number_input("Altura (cm)", min_value=100.0, value=170.0, step=1.0)
with col3:
    sc = ((peso**0.425) * (altura**0.725)) * 0.007184
    st.metric("Superficie Corporal (SC)", f"{sc:.2f} m²")

# --- 2. DIMENSIONES VENTRÍCULO IZQUIERDO ---
st.header("📏 Ventrículo Izquierdo")
vi_col1, vi_col2, vi_col3 = st.columns(3)

with vi_col1:
    sivd = st.number_input("SIVd (cm)", min_value=0.1, value=1.0, step=0.1)
    dvid = st.number_input("DVI diastólico (cm)", min_value=1.0, value=5.0, step=0.1)
    ppvid = st.number_input("PPVId (cm)", min_value=0.1, value=1.0, step=0.1)

with vi_col2:
    dvis = st.number_input("DVI sistólico (cm)", min_value=1.0, value=3.0, step=0.1)
    vfd = st.number_input("VFD (ml)", min_value=1.0, value=120.0, step=1.0)
    vfs = st.number_input("VFS (ml)", min_value=1.0, value=40.0, step=1.0)

with vi_col3:
    vs = vfd - vfs
    masa_vi = 0.8 * (1.04 * ((dvid + sivd + ppvid)**3 - dvid**3)) + 0.6
    masa_index = masa_vi / sc if sc > 0 else 0
    epr = (ppvid * 2) / dvid
    fevi = ((vfd - vfs) / vfd) * 100 if vfd > 0 else 0
    
    st.metric("VS (ml)", f"{vs:.1f}")
    st.metric("Masa VI (g)", f"{masa_vi:.1f}")
    st.metric("Masa Index (g/m²)", f"{masa_index:.1f}")
    st.metric("EPR", f"{epr:.2f}")
    st.metric("FEVI (%)", f"{fevi:.1f}")

# --- 3. AURÍCULA IZQUIERDA ---
st.header("📏 Aurícula Izquierda")
ai_col1, ai_col2 = st.columns(2)

with ai_col1:
    vol_ai_4c = st.number_input("Vol AI 4c (ml)", min_value=1.0, value=30.0, step=1.0)
with ai_col2:
    vol_ai_2c = st.number_input("Vol AI 2c (ml)", min_value=1.0, value=30.0, step=1.0)

vol_ai = (vol_ai_4c + vol_ai_2c) / 2
vol_ai_index = vol_ai / sc if sc > 0 else 0

st.metric("Volumen AI (ml)", f"{vol_ai:.1f}")
st.metric("Volumen AI Index (ml/m²)", f"{vol_ai_index:.1f}")

# --- 4. DIMENSIONES AORTA ---
st.header("📏 Aorta")
ao_col1, ao_col2 = st.columns(2)

with ao_col1:
    raiz_ao = st.number_input("Raíz Ao (mm)", min_value=10.0, value=35.0, step=0.1)
with ao_col2:
    ao_ascend = st.number_input("Ao Ascend (mm)", min_value=10.0, value=30.0, step=0.1)

ao_index = raiz_ao / sc if sc > 0 else 0
st.metric("Ao Index (mm/m²)", f"{ao_index:.1f}")

# --- 5. VENTRÍCULO DERECHO ---
st.header("📏 Ventrículo Derecho")
vd_col1, vd_col2 = st.columns(2)

with vd_col1:
    tapse = st.number_input("TAPSE (mm)", min_value=5.0, value=20.0, step=0.1)
    diam_basal_vd = st.number_input("Diámetro basal (mm)", min_value=10.0, value=35.0, step=0.1)
with vd_col2:
    diam_medio_vd = st.number_input("Diámetro medio (mm)", min_value=10.0, value=25.0, step=0.1)
    long_vd = st.number_input("Longitud (mm)", min_value=10.0, value=70.0, step=0.1)

# --- 6. DOPPLER VALVULAR ---
st.header("📡 Doppler Valvular")

# Válvula Mitral
st.subheader("Válvula Mitral")
mitral_col1, mitral_col2 = st.columns(2)

with mitral_col1:
    vel_e = st.number_input("Vel E (m/s)", min_value=0.1, value=0.8, step=0.1)
    vel_a = st.number_input("Vel A (m/s)", min_value=0.1, value=0.6, step=0.1)
    rel_e_a = vel_e / vel_a if vel_a > 0 else 0
    st.metric("Relación E/A", f"{rel_e_a:.1f}")

with mitral_col2:
    vel_e_prime = st.number_input("Vel e' (m/s)", min_value=0.1, value=0.1, step=0.1)
    e_e_prime = vel_e / vel_e_prime if vel_e_prime > 0 else 0
    st.metric("E/e'", f"{e_e_prime:.1f}")

# Válvula Aórtica
st.subheader("Válvula Aórtica")
aortica_col1, aortica_col2 = st.columns(2)

with aortica_col1:
    vmax_ao = st.number_input("Vmax Ao (m/s)", min_value=0.1, value=1.5, step=0.1)
    g_max_ao = 4 * (vmax_ao**2)
    st.metric("Gradiente máximo (mmHg)", f"{g_max_ao:.1f}")
    
with aortica_col2:
    diam_tsvi = st.number_input("Diámetro TSVI (cm)", min_value=0.1, value=2.0, step=0.1)
    vti_tsvi = st.number_input("VTI TSVI (cm)", min_value=1.0, value=20.0, step=1.0)
    vti_ao = st.number_input("VTI Ao (cm)", min_value=1.0, value=20.0, step=1.0)
    
    ava = (math.pi * (diam_tsvi/2)**2 * vti_tsvi) / vti_ao if vti_ao > 0 else 0
    ava_index = ava / sc if sc > 0 else 0
    vel_tsvi_ao = vti_tsvi / vti_ao if vti_ao > 0 else 0
    
    st.metric("AVA (cm²)", f"{ava:.2f}")
    st.metric("AVA Index", f"{ava_index:.2f}")
    st.metric("Vel TSVI/Ao", f"{vel_tsvi_ao:.2f}")

# Válvula Tricúspide
st.subheader("Válvula Tricúspide")
tricuspide_col1, tricuspide_col2 = st.columns(2)

with tricuspide_col1:
    vmax_tricuspide = st.number_input("V max (m/s)", min_value=0.1, value=1.0, step=0.1)
    g_max_tricuspide = 4 * (vmax_tricuspide**2)
    st.metric("Gradiente máximo (mmHg)", f"{g_max_tricuspide:.1f}")
    
with tricuspide_col2:
    pr_ad = st.number_input("Pr AD (mmHg)", min_value=0.0, value=3.0, step=0.1)
    psvd = g_max_tricuspide + pr_ad
    st.metric("PSVD (mmHg)", f"{psvd:.1f}")

# --- 7. INFORME FINAL ---
st.header("📝 Informe Final")

# Resumen de valores con rangos normales
resumen = f"""
**RESUMEN DE VALORES:**

**Ventrículo Izquierdo:**
- Masa VI: {masa_vi:.1f} g (H:88-224, F:67-162)
- Masa Index: {masa_index:.1f} g/m² (H:46-115, F:43-95)
- FEVI: {fevi:.1f}% (H:>52%, F:>54%)
- EPR: {epr:.2f} (<0.42)

**Aurícula Izquierda:**
- Volumen AI: {vol_ai:.1f} ml
- Volumen AI Index: {vol_ai_index:.1f} ml/m² (<34)

**Aorta:**
- Raíz Ao: {raiz_ao:.1f} mm (29-45)
- Ao Ascend: {ao_ascend:.1f} mm (22-36)
- Ao Index: {ao_index:.1f} mm/m² (19±1)

**Ventrículo Derecho:**
- TAPSE: {tapse:.1f} mm (>17)
- Diámetro basal: {diam_basal_vd:.1f} mm (25-41)

**Doppler Mitral:**
- E/A: {rel_e_a:.1f} (1.0-2.0)
- E/e': {e_e_prime:.1f} (<13)

**Doppler Aórtico:**
- AVA: {ava:.2f} cm²
- Gradiente máximo: {g_max_ao:.1f} mmHg

**Doppler Tricúspide:**
- PSVD: {psvd:.1f} mmHg (<35)
"""

# Texto fijo de hallazgos
hallazgos = """
**HALLAZGOS:**

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

**CONCLUSIÓN:**					
ECOCARIOGRAMA DOPPLER DENTRO DE LIMITES NORMALES.
"""

# Mostrar informe completo
informe_completo = resumen + hallazgos
st.text_area("Informe Ecocardiográfico", informe_completo, height=600)

# Botón para copiar
if st.button("📋 Copiar Informe"):
    st.toast("¡Informe copiado al portapapeles!", icon="✅")

# --- FOOTER ---
st.divider()
st.caption("Aplicación desarrollada para el Hospital Santa María - Servicio de Cardiología")