def generate_peptides(seq):
    peptides = []
    positions = []

    lengths = [8, 9, 10]   # ✅ updated

    # CLEAN sequence (VERY IMPORTANT)
    seq = "".join([a for a in seq.upper() if a in "ACDEFGHIKLMNPQRSTVWY"])

    for L in lengths:
        for i in range(len(seq) - L + 1):
            peptides.append(seq[i:i+L])
            positions.append(i + 1)

    return peptides, positions
    
import streamlit as st

st.set_page_config(page_title="HPV EPIPRED", page_icon="🧬", layout="wide")

st.markdown("""
<style>

/* ==========================
GOOGLE FONTS
========================== */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;700&family=Sora:wght@600;700&family=Inter:wght@400;600&display=swap');

/* ==========================
GLOBAL
========================== */
html, body, [data-testid="stAppViewContainer"]{
    background-color:#0f172a;
    color:#e2e8f0;
    font-family:'Inter', sans-serif;
    margin:0;
    padding:0;
}

/* ==========================
FULL WIDTH
========================== */
.main .block-container{
    max-width:100% !important;
    padding:0 2rem;
}

/* REMOVE HEADER */
header{visibility:hidden;}

/* ==========================
HEADINGS
========================== */
h1,h2,h3{
    font-family:'Sora', sans-serif;
    font-weight:700;
    color:#e0f2fe;
}

/* ==========================
BUTTONS
========================== */
.stButton > button{
    border-radius:12px;
    padding:10px 24px;
    background:linear-gradient(90deg,#6366f1,#22d3ee);
    color:white;
    border:none;
    font-weight:600;
    box-shadow:0 0 15px rgba(99,102,241,0.5);
}

.stButton > button:hover{
    transform:translateY(-2px);
    box-shadow:0 0 25px rgba(34,211,238,0.8);
}

/* ==========================
INPUT
========================== */
textarea, input{
    background:#020617 !important;
    color:#f8fafc !important;
    border-radius:12px;
    border:1px solid rgba(99,102,241,0.3);
}

/* ==========================
TABLE (FIX WHITE ISSUE)
========================== */
div[data-testid="stDataFrame"]{
    background:rgba(15,23,42,0.85) !important;
    border-radius:14px;
    border:1px solid rgba(99,102,241,0.2);
}

/* ==========================
PLOT
========================== */
.stPlotlyChart{
    background:rgba(15,23,42,0.85) !important;
    border-radius:14px;
    padding:10px;
}

/* ==========================
DOWNLOAD BUTTON FIX
========================== */
.stDownloadButton > button{
    background:linear-gradient(90deg,#6366f1,#22d3ee) !important;
    color:white !important;
    border-radius:12px;
    padding:10px 22px;
    border:none;
    font-weight:600;
}

/* ==========================
REMOVE GREY EMPTY BLOCKS
========================== */
[data-testid="stVerticalBlock"] > div{
    background:transparent !important;
    box-shadow:none !important;
    border:none !important;
    padding:0 !important;
}

/* ==========================
PREMIUM GLASS CARD
========================== */
.glass-card{
    background:linear-gradient(
        135deg,
        rgba(15,23,42,0.85),
        rgba(2,6,23,0.85)
    );

    border-radius:18px;
    padding:20px;
    margin-bottom:20px;

    border:1px solid rgba(99,102,241,0.15);

    box-shadow:
        0 8px 30px rgba(0,0,0,0.4),
        inset 0 0 10px rgba(255,255,255,0.02);
}

/* ==========================
PREMIUM LEGEND BOX
========================== */
.legend-box{
    background:linear-gradient(
        135deg,
        rgba(15,23,42,0.95),
        rgba(2,6,23,0.95)
    );

    border-radius:16px;
    padding:20px;
    margin-bottom:20px;

    border:1px solid rgba(99,102,241,0.3);

    backdrop-filter:blur(12px);

    box-shadow:
        0 0 20px rgba(99,102,241,0.15),
        inset 0 0 12px rgba(255,255,255,0.03);
}

/* TITLE */
.legend-title{
    font-size:18px;
    font-weight:700;

    background:linear-gradient(90deg,#38bdf8,#a78bfa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;

    margin-bottom:12px;
}

/* TEXT */
.legend-item{
    color:#f8fafc !important;
    font-size:14.5px;
    line-height:1.8;
}

.legend-item b{
    color:#22d3ee;
}

/* ==========================
TABS PREMIUM
========================== */
button[data-baseweb="tab"]{
    background:rgba(99,102,241,0.15);
    border-radius:10px;
    padding:6px 14px;
}

button[data-baseweb="tab"]:hover{
    background:rgba(99,102,241,0.35);
}

button[aria-selected="true"]{
    background:linear-gradient(90deg,#6366f1,#22d3ee);
    color:white !important;
    box-shadow:0 0 12px rgba(99,102,241,0.6);
}

/* ==========================
FORCE TEXT VISIBILITY (FIX DULL TEXT)
========================== */

/* ALL TEXT */
body, p, span, div, label {
    color: #f8fafc !important;
}

/* RADIO + OPTIONS */
.stRadio label,
.stRadio div {
    color: #f8fafc !important;
}

/* TAB LABEL TEXT */
button[data-baseweb="tab"] {
    color: #cbd5f5 !important;
}

button[aria-selected="true"] {
    color: #ffffff !important;
}

/* INPUT LABELS */
label[data-testid="stWidgetLabel"] {
    color: #e2e8f0 !important;
    font-weight: 500;
}

/* TEXTAREA CONTENT */
textarea {
    color: #f8fafc !important;
}

/* METRICS */
[data-testid="metric-container"] {
    color: #f8fafc !important;
}

/* DATAFRAME TEXT */
div[data-testid="stDataFrame"] * {
    color: #e2e8f0 !important;
}

/* REMOVE FADED OPACITY FROM STREAMLIT */
* {
    opacity: 1 !important;
}

/* ==========================
FORCE LEGEND BOX DARK (FIX WHITE BOX)
========================== */

.legend-box {
    background: linear-gradient(
        135deg,
        rgba(15,23,42,0.95),
        rgba(2,6,23,0.95)
    ) !important;

    color: #f8fafc !important;

    border: 1px solid rgba(99,102,241,0.35);
    border-radius: 16px;

    padding: 20px;
    margin-bottom: 20px;

    backdrop-filter: blur(12px);

    box-shadow:
        0 0 20px rgba(99,102,241,0.2),
        inset 0 0 12px rgba(255,255,255,0.04);
}

/* TEXT INSIDE LEGEND */
.legend-box * {
    color: #f8fafc !important;
}

/* TITLE */
.legend-title {
    font-size: 18px;
    font-weight: 700;

    background: linear-gradient(90deg,#38bdf8,#a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 12px;
}

/* ITEMS */
.legend-item b {
    color: #22d3ee !important;
}

/* ==========================
DATAFRAME FULL DARK FIX
========================== */

div[data-testid="stDataFrame"] {
    background: #020617 !important;
}

div[data-testid="stDataFrame"] table {
    background: transparent !important;
    color: #e2e8f0 !important;
}

div[data-testid="stDataFrame"] th {
    background: rgba(99,102,241,0.15) !important;
    color: #ffffff !important;
}

div[data-testid="stDataFrame"] td {
    background: transparent !important;
}

/* REMOVE EXTRA GAP BELOW HERO */
section.main {
    padding-top: 0 !important;
}

/* REMOVE RANDOM VERTICAL SPACE */
[data-testid="stVerticalBlock"] {
    gap: 10px !important;
}

html {
    scroll-behavior: smooth;
}

.stButton > button {
    transition: all 0.25s ease !important;
}

.stButton > button:active {
    transform: scale(0.96);
}

.glass-card {
    transition: all 0.25s ease;
}

.glass-card:hover {
    transform: translateY(-4px);
    box-shadow:
        0 12px 40px rgba(0,0,0,0.6),
        0 0 20px rgba(99,102,241,0.2);
}

body::before {
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;

    background:
        radial-gradient(circle at 20% 30%, rgba(99,102,241,0.08), transparent),
        radial-gradient(circle at 80% 70%, rgba(34,211,238,0.08), transparent);

    z-index: -1;
}

.footer {
    backdrop-filter: blur(6px);
}

</style>
""", unsafe_allow_html=True)


import numpy as np
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px
from itertools import product
from collections import Counter
import math
from sklearn.cluster import KMeans
import networkx as nx
import streamlit.components.v1 as components
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
import io
import matplotlib.pyplot as plt
from reportlab.platypus import Image
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak


# =========================================================
# REMOVE STREAMLIT DEFAULT PADDING
# =========================================================
st.markdown("""
<style>

.block-container { padding-top: 0rem !important; }
header {visibility: hidden;}
html { scroll-behavior: smooth; }

</style>
""", unsafe_allow_html=True)

# =========================================================
# PREMIUM FONT SYSTEM
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Inter:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

h1, h2, h3 {
    font-family: 'Sora', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO BLOCK
# =========================================================
components.html("""
<style>

.hero {
    position: relative;
    width: 100vw;
    height: 100vh;
    margin-left: calc(-50vw + 50%);
    overflow: hidden;

    background:
        radial-gradient(circle at 30% 40%, #3b0764 0%, transparent 45%),
        radial-gradient(circle at 70% 60%, #1e1b4b 0%, transparent 50%),
        linear-gradient(135deg, #020617 0%, #0f172a 60%, #020617 100%);
}

canvas {
    position:absolute;
    top:0;
    left:0;
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    z-index: 10;
}

.hero-title {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(64px,8vw,115px);
    font-weight:700;
    letter-spacing:4px;

    background: linear-gradient(
        90deg,
        #60a5fa,
        #a78bfa,
        #22d3ee,
        #60a5fa
    );

    background-size: 300% 300%;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: gradientMove 6s ease infinite,
               glowPulse 3s ease-in-out infinite;
}

.hero-sub {
    font-size:40px;
    color:#cbd5e1;
}

.cta {
    margin-top: 60px;
    font-size: 20px;
    color: #38bdf8;
    text-decoration: none;
    display: inline-block;
    font-weight: 500;
}

.arrow {
    display: inline-block;
    animation: bounce 1.6s infinite;
}

@keyframes bounce {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(8px); }
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes glowPulse {
    0% { text-shadow: 0 0 20px rgba(96,165,250,0.2); }
    50% { text-shadow: 0 0 45px rgba(96,165,250,0.55); }
    100% { text-shadow: 0 0 20px rgba(96,165,250,0.2); }
}

</style>

<div class="hero">

    <canvas id="immune"></canvas>
    <canvas id="network"></canvas>

    <div class="hero-content">
        <div class="hero-title">HPV EPIPRED</div>
        <div class="hero-sub">MHC I Epitope Prediction</div>

        <a href="#scanner" class="cta">
            <span class="arrow">↓</span> Launch Scanner
        </a>
    </div>

</div>

<script>
// (YOUR JS — unchanged)

const immune = document.getElementById("immune");
const network = document.getElementById("network");

const ictx = immune.getContext("2d");
const nctx = network.getContext("2d");

function resize(){
    immune.width = window.innerWidth;
    immune.height = window.innerHeight;
    network.width = window.innerWidth;
    network.height = window.innerHeight;
}
resize();
window.addEventListener("resize", resize);

// IMMUNE + NETWORK SAME CODE (UNCHANGED)

let cells = [];
for(let i=0;i<7;i++){
    cells.push({
        x:Math.random()*window.innerWidth,
        y:Math.random()*window.innerHeight,
        r:90+Math.random()*40,
        pulse:Math.random()*Math.PI,
        driftX:(Math.random()-0.5)*0.3,
        driftY:(Math.random()-0.5)*0.3
    });
}

function drawImmune(){
    ictx.clearRect(0,0,immune.width,immune.height);
    cells.forEach(c=>{
        c.pulse+=0.02;
        c.x+=c.driftX;
        c.y+=c.driftY;

        let membrane = ictx.createRadialGradient(c.x,c.y,c.r*0.2,c.x,c.y,c.r);
        membrane.addColorStop(0,"rgba(168,85,247,0.8)");
        membrane.addColorStop(1,"rgba(168,85,247,0.02)");

        ictx.beginPath();
        ictx.arc(c.x,c.y,c.r,0,Math.PI*2);
        ictx.fillStyle=membrane;
        ictx.fill();

        ictx.beginPath();
        ictx.arc(c.x,c.y,c.r*0.65,0,Math.PI*2);
        ictx.fillStyle="rgba(99,102,241,0.4)";
        ictx.fill();

        ictx.beginPath();
        ictx.arc(c.x,c.y,c.r*0.3,0,Math.PI*2);
        ictx.fillStyle="rgba(56,189,248,0.7)";
        ictx.fill();
    });

    requestAnimationFrame(drawImmune);
}
drawImmune();

// =============================
// AI NEURAL OVERLAY (RESTORED)
// =============================

let nodes = [];
let mouseX = 0;
let mouseY = 0;

for(let i=0;i<70;i++){
    nodes.push({
        x:Math.random()*window.innerWidth,
        y:Math.random()*window.innerHeight,
        vx:(Math.random()-0.5)*0.4,
        vy:(Math.random()-0.5)*0.4
    });
}

window.addEventListener("mousemove", e=>{
    mouseX = e.clientX;
    mouseY = e.clientY;
});

function drawNetwork(){

    nctx.clearRect(0,0,network.width,network.height);

    nodes.forEach(n=>{

        n.x+=n.vx;
        n.y+=n.vy;

        if(n.x<0||n.x>network.width) n.vx*=-1;
        if(n.y<0||n.y>network.height) n.vy*=-1;

        // mouse interaction
        let dx = mouseX - n.x;
        let dy = mouseY - n.y;
        let dist = Math.sqrt(dx*dx + dy*dy);

        if(dist < 200){
            n.x += dx * 0.002;
            n.y += dy * 0.002;
        }

        let pulse = 2 + Math.sin(Date.now()*0.005 + n.x);

        nctx.beginPath();
        nctx.arc(n.x,n.y,pulse,0,Math.PI*2);
        nctx.fillStyle="rgba(34,211,238,0.9)";
        nctx.fill();
    });

    for(let i=0;i<nodes.length;i++){
        for(let j=i+1;j<nodes.length;j++){

            let dx = nodes[i].x - nodes[j].x;
            let dy = nodes[i].y - nodes[j].y;
            let dist = Math.sqrt(dx*dx + dy*dy);

            if(dist < 140){
                nctx.beginPath();
                nctx.moveTo(nodes[i].x,nodes[i].y);
                nctx.lineTo(nodes[j].x,nodes[j].y);
                nctx.strokeStyle="rgba(34,211,238,0.15)";
                nctx.stroke();
            }
        }
    }

    requestAnimationFrame(drawNetwork);
}

drawNetwork();
</script>
""", height=950)

# =========================================================
# MODEL
# =========================================================
@st.cache_resource
def load_model():
    return joblib.load("hpv_cd8_model.pkl")

model = load_model()
threshold = 0.261

# ===== AA LIST (WITH X — IMPORTANT) =====
aa_list = list("ACDEFGHIKLMNPQRSTVWYX")
aa_index = {aa:i for i,aa in enumerate(aa_list)}

def extract_features(seq):

    seq = str(seq)

    if len(seq) not in [8, 9, 10]:
        return None

    # pad to 10 using X (important)
    if len(seq) < 10:
        seq = seq + "X"*(10-len(seq))

    # ===== POSITION (WITH X → 21 AA) =====
    aa_list = list("ACDEFGHIKLMNPQRSTVWYX")
    aa_index = {aa:i for i,aa in enumerate(aa_list)}

    pos = np.zeros((10, len(aa_list)))

    for i in range(10):
        aa = seq[i]
        if aa in aa_index:
            pos[i, aa_index[aa]] = 1

    pos = pos.flatten()   # 210 features

    # ===== AA COMPOSITION (21 features) =====
    aa_count = Counter(seq)
    length = len(seq)

    comp = np.array([
        aa_count.get(aa, 0)/length for aa in aa_list
    ])  # 21 features

    # ===== FINAL =====
    return np.concatenate([pos, comp])   # 🔥 210 + 21 = 231
    
st.markdown("""
<style>

/* RESULT SECTION BACKGROUND */
.result-bg {
    background:
        radial-gradient(circle at 20% 30%, rgba(56,189,248,0.15), transparent 40%),
        radial-gradient(circle at 80% 70%, rgba(168,85,247,0.15), transparent 40%),
        linear-gradient(135deg, #020617 0%, #0f172a 60%, #020617 100%);
    padding: 30px;
    border-radius: 18px;
}

/* TABLE CONTAINER */
[data-testid="stDataFrame"] {
    background: rgba(255,255,255,0.04);
    border-radius: 14px;
    backdrop-filter: blur(6px);
}

/* PLOT CONTAINER */
.stPlotlyChart {
    background: rgba(255,255,255,0.04);
    border-radius: 14px;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.legend-box {
    background: linear-gradient(135deg,#f8fafc,#eef2ff);
    border-left: 6px solid #6366f1;
    padding: 16px;
    border-radius: 10px;
    margin-bottom: 15px;
    font-size: 14px;
}

.legend-title {
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 8px;
}

.legend-item {
    margin-left: 6px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SCANNER SECTION (FULL RESTORED VERSION)
# =========================================================
st.markdown('<div id="scanner"></div>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🔬 AI Scanner", "🧠 Model Explainability"])

# ==========================
# AI SCANNER TAB
# ==========================
with tab1:

    mode = st.radio("Mode", ["Single Sequence","Batch Upload"])
    fasta = ""

    if mode == "Single Sequence":
        fasta = st.text_area("Paste FASTA Sequence")
    else:
        uploaded = st.file_uploader("Upload FASTA File")
        if uploaded:
            fasta = uploaded.read().decode()

    # BUTTON MUST BE INSIDE TAB
    run_scan = st.button("Run AI Scan")

if run_scan and fasta:

        seq = "".join([
                l.strip() for l in fasta.split("\n")
                if not l.startswith(">")
        ]).upper()

        peptides, positions = generate_peptides(seq)
              
        valid_peptides = []
        valid_positions = []
        features = []

        for p, pos in zip(peptides, positions):

            f = extract_features(p)

            if f is not None:
                valid_peptides.append(p)
                valid_positions.append(pos)
                features.append(f)

        X = np.array(features)
        probs = model.predict_proba(X)[:,1]
      
        results = []
        for pos, pep, prob in zip(positions, peptides, probs):
            cat = "Epitope" if prob >= threshold else "Non-Epitope"
            results.append([pos, pep, prob, cat])

        df = pd.DataFrame(
            results,
            columns=["Position","Peptide","Probability","Category"]
        )

        st.session_state["df"] = df

        df["Length"] = df["Peptide"].apply(len)

        # ==========================
        # SPLIT TABLES
        # ==========================
        epitope_df = df[df["Category"] == "Epitope"].sort_values(
            by="Probability", ascending=False
        )

        non_df = df[df["Category"] == "Non-Epitope"].sort_values(
            by="Probability", ascending=False
        )

                
        # ==========================
        # RESULT TABS
        # ==========================
        tab_table, tab_prob, tab_landscape, tab_density, tab_fingerprint, tab_score, tab_atlas, tab_competition = st.tabs([
                "📊 Tables",
                "📈 Probability Plot",
                "🌍 Epitope Landscape",
                "🧬 Epitope Density Map",
                "🌐 Immunogenicity Fingerprint",
                "🧬 Immunogenic Score",
                "🧭 Epitope Atlas",
                "🔥 Epitope Competition Map"
        ])

        config = {
        "displaylogo": False,

        "toImageButtonOptions": {
        "format": "png",
        "filename": "epipred_plot",
        "height": 800,
        "width": 1400,
        "scale": 5   # 🔥 HIGH QUALITY EXPORT
    }
        }
        
        # ==========================
        # TABLE TAB
        # ==========================
        with tab_table:
        
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("### 🟢 Predicted Epitopes")

                st.markdown("""
        <div class="legend-box">

        <div class="legend-title">📊 Table Description</div>

        <div class="legend-item">📍 <b>Position</b> – Starting index of the peptide in the protein sequence</div>

        <div class="legend-item">🧬 <b>Peptide</b> – Extracted 9-mer amino acid window</div>

        <div class="legend-item">📈 <b>Probability</b> – Machine learning predicted epitope likelihood</div>

        <div class="legend-item">🏷 <b>Category</b> – Epitope classification based on prediction threshold</div>

        </div>
        """, unsafe_allow_html=True)
            

                if not epitope_df.empty:

                        epi_show = epitope_df.copy()
                        epi_show["Probability"] = epi_show["Probability"].round(3)

                        st.dataframe(
                                 epi_show[["Position","Peptide","Length","Probability","Category"]],
                                 use_container_width=True,
                                 hide_index=True,
                                 height=350
                        )

                else:
                        st.info("No epitopes detected above threshold.")

                st.markdown("---")

                st.markdown("### ⚪ Predicted Non-Epitopes")

                if not non_df.empty:

                        non_show = non_df.copy()
                        non_show["Probability"] = non_show["Probability"].round(3)

                        st.dataframe(
                                non_show[["Position","Peptide","Length","Probability","Category"]],
                                use_container_width=True,
                                height=350,
                                hide_index=True
                        )

                else:
                        st.info("All peptides classified as epitopes.")

                st.markdown("---")

                st.markdown("### 🏆 Top 10 High-Confidence Epitopes")

                top10 = epitope_df.head(10).copy()
                top10.insert(0, "Rank", range(1, len(top10)+1))
                top10["Length"] = top10["Peptide"].apply(len)

                st.dataframe(
                        top10[["Rank","Position","Peptide","Length","Probability"]],
                        use_container_width=True,
                        hide_index=True
                )
       
        # ==========================
        # PROBABILITY PLOT TAB
        # ==========================
        with tab_prob:
        
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("### 📈 Epitope Probability Across Protein Sequence")
                
                st.markdown("""
        <div class="legend-box">

        <div class="legend-title">📈 Plot Interpretation</div>

        <div class="legend-item">🔵 <b>Light Blue Line</b> – Raw prediction probability for each peptide</div>

        <div class="legend-item">🔷 <b>Dark Blue Line</b> – Smoothed immunogenic signal across sequence</div>

        <div class="legend-item">🚨 <b>Red Dashed Line</b> – Threshold used to classify epitopes</div>

        <div class="legend-item">⛰ <b>Probability Peaks</b> – Regions with strong predicted immune recognition</div>

        </div>
        """, unsafe_allow_html=True)

                window = 12
                smooth_prob = np.convolve(
                        df["Probability"],
                        np.ones(window)/window,
                        mode="same"
                )

                fig = go.Figure()

                fig.add_trace(
                        go.Scatter(
                                x=df["Position"],
                                y=df["Probability"],
                                mode="lines",
                                line=dict(color="rgba(59,130,246,0.3)", width=1),
                                name="Raw Prediction"
                        )
                )

                fig.add_trace(
                        go.Scatter(
                                x=df["Position"],
                                y=smooth_prob,
                                mode="lines",
                                line=dict(color="#1d4ed8", width=3),
                                name="Smoothed Signal"
                        )
                )

                fig.add_hline(
                        y=threshold,
                        line_dash="dash",
                        line_color="red",
                        annotation_text="Epitope Threshold"
                )

                fig.update_layout(
                        height=500,
                        xaxis_title="Protein Position",
                        yaxis_title="Epitope Probability",
                        hovermode="x unified"
                )

                st.plotly_chart(fig, use_container_width=True, config=config)

        # ==========================
        # EPITOPE LANDSCAPE TAB
        # ==========================

        with tab_landscape:
        
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("### 🌍 Epitope Immunogenic Landscape")

                st.markdown("""
                <div class="legend-box">

                <div class="legend-title">🌍 Landscape Interpretation</div>

                <div class="legend-item">📏 <b>X-axis</b> – Peptide position along the protein</div>

                <div class="legend-item">📊 <b>Y-axis</b> – Predicted epitope probability</div>

                <div class="legend-item">🎨 <b>Point Colors</b> – Cluster assignment of peptides</div>

                <div class="legend-item">✖ <b>Black Cross</b> – Cluster center</div>

                </div>
                """, unsafe_allow_html=True)

                X_cluster = df[["Position","Probability"]]

                kmeans = KMeans(n_clusters=4, random_state=42)

                df["Cluster"] = kmeans.fit_predict(X_cluster)

                centers = kmeans.cluster_centers_

                fig_land = px.scatter(
                        df,
                        x="Position",
                        y="Probability",
                        color="Cluster",
                        hover_data=["Peptide"],
                        color_continuous_scale="viridis"
                )

                fig_land.add_trace(
                        go.Scatter(
                                x=centers[:,0],
                                y=centers[:,1],
                                mode="markers",
                                marker=dict(color="black",size=12,symbol="x"),
                                name="Cluster Center"
                        )
                )

                st.plotly_chart(fig_land, use_container_width=True, config=config)
        
        # ==========================
        # EPITOPE DENSITY MAP TAB
        # ==========================
        with tab_density:
        
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("### 🧬 Epitope Density Map")
                    
                st.markdown("""
        <div class="legend-box">

        <div class="legend-title">🧬 Density Map Guide</div>

        <div class="legend-item">📦 <b>Bars</b> – Sliding window regions across the protein</div>

        <div class="legend-item">📊 <b>Bar Height</b> – Fraction of predicted epitopes within that region</div>

        <div class="legend-item">🔥 <b>High Density</b> – Indicates potential immunogenic hotspot regions</div>

        </div>
        """, unsafe_allow_html=True)

                window = 15
                density = []

                for i in range(len(df)):

                        start = max(0, i-window)
                        end = min(len(df), i+window)

                        region = df.iloc[start:end]
                        ep_count = (region["Probability"] >= threshold).sum()

                        density.append(ep_count/len(region))

                density_df = pd.DataFrame({
                        "Position":df["Position"],
                        "Density":density
                })

                fig_density = go.Figure()

                fig_density.add_trace(
                        go.Bar(
                                x=density_df["Position"],
                                y=density_df["Density"],
                                marker_color="#6366f1"
                        )
                )

                fig_density.update_layout(
                        height=350,
                        xaxis_title="Protein Position",
                        yaxis_title="Epitope Density"
                )

                st.plotly_chart(fig_density, use_container_width=True, config=config)

       
        # IMMUNOGENICITY FINGERPRINT
        # ==========================
        with tab_fingerprint:

                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("### 🧬 Protein Immunogenicity Fingerprint")

                st.markdown("""
        <div class="legend-box">

        <div class="legend-title">🧬 Fingerprint Metrics</div>

        <div class="legend-item">🤖 <b>ML Immunogenicity</b> – Average predicted epitope probability</div>

        <div class="legend-item">📍 <b>Epitope Density</b> – Fraction of peptides classified as epitopes</div>

        <div class="legend-item">🧪 <b>Hydrophobicity</b> – Fraction of hydrophobic amino acids</div>

        <div class="legend-item">🧠 <b>Entropy</b> – Sequence diversity across peptides</div>

        <div class="legend-item">⚡ <b>Net Charge</b> – Balance of positive and negative residues</div>

        </div>
        """, unsafe_allow_html=True)

                # Global metrics
                mean_prob = df["Probability"].mean()

                epitope_density = len(df[df["Category"]=="Epitope"]) / len(df)

                hydro_score = np.mean([
                        extract_features(p)[-7]
                        for p in df["Peptide"]
                ])

                entropy_score = np.mean([
                        extract_features(p)[-2]
                        for p in df["Peptide"]
                ])

                charge_score = np.mean([
                        extract_features(p)[-3]
                        for p in df["Peptide"]
                ])

                metrics = {
                        "ML Immunogenicity": mean_prob,
                        "Epitope Density": epitope_density,
                        "Hydrophobicity": hydro_score,
                        "Entropy": entropy_score,
                        "Net Charge": abs(charge_score)
                }

                categories = list(metrics.keys())
                values = list(metrics.values())

                fig_radar = go.Figure()

                fig_radar.add_trace(
                        go.Scatterpolar(
                                r=values,
                                theta=categories,
                                fill="toself",
                                line=dict(color="#6366f1", width=3),
                                name="Protein Profile"
                        )
                )

                fig_radar.update_layout(
                        polar=dict(
                                radialaxis=dict(
                                        visible=True,
                                        range=[0,1]
                                )
                        ),
                        height=500
                )

                st.plotly_chart(fig_radar, use_container_width=True, config=config)
            
        # ==========================
        # IMMUNOGENIC SCORE TAB
        # ==========================
        with tab_score:

                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("### 🧬 Global Immunogenic Score")

                st.markdown("""
        <div class="legend-box">

        <div class="legend-title">🧬 Score Explanation</div>

        <div class="legend-item">🎯 <b>Gauge Value</b> – Mean predicted epitope probability</div>

        <div class="legend-item">🧬 <b>Total Peptides</b> – Number of peptide windows analyzed</div>

        <div class="legend-item">🔥 <b>Predicted Epitopes</b> – Peptides above classification threshold</div>

        <div class="legend-item">📊 <b>Epitope Density</b> – Percentage of peptides predicted as epitopes</div>

        </div>
        """, unsafe_allow_html=True)
                mean_prob = df["Probability"].mean()
                total_pep = len(df)
                epi_count = len(df[df["Category"]=="Epitope"])

                density_score = epi_count/total_pep

                gauge = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=mean_prob,
                        number={'valueformat':".2f"},
                        title={'text':"Global Immunogenic Score"},
                        gauge={
                                'axis':{'range':[0,1]},
                                'bar':{'color':"#38bdf8"}
                        }
                ))

                st.plotly_chart(gauge, use_container_width=True, config=config)

                st.metric("Peptides scanned",total_pep)
                st.metric("Predicted epitopes",epi_count)
                st.metric("Epitope density",f"{density_score:.2%}")

        # ==========================
        # STACKED PROTEIN EPITOPE ATLAS
        # ==========================

        with tab_atlas:

                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("### 🧭 Stacked Protein Epitope Atlas")

                st.markdown("""
        <div class="legend-box">

        <div class="legend-title">🧭 Atlas Visualization Guide</div>

        <div class="legend-item">🔴 <b>Red Circles</b> – Predicted epitope peptides</div>

        <div class="legend-item">⚪ <b>Grey Circles</b> – Non-epitope peptide windows</div>

        <div class="legend-item">⭐ <b>Gold Stars</b> – Top high-confidence epitopes</div>

        <div class="legend-item">📏 <b>X-axis</b> – Protein sequence position</div>

        <div class="legend-item">📚 <b>Y-axis Tracks</b> – Stacked peptide windows to show overlaps</div>

        <div class="legend-item">📦 <b>Bubble Size</b> – Epitope prediction probability</div>

        </div>
        """, unsafe_allow_html=True)

                atlas_df = df.copy()

                # assign vertical tracks so overlapping peptides stack
                tracks = []
                current_track = 0

                for i in range(len(atlas_df)):
                        tracks.append(current_track)
                        current_track = (current_track + 1) % 6

                atlas_df["Track"] = tracks

                atlas_df["Color"] = atlas_df["Category"].map({
                        "Epitope": "red",
                        "Non-Epitope": "lightgray"
                })

                atlas_df["Size"] = atlas_df["Probability"] * 20 + 4

                fig_atlas = go.Figure()

                fig_atlas.add_trace(
                        go.Scatter(
                                x=atlas_df["Position"],
                                y=atlas_df["Track"],
                                mode="markers",
                                marker=dict(
                                        size=atlas_df["Size"],
                                        color=atlas_df["Color"],
                                        opacity=0.85
                                ),
                                hovertext=atlas_df["Peptide"],
                                name="Peptide Windows"
                        )
                )

                # highlight top epitopes
                top = atlas_df.nlargest(10, "Probability")

                fig_atlas.add_trace(
                        go.Scatter(
                                x=top["Position"],
                                y=top["Track"],
                                mode="markers",
                                marker=dict(
                                        size=18,
                                        color="gold",
                                        symbol="star"
                                ),
                                hovertext=top["Peptide"],
                                name="Top Epitopes"
                        )
                )

                fig_atlas.update_layout(
                        height=420,
                        xaxis_title="Protein Position",
                        yaxis_title="Peptide Track",
                        title="Stacked Epitope Atlas"
                )

                st.plotly_chart(fig_atlas, use_container_width=True, config=config)
        
        # ==========================
        # EPITOPE COMPETITION HEATMAP
        # ==========================

        with tab_competition:

                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("### ⚔️ Epitope Competition Heatmap")

                st.markdown("""
        <div class="legend-box">

        <div class="legend-title">⚔️ Epitope Competition Heatmap Guide</div>

        <div class="legend-item">
        <span style="color:#3b82f6;font-weight:700;">■ Blue regions</span> – Low epitope competition
        </div>

        <div class="legend-item">
        <span style="color:#facc15;font-weight:700;">■ Yellow regions</span> – Moderate overlap of predicted epitopes
        </div>

        <div class="legend-item">
        <span style="color:#ef4444;font-weight:700;">■ Red regions</span> – High epitope competition / dense overlapping peptides
        </div>

        <div class="legend-item">
        <b>X-axis</b> – Protein sequence position
        </div>

        <div class="legend-item">
        <b>Color intensity</b> – Degree of overlap between predicted epitope windows
        </div>

        <div class="legend-item">
        <b>Biological interpretation</b> – Red zones represent regions where multiple peptides compete for MHC-I presentation and may indicate immunodominant hotspots
        </div>

        </div>
        """, unsafe_allow_html=True)
            
                window = 10
                competition_scores = []

                for i in range(len(df)):

                        start = max(0, i-window)
                        end = min(len(df), i+window)

                        region = df.iloc[start:end]

                        competition_scores.append(region["Probability"].mean())

                comp_df = pd.DataFrame({
                        "Position": df["Position"],
                        "Competition_Score": competition_scores
                })

                # reshape for heatmap
                heat = comp_df["Competition_Score"].values.reshape(1,-1)

                fig = px.imshow(
                        heat,
                        aspect="auto",
                        color_continuous_scale="RdYlBu_r",
                        labels=dict(color="Competition Score")
                )

                fig.update_layout(
                        height=200,
                        xaxis_title="Protein Position",
                        yaxis=dict(showticklabels=False),
                        title="Epitope Competition Across Protein Sequence"
                )

                st.plotly_chart(fig, use_container_width=True, config=config)
            
                st.markdown("---")

                st.markdown("### 🏆 Dominant Immunogenic Regions")

                region_df = comp_df.sort_values(
                        by="Competition_Score",
                        ascending=False
                ).head(10)

                region_df.insert(0,"Rank",range(1,len(region_df)+1))

                st.dataframe(
                        region_df,
                        use_container_width=True,
                        hide_index=True
                )

        def section_title(text):
            return Table(
        [[text]],
        style=[
            ("BACKGROUND",(0,0),(-1,-1),"#2c3e50"),
            ("TEXTCOLOR",(0,0),(-1,-1),"white"),
            ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),
            ("FONTSIZE",(0,0),(-1,-1),14),
            ("ALIGN",(0,0),(-1,-1),"LEFT"),
            ("LEFTPADDING",(0,0),(-1,-1),10),
            ("TOPPADDING",(0,0),(-1,-1),6),
            ("BOTTOMPADDING",(0,0),(-1,-1),6),
        ]
    )
            
        # ==========================
        # GENERATE PDF (TABLES ONLY)
        # ==========================

        pdf_buffer = io.BytesIO()
        doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)

        styles = getSampleStyleSheet()
        elements = []

        # TITLE
        elements.append(Paragraph("<b>HPV EPIPRED</b>", styles['Title']))
        elements.append(Paragraph("AI-based MHC-I Epitope Prediction Report", styles['Normal']))
        elements.append(Spacer(1, 20))

        # SUMMARY
        elements.append(Paragraph("<b>Prediction Summary</b>", styles['Heading2']))
        elements.append(Spacer(1, 10))

        summary_data = [
                ["Metric","Value"],
                ["Total peptides analysed", len(df)],
                ["Predicted epitopes", len(epitope_df)],
                ["Predicted non-epitopes", len(non_df)],
                ["Prediction threshold", threshold]
        ]

        elements.append(Table(summary_data))
        elements.append(Spacer(1, 20))

        # TOP EPITOPES
        elements.append(Paragraph("<b>Top High-Confidence Epitopes</b>", styles['Heading2']))
        elements.append(Spacer(1, 10))

        top_data = [top10.columns.tolist()] + top10.values.tolist()
        elements.append(Table(top_data))
        elements.append(PageBreak())

        # ALL EPITOPES
        elements.append(Paragraph("<b>All Predicted Epitopes</b>", styles['Heading2']))
        elements.append(Spacer(1, 10))

        epi_data = [epitope_df.columns.tolist()] + epitope_df.values.tolist()
        elements.append(Table(epi_data))
        elements.append(PageBreak())

        # NON EPITOPES
        elements.append(Paragraph("<b>Non-Epitopes</b>", styles['Heading2']))
        elements.append(Spacer(1, 10))

        non_data = [non_df.columns.tolist()] + non_df.values.tolist()
        elements.append(Table(non_data))

        # BUILD PDF
        doc.build(elements)
        pdf_buffer.seek(0)

        st.download_button(
                label="📄 Download Tables Report",
                data=pdf_buffer,
                file_name="hpv_epipred_tables.pdf",
                mime="application/pdf"
        )
      
# ==========================
# FEATURE NAMES FOR EXPLAINABILITY
# ==========================

# Position features (10 × 21 = 210)
pos_features = []
for pos in range(1, 11):
    for aa in aa_list:
        pos_features.append(f"Pos{pos}_{aa}")

# Composition features (21)
comp_features = [f"Comp_{aa}" for aa in aa_list]

# Final feature names
feature_names = pos_features + comp_features

with tab2:

        st.markdown("### 📊 Model Feature Importance")

        importance = model.feature_importances_

        # FIX: match lengths safely
        min_len = min(len(feature_names), len(importance))

        imp_df = pd.DataFrame({
                "Feature": feature_names[:min_len],
                "Importance": importance[:min_len]
        }).sort_values(by="Importance", ascending=False).head(20)

        fig = px.bar(
                imp_df,
                x="Importance",
                y="Feature",
                orientation="h",
                title="Top Sequence Features Influencing MHC-I Epitope Prediction"
        )

        st.plotly_chart(fig, use_container_width=True)
    
st.markdown("""
<style>

/* ==========================
COMPACT PREMIUM FOOTER
========================== */

.footer {
    position: relative;
    margin-top: 40px;
    padding: 12px 10px;
    text-align: center;
    background: transparent;
    border-top: 1px solid rgba(99,102,241,0.15);
    font-size: 13px;
    color: #94a3b8;
}

.footer span {
    color: #e2e8f0;
    font-weight: 500;
}

.footer .highlight {
    background: linear-gradient(90deg,#6366f1,#22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

</style>

<div class="footer">
    <span>HPV EPIPRED</span> • AI-based Epitope Prediction  
    <br>
    © 2026 <span class="highlight">Shamroz Abrar</span> | All rights reserved.
</div>

""", unsafe_allow_html=True)
