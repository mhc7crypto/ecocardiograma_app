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

# --- 2. MEDICIONES BIDIMENSIONALES ---
st.header("📏 Mediciones Bidimensionales")

# Ventrículo Izquierdo
st.subheader("Dimensiones de Ventrículo Izquierdo")
vi_col1, vi_col2, vi_col3 = st.columns([2,2,2])

with vi_col1:
    st.markdown("**Mediciones**")
    sivd = st.number_input("SIVd (cm)", min_value=0.1, value=1.0, step=0.1, key="sivd")
    dvid = st.number_input("DVId (cm)", min_value=1.0, value=5.0, step=0.1, key="dvid")
    ppvid = st.number_input("PPVId (cm)", min_value=0.1, value=1.0, step=0.1, key="ppvid")
    dvis = st.number_input("DVIs (cm)", min_value=1.0, value=3.0, step=0.1, key="dvis")
    vfd = st.number_input("VFD (ml)", min_value=1.0, value=120.0, step=1.0, key="vfd")
    vfs = st.number_input("VFS (ml)", min_value=1.0, value=40.0, step=1.0, key="vfs")
    vs = vfd - vfs
    st.metric("VS (ml)", f"{vs:.1f}")

with vi_col2:
    st.markdown("**Valores normales**")
    st.markdown("H:0,6 - 1,0 F:0,6-0,9cm")
    st.markdown("H:4,2 - 5,8 F:3,8 - 5,2cm")
    st.markdown("H:0,6 - 1,0 F:0,6-0,9cm")
    st.markdown("H:2,5 - 4,0 F:2,2 - 3,5cm")
    st.markdown("H:62-150 F:46-106ml")
    st.markdown("H:21-61 F:14-42ml")
    st.markdown("60-100 ml")

with vi_col3:
    masa_vi = 0.8 * (1.04 * ((dvid + sivd + ppvid)**3 - dvid**3)) + 0.6
    masa_index = masa_vi / sc if sc > 0 else 0
    epr = (ppvid * 2) / dvid
    fevi = ((vfd - vfs) / vfd) * 100 if vfd > 0 else 0
    
    st.markdown("**Valores normales**")
    st.metric("Masa (g)", f"{masa_vi:.1f}", help="H:88 - 224 F:67 - 162g")
    st.metric("Masa index (g/m²)", f"{masa_index:.1f}", help="H:46-115 F:43-95g/m2")
    st.metric("EPR", f"{epr:.2f}", help="< 0,42")
    st.metric("FEVI (%)", f"{fevi:.1f}", help="H:>52% F:>54%")

# Aurícula Izquierda
st.subheader("Dimensiones de la Aurícula izquierda")
ai_col1, ai_col2, ai_col3 = st.columns([2,2,2])

with ai_col1:
    vol_ai_4c = st.number_input("Vol AI 4c (ml)", min_value=1.0, value=30.0, step=1.0)
with ai_col2:
    vol_ai_2c = st.number_input("Vol AI 2c (ml)", min_value=1.0, value=30.0, step=1.0)
with ai_col3:
    vol_ai = (vol_ai_4c + vol_ai_2c) / 2
    vol_ai_index = vol_ai / sc if sc > 0 else 0
    st.markdown("**Valores normales**")
    st.metric("Vol AI (ml)", f"{vol_ai:.1f}")
    st.metric("Vol AI index (ml/m²)", f"{vol_ai_index:.1f}", help="< 34 ml/m2")

# Aorta
st.subheader("Dimensiones de la Aorta")
ao_col1, ao_col2, ao_col3 = st.columns([2,2,2])

with ao_col1:
    raiz_ao = st.number_input("Raíz Ao (mm)", min_value=10.0, value=35.0, step=0.1)
    ao_ascend = st.number_input("Ao Ascend (mm)", min_value=10.0, value=30.0, step=0.1)
with ao_col2:
    st.markdown("**Valores normales**")
    st.markdown("29 - 45")
    st.markdown("22 - 36")
with ao_col3:
    ao_index = raiz_ao / sc if sc > 0 else 0
    st.markdown("**Valores normales**")
    st.metric("Ao index (mm/m²)", f"{ao_index:.1f}", help="19 +/- 1")

# Ventrículo Derecho
st.subheader("Dimensiones de Ventrículo derecho")
vd_col1, vd_col2, vd_col3 = st.columns([2,2,2])

with vd_col1:
    tapse = st.number_input("TAPSE (mm)", min_value=5.0, value=20.0, step=0.1)
    diam_basal_vd = st.number_input("Diam Basal (mm)", min_value=10.0, value=35.0, step=0.1)
    diam_medio_vd = st.number_input("Diam medio (mm)", min_value=10.0, value=25.0, step=0.1)
    long_vd = st.number_input("Long (mm)", min_value=10.0, value=70.0, step=0.1)
with vd_col2:
    st.markdown("**Valores normales**")
    st.markdown("> 17")
    st.markdown("25 - 41")
    st.markdown("19 - 35")
    st.markdown("59 - 83")

# --- 3. DOPPLER VALVULAR ---
st.header("📡 Doppler Valvular")

# Válvula Mitral
st.subheader("Doppler de Válvula Mitral")
mitral_col1, mitral_col2, mitral_col3 = st.columns([2,2,2])

with mitral_col1:
    vel_e = st.number_input("Vel E (m/s)", min_value=0.1, value=0.8, step=0.1)
    vel_a = st.number_input("Vel A (m/s)", min_value=0.1, value=0.6, step=0.1)
    rel_e_a = vel_e / vel_a if vel_a > 0 else 0
    st.metric("Rel E/A", f"{rel_e_a:.1f}")
with mitral_col2:
    vel_e_prime = st.number_input("Vel e´ (m/s)", min_value=0.1, value=0.1, step=0.1)
    e_e_prime = vel_e / vel_e_prime if vel_e_prime > 0 else 0
    st.metric("E/é", f"{e_e_prime:.1f}", help="< 13")

# Válvula Aórtica
st.subheader("Doppler de Válvula Aórtica")
aortica_col1, aortica_col2, aortica_col3 = st.columns([2,2,2])

with aortica_col1:
    vmax_ao = st.number_input("Vmax Ao (m/s)", min_value=0.1, value=1.5, step=0.1)
    st.markdown("**Valores normales**")
    st.markdown("≤2,5")
    vti_ao = st.number_input("VTI Ao (cm)", min_value=1.0, value=20.0, step=1.0)
    g_max_ao = 4 * (vmax_ao**2)
    st.metric("G max (mmHg)", f"{g_max_ao:.1f}")
    g_medio_ao = st.number_input("G medio (mmHg)", min_value=0.0, value=10.0, step=0.1)
with aortica_col2:
    diam_tsvi = st.number_input("Diam TSVI (cm)", min_value=0.1, value=2.0, step=0.1)
    vti_tsvi = st.number_input("VTI TSVI (cm)", min_value=1.0, value=20.0, step=1.0)
    ava = (math.pi * (diam_tsvi/2)**2 * vti_tsvi) / vti_ao if vti_ao > 0 else 0
    st.metric("AVA (cm²)", f"{ava:.2f}")
    ava_index = ava / sc if sc > 0 else 0
    st.metric("AVA index", f"{ava_index:.2f}")
    vel_tsvi_ao = vti_tsvi / vti_ao if vti_ao > 0 else 0
    st.metric("Vel TSVI/Ao", f"{vel_tsvi_ao:.2f}")

# Válvula Tricúspide
st.subheader("Doppler de la Válvula Tricuspide")
tricuspide_col1, tricuspide_col2, tricuspide_col3 = st.columns([2,2,2])

with tricuspide_col1:
    vmax_tricuspide = st.number_input("V max (m/s)", min_value=0.1, value=1.0, step=0.1)
    g_max_tricuspide = 4 * (vmax_tricuspide**2)
    st.metric("G. max (mmHg)", f"{g_max_tricuspide:.1f}")
with tricuspide_col2:
    pr_ad = st.number_input("Pr AD (mmHg)", min_value=0.0, value=3.0, step=0.1)
    st.markdown("**Valores normales**")
    st.markdown("0-5 mmHg")
    psvd = g_max_tricuspide + pr_ad
    st.metric("PSVD (mmHg)", f"{psvd:.1f}", help="< 35 mmHg")

# Válvula Pulmonar
st.subheader("Doppler de la Válvula Pulmonar")
pulmonar_col1, pulmonar_col2 = st.columns([2,2])

with pulmonar_col1:
    vmax_pulmonar = st.number_input("V max (m/s)", min_value=0.1, value=0.8, step=0.1, key="pulmonar_vmax")
    g_max_pulmonar = 4 * (vmax_pulmonar**2)
    st.metric("G. max (mmHg)", f"{g_max_pulmonar:.1f}")

# --- 4. INFORME FINAL ---
st.header("📝 Informe Final")

# Tabla resumen de valores
resumen = """
**MEDICIONES BIDIMENSIONALES**

**Dimensiones de Ventrículo Izquierdo**  
| Mediciones       | Valor     | Valores normales         | Parámetros calculados | Valor     | Valores normales         |
|------------------|-----------|--------------------------|-----------------------|-----------|--------------------------|
| SIVd (cm)        | {sivd:.1f} | H:0,6 - 1,0 F:0,6-0,9cm | Masa (g)             | {masa_vi:.1f} | H:88 - 224 F:67 - 162g |
| DVId (cm)        | {dvid:.1f} | H:4,2 - 5,8 F:3,8-5,2cm | Masa index (g/m²)    | {masa_index:.1f} | H:46-115 F:43-95g/m2 |
| PPVId (cm)       | {ppvid:.1f} | H:0,6 - 1,0 F:0,6-0,9cm | EPR                  | {epr:.2f} | < 0,42               |
| DVIs (cm)        | {dvis:.1f} | H:2,5 - 4,0 F:2,2-3,5cm | FEVI (%)             | {fevi:.1f} | H:>52% F:>54%       |
| VFD (ml)         | {vfd:.1f} | H:62-150 F:46-106ml     |                      |           |                          |
| VFS (ml)         | {vfs:.1f} | H:21-61 F:14-42ml       |                      |           |                          |
| VS (ml)          | {vs:.1f} | 60-100 ml               |                      |           |                          |

**Dimensiones de la Aurícula izquierda**  
| Mediciones       | Valor     | Valores normales         |
|------------------|-----------|--------------------------|
| Vol AI 4c (ml)   | {vol_ai_4c:.1f} |                          |
| Vol AI 2c (ml)   | {vol_ai_2c:.1f} |                          |
| Vol AI (ml)      | {vol_ai:.1f} |                          |
| Vol AI index     | {vol_ai_index:.1f} | < 34 ml/m2            |

**Dimensiones de la Aorta**  
| Mediciones       | Valor     | Valores normales         |
|------------------|-----------|--------------------------|
| Raíz Ao (mm)     | {raiz_ao:.1f} | 29 - 45               |
| Ao Ascend (mm)   | {ao_ascend:.1f} | 22 - 36              |
| Ao index (mm/m²) | {ao_index:.1f} | 19 +/- 1             |

**Dimensiones de Ventrículo derecho**  
| Mediciones       | Valor     | Valores normales         |
|------------------|-----------|--------------------------|
| TAPSE (mm)       | {tapse:.1f} | > 17                  |
| Diam Basal (mm)  | {diam_basal_vd:.1f} | 25 - 41            |
| Diam medio (mm)  | {diam_medio_vd:.1f} | 19 - 35            |
| Long (mm)        | {long_vd:.1f} | 59 - 83              |

**DOPPLER VALVULAR**

**Doppler de Válvula Mitral**  
| Parámetros | Valor     | Valores normales |
|------------|-----------|------------------|
| Vel E (m/s)| {vel_e:.1f} |                  |
| Vel A (m/s)| {vel_a:.1f} |                  |
| Vel e´(m/s)| {vel_e_prime:.1f} |              |
| E/A        | {rel_e_a:.1f} |                |
| E/e´       | {e_e_prime:.1f} | < 13          |

**Doppler de Válvula Aórtica**  
| Parámetros      | Valor     | Valores normales |
|-----------------|-----------|------------------|
| Vmax Ao (m/s)   | {vmax_ao:.1f} | ≤2,5          |
| G max (mmHg)    | {g_max_ao:.1f} |                |
| G medio (mmHg)  | {g_medio_ao:.1f} |              |
| AVA (cm²)       | {ava:.2f} |                  |
| AVA index       | {ava_index:.2f} |              |
| Vel TSVI/Ao     | {vel_tsvi_ao:.2f} |              |

**Doppler de Válvula Tricúspide**  
| Parámetros      | Valor     | Valores normales |
|-----------------|-----------|------------------|
| V max (m/s)     | {vmax_tricuspide:.1f} |              |
| G. max (mmHg)   | {g_max_tricuspide:.1f} |              |
| Pr AD (mmHg)    | {pr_ad:.1f} | 0-5 mmHg       |
| PSVD (mmHg)     | {psvd:.1f} | < 35 mmHg      |

**Doppler de Válvula Pulmonar**  
| Parámetros      | Valor     |
|-----------------|-----------|
| V max (m/s)     | {vmax_pulmonar:.1f} |
| G. max (mmHg)   | {g_max_pulmonar:.1f} |
""".format(
    sivd=sivd, dvid=dvid, ppvid=ppvid, dvis=dvis, vfd=vfd, vfs=vfs, vs=vs,
    masa_vi=masa_vi, masa_index=masa_index, epr=epr, fevi=fevi,
    vol_ai_4c=vol_ai_4c, vol_ai_2c=vol_ai_2c, vol_ai=vol_ai, vol_ai_index=vol_ai_index,
    raiz_ao=raiz_ao, ao_ascend=ao_ascend, ao_index=ao_index,
    tapse=tapse, diam_basal_vd=diam_basal_vd, diam_medio_vd=diam_medio_vd, long_vd=long_vd,
    vel_e=vel_e, vel_a=vel_a, vel_e_prime=vel_e_prime, rel_e_a=rel_e_a, e_e_prime=e_e_prime,
    vmax_ao=vmax_ao, g_max_ao=g_max_ao, g_medio_ao=g_medio_ao, ava=ava, ava_index=ava_index, vel_tsvi_ao=vel_tsvi_ao,
    vmax_tricuspide=vmax_tricuspide, g_max_tricuspide=g_max_tricuspide, pr_ad=pr_ad, psvd=psvd,
    vmax_pulmonar=vmax_pulmonar, g_max_pulmonar=g_max_pulmonar
)

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
st.markdown(informe_completo)

# Botón para copiar
if st.button("📋 Copiar Informe"):
    st.toast("¡Informe copiado al portapapeles!", icon="✅")

# --- FOOTER ---
st.divider()
st.caption("Aplicación desarrollada para el Hospital Santa María - Servicio de Cardiología")