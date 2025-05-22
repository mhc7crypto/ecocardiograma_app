import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Informe Ecocardiograma", layout="wide")
st.title("📝 INFORME ECOCARDIOGRÁFICO")

# ========================================
# 1. DATOS DEL PACIENTE
# ========================================
st.header("📋 Datos del Paciente")
col1, col2, col3 = st.columns(3)
with col1:
    peso = st.number_input("Peso (kg)", min_value=30.0, value=70.0, step=0.1)
with col2:
    altura = st.number_input("Altura (cm)", min_value=100.0, value=170.0, step=1.0)
with col3:
    sc = ((peso**0.425) * (altura**0.725)) * 0.007184
    st.metric("SC (m²)", f"{sc:.2f}")

# ========================================
# 2. MEDICIONES BIDIMENSIONALES
# ========================================
st.header("📏 Mediciones Bidimensionales")

# ----------------------------------------
# Ventrículo Izquierdo
# ----------------------------------------
st.subheader("Ventrículo Izquierdo")
vi_col1, vi_col2 = st.columns(2)

with vi_col1:
    sivd = st.number_input("SIVd (cm)", min_value=0.1, value=1.0, step=0.1)
    dvid = st.number_input("DVId (cm)", min_value=1.0, value=5.1, step=0.1)
    ppvid = st.number_input("PPVId (cm)", min_value=0.1, value=1.0, step=0.1)
    dvis = st.number_input("DVIs (cm)", min_value=1.0, value=2.9, step=0.1)
    vfd = st.number_input("VFD (ml)", min_value=0.0, value=100.0, step=1.0)
    vfs = st.number_input("VFS (ml)", min_value=0.0, value=30.0, step=1.0)

with vi_col2:
    # Cálculos automáticos
    vs = vfd - vfs if vfd > vfs else 0
    fevi = ((vfd - vfs) / vfd * 100) if vfd > 0 else 0
    
    # Masa ventricular (Fórmula ASE/EACVI)
    masa = 0.8 * (1.04 * ((dvid + sivd + ppvid)**3 - dvid**3)) + 0.6
    masa_index = (masa / sc) if sc > 0 else 0
    
    # EPR corregido
    epr = (ppvid * 2) / dvid if dvid > 0 else 0
    
    st.metric("VS (ml)", f"{vs:.1f}")
    st.metric("Masa index (g/m²)", f"{masa_index:.1f} (H:46-115 F:43-95)")
    st.metric("EPR", f"{epr:.2f} (<0.42)")
    st.metric("FEVI (%)", f"{fevi:.1f}% (H:>52% F:>54%)")

# ----------------------------------------
# Aurícula Izquierda
# ----------------------------------------
st.subheader("Aurícula Izquierda")
ai_col1, ai_col2 = st.columns(2)
with ai_col1:
    vol_ai_4c = st.number_input("Vol AI 4c (ml)", min_value=0.0, value=40.0, step=1.0)
    vol_ai_2c = st.number_input("Vol AI 2c (ml)", min_value=0.0, value=40.0, step=1.0)
with ai_col2:
    vol_ai_prom = (vol_ai_4c + vol_ai_2c)/2
    vol_ai_index = vol_ai_prom / sc if sc > 0 else 0
    st.metric("Volumen AI promedio (ml)", f"{vol_ai_prom:.1f}")
    st.metric("Volumen AI index (ml/m²)", f"{vol_ai_index:.1f} (<34)")

# ----------------------------------------
# Aorta
# ----------------------------------------
st.subheader("Aorta")
ao_col1, ao_col2 = st.columns(2)
with ao_col1:
    raiz_ao = st.number_input("Raíz Ao (mm)", min_value=0.0, value=37.0, step=0.1)
    ao_ascend = st.number_input("Ao Ascend (mm)", min_value=0.0, value=30.0, step=0.1)
with ao_col2:
    ao_index = raiz_ao / sc if sc > 0 else 0
    st.metric("Ao index (mm/m²)", f"{ao_index:.1f} (19±1)")

# ----------------------------------------
# Ventrículo Derecho
# ----------------------------------------
st.subheader("Ventrículo Derecho")
tapse = st.number_input("TAPSE (mm)", min_value=0.0, value=18.0, step=0.1)

# ========================================
# 3. MEDICIONES DOPPLER
# ========================================
st.header("📡 Mediciones Doppler")

# ----------------------------------------
# Válvula Mitral
# ----------------------------------------
st.subheader("Válvula Mitral")
mitral_col1, mitral_col2 = st.columns(2)
with mitral_col1:
    vel_e = st.number_input("Vel E (cm/s)", min_value=0.0, value=80.0, step=1.0)
    vel_a = st.number_input("Vel A (cm/s)", min_value=0.0, value=60.0, step=1.0)
    rel_e_a = vel_e / vel_a if vel_a > 0 else 0
    st.metric("Relación E/A", f"{rel_e_a:.1f}")
with mitral_col2:
    vel_e_prime = st.number_input("Vel e' lateral (cm/s)", min_value=0.0, value=7.0, step=0.1)
    e_e_prime = (vel_e/100) / (vel_e_prime/100) if vel_e_prime > 0 else 0
    st.metric("Relación E/e'", f"{e_e_prime:.1f} (<13)")

# ----------------------------------------
# Válvula Aórtica
# ----------------------------------------
st.subheader("Válvula Aórtica")
aortica_col1, aortica_col2 = st.columns(2)
with aortica_col1:
    vmax_ao = st.number_input("Vmax Ao (m/s)", min_value=0.0, value=1.5, step=0.1)
    g_max_ao = 4 * (vmax_ao**2) if vmax_ao > 0 else 0
    st.metric("Gradiente máximo (mmHg)", f"{g_max_ao:.1f}")

# ----------------------------------------
# Válvula Tricúspide
# ----------------------------------------
st.subheader("Válvula Tricúspide")
tricuspide_col1, tricuspide_col2 = st.columns(2)
with tricuspide_col1:
    no_jet_tricuspide = st.checkbox("No se detectó jet de insuficiencia tricuspídea")
    vmax_tricuspide = 0.0
    g_max_tricuspide = 0.0
    pr_ad = 0.0
    psvd = 0.0
    
    if not no_jet_tricuspide:
        vmax_tricuspide = st.number_input("V max (m/s)", min_value=0.0, value=0.0, step=0.1)
        g_max_tricuspide = 4 * (vmax_tricuspide**2) if vmax_tricuspide > 0 else 0
        pr_ad = st.number_input("Pr AD (mmHg)", min_value=0.0, value=0.0, step=0.1)
        psvd = g_max_tricuspide + pr_ad if g_max_tricuspide > 0 else 0

# ----------------------------------------
# Válvula Pulmonar
# ----------------------------------------
st.subheader("Válvula Pulmonar")
pulmonar_col1, pulmonar_col2 = st.columns(2)
with pulmonar_col1:
    vmax_pulmonar = st.number_input("V max (m/s)", min_value=0.0, value=0.8, step=0.1)
    g_max_pulmonar = 4 * (vmax_pulmonar**2) if vmax_pulmonar > 0 else 0

# ========================================
# 4. INFORME FINAL
# ========================================
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
- VFD: {vfd:.1f} ml
- VFS: {vfs:.1f} ml
- VS: {vs:.1f} ml
- Masa index: {masa_index:.1f} g/m² (H:46-115 F:43-95g/m2)
- EPR: {epr:.2f} (<0,42)
- FEVI: {fevi:.1f}% (H:>52% F:>54%)

Dimensiones de Aurícula Izquierda:
- Vol AI 4c: {vol_ai_4c:.1f} ml
- Vol AI 2c: {vol_ai_2c:.1f} ml
- Volumen AI promedio: {vol_ai_prom:.1f} ml
- Volumen AI index: {vol_ai_index:.1f} ml/m² (<34)

Dimensiones de Aorta:
- Raíz Ao: {raiz_ao:.1f} mm (29-45)
- Ao Ascend: {ao_ascend:.1f} mm (22-36)
- Ao index: {ao_index:.1f} mm/m² (19±1)

Dimensiones de Ventrículo Derecho:
- TAPSE: {tapse:.1f} mm (>17)

MEDICIONES DOPPLER:

Válvula Mitral:
- Vel E: {vel_e:.1f} cm/s
- Vel A: {vel_a:.1f} cm/s
- Relación E/A: {rel_e_a:.1f}
- Vel e' lateral: {vel_e_prime:.1f} cm/s
- Relación E/e': {e_e_prime:.1f} (<13)

Válvula Aórtica:
- Vmax Ao: {vmax_ao:.1f} m/s (≤2,5)
- Gradiente máximo: {g_max_ao:.1f} mmHg

Válvula Tricúspide:
{"- No se detectó jet de insuficiencia tricuspídea\n" if no_jet_tricuspide else ""}\
{mostrar_si(vmax_tricuspide, "V max", "m/s")}\
{mostrar_si(g_max_tricuspide, "Gradiente máximo", "mmHg")}\
{mostrar_si(pr_ad, "Pr AD", "mmHg (0-5mmHg)")}\
{mostrar_si(psvd, "PSVD", "mmHg (<35mmHg)")}

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
Tabique interauricular intacto.
Vena cava inferior de dimensiones normales y con colapso inspiratorio.
Raíz aortica y Aorta ascendente de dimensiones conservadas.
Ausencia de derrame pericárdico.

CONCLUSIÓN:
ECOCARIOGRAMA DOPPLER DENTRO DE LIMITES NORMALES.
"""

st.text_area("Informe completo:", informe, height=600)

# ========================================
# FOOTER
# ========================================
st.divider()
st.caption("Hospital Santa María - Servicio de Cardiología")

# ========================================
# EJECUCIÓN
# ========================================
if __name__ == "__main__":
    st.write("Aplicación lista 🏥")
