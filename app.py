# import streamlit as st
# import time
# from agents import build_redear_agent, build_search_agent, writer_chain, critic_chain

# # ── Page config ──────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="Intellexa AI · AI Research Agent",
#     page_icon="🔬",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # ── Custom CSS ────────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

# /* ── Reset & base ── */
# html, body, [class*="css"] {
#     font-family: 'DM Sans', sans-serif;
#     color: #e8e4dc;
# }

# .stApp {
#     background: #0a0a0f;
#     background-image:
#         radial-gradient(ellipse 80% 50% at 20% -10%, rgba(255,140,50,0.12) 0%, transparent 60%),
#         radial-gradient(ellipse 60% 40% at 80% 110%, rgba(255,80,30,0.08) 0%, transparent 55%);
# }

# /* ── Hide default streamlit chrome ── */
# #MainMenu, footer, header { visibility: hidden; }
# .block-container { padding: 2rem 3rem 4rem; max-width: 1200px; }

# /* ── Hero header ── */
# .hero {
#     text-align: center;
#     padding: 3.5rem 0 2.5rem;
#     position: relative;
# }
# .hero-eyebrow {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.7rem;
#     font-weight: 500;
#     letter-spacing: 0.25em;
#     text-transform: uppercase;
#     color: #ff8c32;
#     margin-bottom: 1rem;
#     opacity: 0.9;
# }
# .hero h1 {
#     font-family: 'Syne', sans-serif;
#     font-size: clamp(2.8rem, 6vw, 5rem);
#     font-weight: 800;
#     line-height: 1.0;
#     letter-spacing: -0.03em;
#     color: #f0ebe0;
#     margin: 0 0 1rem;
# }
# .hero h1 span {
#     color: #ff8c32;
# }
# .hero-sub {
#     font-size: 1.05rem;
#     font-weight: 300;
#     color: #a09890;
#     max-width: 520px;
#     margin: 0 auto;
#     line-height: 1.65;
# }

# /* ── Divider ── */
# .divider {
#     height: 1px;
#     background: linear-gradient(90deg, transparent, rgba(255,140,50,0.3), transparent);
#     margin: 2rem 0;
# }

# /* ── Input card ── */
# .input-card {
#     background: rgba(255,255,255,0.03);
#     border: 1px solid rgba(255,140,50,0.15);
#     border-radius: 16px;
#     padding: 2rem 2.5rem;
#     margin-bottom: 2rem;
#     backdrop-filter: blur(8px);
# }

# /* ── Streamlit input overrides ── */
# .stTextInput > div > div > input {
#     background: rgba(255,255,255,0.05) !important;
#     border: 1px solid rgba(255,140,50,0.25) !important;
#     border-radius: 10px !important;
#     color: #f0ebe0 !important;
#     font-family: 'DM Sans', sans-serif !important;
#     font-size: 1rem !important;
#     padding: 0.75rem 1rem !important;
#     transition: border-color 0.2s, box-shadow 0.2s !important;
# }
# .stTextInput > div > div > input:focus {
#     border-color: #ff8c32 !important;
#     box-shadow: 0 0 0 3px rgba(255,140,50,0.12) !important;
# }
# .stTextInput > label {
#     font-family: 'DM Mono', monospace !important;
#     font-size: 0.72rem !important;
#     letter-spacing: 0.15em !important;
#     text-transform: uppercase !important;
#     color: #ff8c32 !important;
#     font-weight: 500 !important;
# }

# /* ── Button ── */
# .stButton > button {
#     background: linear-gradient(135deg, #ff8c32 0%, #ff5a1a 100%) !important;
#     color: #0a0a0f !important;
#     font-family: 'Syne', sans-serif !important;
#     font-weight: 700 !important;
#     font-size: 0.95rem !important;
#     letter-spacing: 0.04em !important;
#     border: none !important;
#     border-radius: 10px !important;
#     padding: 0.7rem 2.2rem !important;
#     cursor: pointer !important;
#     transition: transform 0.15s, box-shadow 0.15s, opacity 0.15s !important;
#     box-shadow: 0 4px 20px rgba(255,140,50,0.3) !important;
#     width: 100%;
# }
# .stButton > button:hover {
#     transform: translateY(-2px) !important;
#     box-shadow: 0 8px 28px rgba(255,140,50,0.4) !important;
#     opacity: 0.95 !important;
# }
# .stButton > button:active {
#     transform: translateY(0) !important;
# }

# /* ── Pipeline step cards ── */
# .step-card {
#     background: rgba(255,255,255,0.03);
#     border: 1px solid rgba(255,255,255,0.07);
#     border-radius: 14px;
#     padding: 1.5rem 1.8rem;
#     margin-bottom: 1.2rem;
#     position: relative;
#     overflow: hidden;
#     transition: border-color 0.3s;
# }
# .step-card.active {
#     border-color: rgba(255,140,50,0.4);
#     background: rgba(255,140,50,0.04);
# }
# .step-card.done {
#     border-color: rgba(80,200,120,0.3);
#     background: rgba(80,200,120,0.03);
# }
# .step-card::before {
#     content: '';
#     position: absolute;
#     left: 0; top: 0; bottom: 0;
#     width: 3px;
#     border-radius: 14px 0 0 14px;
#     background: rgba(255,255,255,0.05);
#     transition: background 0.3s;
# }
# .step-card.active::before { background: #ff8c32; }
# .step-card.done::before   { background: #50c878; }

# .step-header {
#     display: flex;
#     align-items: center;
#     gap: 0.8rem;
#     margin-bottom: 0.3rem;
# }
# .step-num {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.68rem;
#     font-weight: 500;
#     letter-spacing: 0.15em;
#     color: #ff8c32;
#     opacity: 0.7;
# }
# .step-title {
#     font-family: 'Syne', sans-serif;
#     font-size: 0.95rem;
#     font-weight: 700;
#     color: #f0ebe0;
# }
# .step-status {
#     margin-left: auto;
#     font-family: 'DM Mono', monospace;
#     font-size: 0.68rem;
#     letter-spacing: 0.1em;
# }
# .status-waiting  { color: #555; }
# .status-running  { color: #ff8c32; }
# .status-done     { color: #50c878; }

# /* ── Result panels ── */
# .result-panel {
#     background: rgba(255,255,255,0.025);
#     border: 1px solid rgba(255,255,255,0.07);
#     border-radius: 14px;
#     padding: 1.8rem 2rem;
#     margin-top: 1rem;
#     margin-bottom: 1.5rem;
# }
# .result-panel-title {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.7rem;
#     font-weight: 500;
#     letter-spacing: 0.2em;
#     text-transform: uppercase;
#     color: #ff8c32;
#     margin-bottom: 1rem;
#     padding-bottom: 0.7rem;
#     border-bottom: 1px solid rgba(255,140,50,0.15);
# }
# .result-content {
#     font-size: 0.92rem;
#     line-height: 1.8;
#     color: #cdc8bf;
#     white-space: pre-wrap;
#     font-family: 'DM Sans', sans-serif;
# }

# /* ── Report & feedback panels ── */
# .report-panel {
#     background: rgba(255,255,255,0.025);
#     border: 1px solid rgba(255,140,50,0.2);
#     border-radius: 16px;
#     padding: 2rem 2.5rem;
#     margin-top: 1rem;
# }
# .feedback-panel {
#     background: rgba(255,255,255,0.025);
#     border: 1px solid rgba(80,200,120,0.2);
#     border-radius: 16px;
#     padding: 2rem 2.5rem;
#     margin-top: 1rem;
# }
# .panel-label {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.7rem;
#     letter-spacing: 0.2em;
#     text-transform: uppercase;
#     margin-bottom: 1.2rem;
#     padding-bottom: 0.7rem;
# }
# .panel-label.orange {
#     color: #ff8c32;
#     border-bottom: 1px solid rgba(255,140,50,0.15);
# }
# .panel-label.green {
#     color: #50c878;
#     border-bottom: 1px solid rgba(80,200,120,0.15);
# }

# /* ── Progress text ── */
# .stSpinner > div { color: #ff8c32 !important; }

# /* ── Expander ── */
# details summary {
#     font-family: 'DM Mono', monospace !important;
#     font-size: 0.75rem !important;
#     color: #a09890 !important;
#     letter-spacing: 0.1em !important;
#     cursor: pointer;
# }

# /* ── Section heading ── */
# .section-heading {
#     font-family: 'Syne', sans-serif;
#     font-size: 1.3rem;
#     font-weight: 700;
#     color: #f0ebe0;
#     margin: 2rem 0 1rem;
# }

# /* ── Toast-style notice ── */
# .notice {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.72rem;
#     color: #605850;
#     text-align: center;
#     margin-top: 3rem;
#     letter-spacing: 0.08em;
# }
# </style>
# """, unsafe_allow_html=True)


# # ── Helper: render a step card ────────────────────────────────────────────────
# def step_card(num: str, title: str, state: str, desc: str = ""):
#     status_map = {
#         "waiting": ("WAITING", "status-waiting"),
#         "running": ("● RUNNING", "status-running"),
#         "done":    ("✓ DONE",   "status-done"),
#     }
#     label, cls = status_map.get(state, ("", ""))
#     card_cls = {"running": "active", "done": "done"}.get(state, "")
#     st.markdown(f"""
#     <div class="step-card {card_cls}">
#         <div class="step-header">
#             <span class="step-num">{num}</span>
#             <span class="step-title">{title}</span>
#             <span class="step-status {cls}">{label}</span>
#         </div>
#         {"<div style='font-size:0.82rem;color:#706860;margin-top:0.3rem;'>"+desc+"</div>" if desc else ""}
#     </div>
#     """, unsafe_allow_html=True)


# # ── Session state init ────────────────────────────────────────────────────────
# for key in ("results", "running", "done"):
#     if key not in st.session_state:
#         st.session_state[key] = {} if key == "results" else False


# # ── Hero ──────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="hero">
#     <div class="hero-eyebrow">Multi-Agent AI System - Powered By Dhiraj Rupnawar</div>
#     <h1>Intellexa <span>AI</span></h1>
#     <p class="hero-sub">
#         Four specialized AI agents collaborate — searching, scraping, writing,
#         and critiquing — to deliver a polished research report on any topic.
#     </p>
# </div>
# <div class="divider"></div>
# """, unsafe_allow_html=True)


# # ── Layout: input left, pipeline right ───────────────────────────────────────
# col_input, col_spacer, col_pipeline = st.columns([5, 0.5, 4])

# with col_input:
#     st.markdown('<div class="input-card">', unsafe_allow_html=True)
#     topic = st.text_input(
#         "Research Topic",
#         placeholder="e.g. Quantum computing breakthroughs in 2025",
#         key="topic_input",
#         label_visibility="visible",
#     )
#     run_btn = st.button("⚡  Run Research Pipeline", use_container_width=True)
#     st.markdown('</div>', unsafe_allow_html=True)

#     # Example chips
#     st.markdown("""
#     <div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-bottom:1.5rem;">
#         <span style="font-family:'DM Mono',monospace;font-size:0.68rem;color:#605850;letter-spacing:0.1em;">TRY →</span>
#     """, unsafe_allow_html=True)
#     examples = ["LLM agents 2025", "CRISPR gene editing", "Fusion energy progress"]
#     for ex in examples:
#         st.markdown(f"""
#         <span style="
#             background:rgba(255,255,255,0.04);
#             border:1px solid rgba(255,255,255,0.08);
#             border-radius:6px;
#             padding:0.25rem 0.7rem;
#             font-size:0.75rem;
#             color:#a09890;
#             font-family:'DM Sans',sans-serif;
#             cursor:default;
#         ">{ex}</span>
#         """, unsafe_allow_html=True)
#     st.markdown("</div>", unsafe_allow_html=True)

# with col_pipeline:
#     st.markdown('<div class="section-heading">Pipeline</div>', unsafe_allow_html=True)

#     r = st.session_state.results
#     done = st.session_state.done

#     def s(step):
#         if not r:
#             return "waiting"
#         steps = ["search", "reader", "writer", "critic"]
#         idx = steps.index(step)
#         completed = list(r.keys())
#         # figure out which steps are done
#         if step in r:
#             return "done"
#         # which step is running now (first not in r)
#         if st.session_state.running:
#             for i, k in enumerate(steps):
#                 if k not in r:
#                     return "running" if k == step else "waiting"
#         return "waiting"

#     step_card("01", "Search Agent",  s("search"), "Gathers recent web information")
#     step_card("02", "Reader Agent",  s("reader"), "Scrapes & extracts deep content")
#     step_card("03", "Writer Chain",  s("writer"), "Drafts the full research report")
#     step_card("04", "Critic Chain",  s("critic"), "Reviews & scores the report")


# # ── Run pipeline ──────────────────────────────────────────────────────────────
# if run_btn:
#     if not topic.strip():
#         st.warning("Please enter a research topic first.")
#     else:
#         st.session_state.results = {}
#         st.session_state.running = True
#         st.session_state.done = False
#         st.rerun()

# if st.session_state.running and not st.session_state.done:
#     results = {}
#     topic_val = st.session_state.topic_input

#     # ── Step 1: Search ──
#     with st.spinner("🔍  Search Agent is working…"):
#         search_agent = build_search_agent()
#         sr = search_agent.invoke({
#             "messages": [("user", f"Find recent, reliable and detailed information about: {topic_val}")]
#         })
#         results["search"] = sr["messages"][-1].content
#         st.session_state.results = dict(results)
#     st.rerun() if False else None   # keep inline for now

#     # ── Step 2: Reader ──
#     with st.spinner("📄  Reader Agent is scraping top resources…"):
#         reader_agent = build_redear_agent()
#         rr = reader_agent.invoke({
#             "messages": [("user",
#                 f"Based on the following search results about '{topic_val}', "
#                 f"pick the most relevant URL and scrape it for deeper content.\n\n"
#                 f"Search Results:\n{results['search'][:800]}"
#             )]
#         })
#         results["reader"] = rr["messages"][-1].content
#         st.session_state.results = dict(results)

#     # ── Step 3: Writer ──
#     with st.spinner("✍️  Writer is drafting the report…"):
#         research_combined = (
#             f"SEARCH RESULTS:\n{results['search']}\n\n"
#             f"DETAILED SCRAPED CONTENT:\n{results['reader']}"
#         )
#         results["writer"] = writer_chain.invoke({
#             "topic": topic_val,
#             "research": research_combined
#         })
#         st.session_state.results = dict(results)

#     # ── Step 4: Critic ──
#     with st.spinner("🧐  Critic is reviewing the report…"):
#         results["critic"] = critic_chain.invoke({
#             "report": results["writer"]
#         })
#         st.session_state.results = dict(results)

#     st.session_state.running = False
#     st.session_state.done = True
#     st.rerun()


# # ── Results display ───────────────────────────────────────────────────────────
# r = st.session_state.results

# if r:
#     st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
#     st.markdown('<div class="section-heading">Results</div>', unsafe_allow_html=True)

#     # Raw outputs in expanders
#     if "search" in r:
#         with st.expander("🔍 Search Results (raw)", expanded=False):
#             st.markdown(f'<div class="result-panel"><div class="result-panel-title">Search Agent Output</div>'
#                         f'<div class="result-content">{r["search"]}</div></div>', unsafe_allow_html=True)

#     if "reader" in r:
#         with st.expander("📄 Scraped Content (raw)", expanded=False):
#             st.markdown(f'<div class="result-panel"><div class="result-panel-title">Reader Agent Output</div>'
#                         f'<div class="result-content">{r["reader"]}</div></div>', unsafe_allow_html=True)

#     # Final report
#     if "writer" in r:
#         st.markdown("""
#         <div class="report-panel">
#             <div class="panel-label orange">📝 Final Research Report</div>
#         """, unsafe_allow_html=True)
#         st.markdown(r["writer"])   # render markdown natively
#         st.markdown("</div>", unsafe_allow_html=True)

#         # Download
#         st.download_button(
#             label="⬇  Download Report (.md)",
#             data=r["writer"],
#             file_name=f"research_report_{int(time.time())}.md",
#             mime="text/markdown",
#         )

#     # Critic feedback
#     if "critic" in r:
#         st.markdown("""
#         <div class="feedback-panel">
#             <div class="panel-label green">🧐 Critic Feedback</div>
#         """, unsafe_allow_html=True)
#         st.markdown(r["critic"])
#         st.markdown("</div>", unsafe_allow_html=True)


# # ── Footer ────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="notice">
#     Intellexa AI · Powered by LangChain multi-agent pipeline · Built with Streamlit . All Rights Belongs to Dhiraj Rupnawar
# </div>
# """, unsafe_allow_html=True)

import streamlit as st
import time
from agents import build_redear_agent, build_search_agent, writer_chain, critic_chain

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Intellexa Research",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700;14..32,800&display=swap');

/* ── Reset & base ── */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: #0a0a0a;
    background-image: 
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(120, 120, 120, 0.08), transparent),
        radial-gradient(ellipse 40% 30% at 100% 100%, rgba(100, 100, 100, 0.04), transparent);
}

/* ── Hide default streamlit chrome ── */
#MainMenu, footer, header { 
    visibility: hidden; 
}
.block-container {
    padding: 0rem 2rem 2rem;
    max-width: 1300px;
}

/* ── Typography ── */
h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    letter-spacing: -0.02em;
}

/* ── Navigation ── */
.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.25rem 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    margin-bottom: 3rem;
}
.nav-left {
    display: flex;
    align-items: center;
    gap: 2rem;
}
.logo {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1.25rem;
    font-weight: 600;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #ffffff 0%, #a0a0a0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.logo-icon {
    background: rgba(255, 255, 255, 0.1);
    padding: 0.3rem;
    border-radius: 8px;
    font-size: 1rem;
    -webkit-text-fill-color: white;
}
.nav-links {
    display: flex;
    gap: 1.5rem;
}
.nav-links a {
    color: #888;
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 500;
    transition: color 0.2s;
}
.nav-links a:hover {
    color: #fff;
}
.nav-right {
    display: flex;
    gap: 1rem;
}
.nav-btn {
    background: transparent;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 0.5rem 1rem;
    border-radius: 8px;
    color: #fff;
    font-size: 0.85rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
}
.nav-btn:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: rgba(255, 255, 255, 0.2);
}

/* ── Hero Section ── */
.hero {
    text-align: center;
    padding: 3rem 0 4rem;
}
.hero-badge {
    display: inline-block;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 100px;
    padding: 0.4rem 1rem;
    font-size: 0.75rem;
    font-weight: 500;
    color: #aaa;
    margin-bottom: 1.5rem;
}
.hero h1 {
    font-size: 4rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    line-height: 1.1;
    background: linear-gradient(135deg, #ffffff 0%, #e0e0e0 50%, #888888 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}
.hero-sub {
    font-size: 1.1rem;
    color: #666;
    max-width: 500px;
    margin: 0 auto;
    line-height: 1.5;
}

/* ── Main Container ── */
.main-container {
    max-width: 900px;
    margin: 0 auto;
}

/* ── Input Section ── */
.input-section {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 24px;
    padding: 2rem;
    margin: 2rem 0;
}
.input-label {
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #888;
    margin-bottom: 0.75rem;
}
.stTextInput > div > div > input {
    background: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 16px !important;
    color: #fff !important;
    font-size: 1rem !important;
    padding: 0.9rem 1rem !important;
    transition: all 0.2s !important;
}
.stTextInput > div > div > input:focus {
    border-color: rgba(255, 255, 255, 0.2) !important;
    box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.05) !important;
}
.stTextInput > div > div > input::placeholder {
    color: #444 !important;
}

/* ── Examples Grid ── */
.examples-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.75rem;
    margin-top: 1rem;
}
.example-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 12px;
    padding: 0.6rem 0.8rem;
    font-size: 0.8rem;
    color: #aaa;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s;
}
.example-card:hover {
    background: rgba(255, 255, 255, 0.04);
    border-color: rgba(255, 255, 255, 0.12);
    color: #fff;
}

/* ── Run Button ── */
.run-button {
    margin-top: 1.5rem;
}
.stButton > button {
    background: #fff !important;
    color: #000 !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    padding: 0.8rem 1.5rem !important;
    border-radius: 40px !important;
    border: none !important;
    width: 100%;
    cursor: pointer !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    transform: scale(0.98) !important;
    background: #e0e0e0 !important;
}
.stButton > button:active {
    transform: scale(0.97) !important;
}

/* ── Pipeline Status ── */
.pipeline-status {
    margin: 2rem 0;
}
.pipeline-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 1rem;
}
.pipeline-title {
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #888;
}
.pipeline-steps {
    display: flex;
    gap: 0.5rem;
}
.pipeline-step {
    flex: 1;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
    transition: all 0.3s;
}
.pipeline-step.active {
    border-color: rgba(255, 255, 255, 0.2);
    background: rgba(255, 255, 255, 0.04);
}
.pipeline-step.completed {
    border-color: rgba(100, 255, 100, 0.2);
    background: rgba(100, 255, 100, 0.02);
}
.step-icon {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}
.step-name {
    font-size: 0.7rem;
    font-weight: 500;
    color: #fff;
    margin-bottom: 0.25rem;
}
.step-desc {
    font-size: 0.6rem;
    color: #555;
}
.step-indicator {
    display: inline-block;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #555;
    margin-top: 0.5rem;
}
.step-indicator.active {
    background: #fff;
    box-shadow: 0 0 8px rgba(255, 255, 255, 0.5);
}
.step-indicator.completed {
    background: #64ff64;
}

/* ── Results Section ── */
.results-section {
    margin-top: 3rem;
}
.results-header {
    font-size: 1.5rem;
    font-weight: 600;
    letter-spacing: -0.02em;
    color: #fff;
    margin-bottom: 1.5rem;
}

/* ── Collapsible Raw Data ── */
details {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 16px;
    margin-bottom: 1rem;
}
summary {
    padding: 1rem 1.5rem;
    cursor: pointer;
    font-size: 0.85rem;
    font-weight: 500;
    color: #aaa;
    user-select: none;
}
summary:hover {
    color: #fff;
}
.raw-content {
    padding: 1rem 1.5rem 1.5rem;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    font-size: 0.8rem;
    color: #888;
    line-height: 1.6;
    white-space: pre-wrap;
}

/* ── Report Card ── */
.report-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 24px;
    padding: 2rem;
    margin: 1.5rem 0;
}
.report-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}
.report-title {
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #aaa;
}
.report-content {
    font-size: 0.95rem;
    line-height: 1.7;
    color: #ccc;
}
.report-content h1, .report-content h2, .report-content h3 {
    color: #fff;
    margin-top: 1.5rem;
    margin-bottom: 0.75rem;
}
.report-content p {
    margin-bottom: 1rem;
}
.report-content code {
    background: rgba(255, 255, 255, 0.05);
    padding: 0.2rem 0.4rem;
    border-radius: 6px;
    font-size: 0.85rem;
}
.report-content pre {
    background: rgba(255, 255, 255, 0.03);
    padding: 1rem;
    border-radius: 12px;
    overflow-x: auto;
}

/* ── Download Section ── */
.download-section {
    text-align: center;
    margin: 2rem 0;
}
.download-btn {
    display: inline-block;
    background: transparent;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 0.7rem 1.5rem;
    border-radius: 40px;
    color: #fff;
    font-size: 0.85rem;
    font-weight: 500;
    text-decoration: none;
    transition: all 0.2s;
    cursor: pointer;
}
.download-btn:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: rgba(255, 255, 255, 0.2);
}

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 3rem 2rem 2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    margin-top: 4rem;
}
.footer-text {
    font-size: 0.7rem;
    color: #444;
    letter-spacing: 0.02em;
}

/* ── Spinner Override ── */
.stSpinner > div {
    color: #fff !important;
    border-color: #fff transparent transparent transparent !important;
}

/* ── Alert ── */
.stAlert {
    background: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    color: #fff !important;
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)


# ── Navigation ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="nav">
    <div class="nav-left">
        <div class="logo">
            <span class="logo-icon">✨</span>
            <span>Intellexa</span>
        </div>
        <div class="nav-links">
            <a href="#">Research</a>
            <a href="#">Agents</a>
            <a href="#">Documentation</a>
        </div>
    </div>
    <div class="nav-right">
        <div class="nav-btn">Sign in</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── Hero Section ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">Multi-Agent Research System</div>
    <h1>Intelligent research,<br>automated.</h1>
    <p class="hero-sub">Four specialized AI agents working together to deliver comprehensive research reports.</p>
</div>
""", unsafe_allow_html=True)


# ── Session state init ────────────────────────────────────────────────────────
for key in ("results", "running", "done"):
    if key not in st.session_state:
        st.session_state[key] = {} if key == "results" else False


# ── Main Content Container ────────────────────────────────────────────────────
st.markdown('<div class="main-container">', unsafe_allow_html=True)


# ── Input Section ─────────────────────────────────────────────────────────────
st.markdown('<div class="input-section">', unsafe_allow_html=True)
st.markdown('<div class="input-label">Research topic</div>', unsafe_allow_html=True)

topic = st.text_input(
    "",
    placeholder="e.g., The future of autonomous agents",
    key="topic_input",
    label_visibility="collapsed",
)

st.markdown("""
<div class="examples-grid">
    <div class="example-card">LLM reasoning capabilities</div>
    <div class="example-card">Multimodal AI systems</div>
    <div class="example-card">AI safety research 2025</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="run-button">', unsafe_allow_html=True)
run_btn = st.button("Start research →", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# ── Pipeline Status (shown only when running or completed) ────────────────────
if st.session_state.running or st.session_state.results:
    st.markdown('<div class="pipeline-status">', unsafe_allow_html=True)
    st.markdown('<div class="pipeline-header">', unsafe_allow_html=True)
    st.markdown('<div class="pipeline-title">Research pipeline</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="pipeline-steps">', unsafe_allow_html=True)
    
    steps = [
        {"name": "Search", "desc": "Gathering", "icon": "🔍"},
        {"name": "Read", "desc": "Extracting", "icon": "📖"},
        {"name": "Write", "desc": "Synthesizing", "icon": "✍️"},
        {"name": "Review", "desc": "Quality check", "icon": "✓"}
    ]
    
    r = st.session_state.results
    for idx, step in enumerate(steps):
        step_key = ["search", "reader", "writer", "critic"][idx]
        if not r:
            status_class = ""
            indicator_class = ""
        elif step_key in r:
            status_class = "completed"
            indicator_class = "completed"
        elif st.session_state.running:
            # Find the first incomplete step
            for i, k in enumerate(["search", "reader", "writer", "critic"]):
                if k not in r:
                    status_class = "active" if i == idx else ""
                    indicator_class = "active" if i == idx else ""
                    break
        else:
            status_class = ""
            indicator_class = ""
        
        st.markdown(f"""
        <div class="pipeline-step {status_class}">
            <div class="step-icon">{step['icon']}</div>
            <div class="step-name">{step['name']}</div>
            <div class="step-desc">{step['desc']}</div>
            <div class="step-indicator {indicator_class}"></div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ── Run pipeline ──────────────────────────────────────────────────────────────
if run_btn:
    if not topic.strip():
        st.warning("Please enter a research topic to begin.")
    else:
        st.session_state.results = {}
        st.session_state.running = True
        st.session_state.done = False
        st.rerun()

if st.session_state.running and not st.session_state.done:
    results = {}
    topic_val = st.session_state.topic_input

    with st.spinner(""):
        # Step 1: Search
        search_agent = build_search_agent()
        sr = search_agent.invoke({
            "messages": [("user", f"Find recent, reliable and detailed information about: {topic_val}")]
        })
        results["search"] = sr["messages"][-1].content
        st.session_state.results = dict(results)

        # Step 2: Reader
        reader_agent = build_redear_agent()
        rr = reader_agent.invoke({
            "messages": [("user",
                f"Based on the following search results about '{topic_val}', "
                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                f"Search Results:\n{results['search'][:800]}"
            )]
        })
        results["reader"] = rr["messages"][-1].content
        st.session_state.results = dict(results)

        # Step 3: Writer
        research_combined = (
            f"SEARCH RESULTS:\n{results['search']}\n\n"
            f"DETAILED SCRAPED CONTENT:\n{results['reader']}"
        )
        results["writer"] = writer_chain.invoke({
            "topic": topic_val,
            "research": research_combined
        })
        st.session_state.results = dict(results)

        # Step 4: Critic
        results["critic"] = critic_chain.invoke({
            "report": results["writer"]
        })
        st.session_state.results = dict(results)

    st.session_state.running = False
    st.session_state.done = True
    st.rerun()


# ── Results Section ───────────────────────────────────────────────────────────
r = st.session_state.results

if r:
    st.markdown('<div class="results-section">', unsafe_allow_html=True)
    
    # Raw data in expandable sections
    if "search" in r:
        with st.expander("Search results"):
            st.markdown(f'<div class="raw-content">{r["search"]}</div>', unsafe_allow_html=True)
    
    if "reader" in r:
        with st.expander("Extracted content"):
            st.markdown(f'<div class="raw-content">{r["reader"]}</div>', unsafe_allow_html=True)
    
    # Final Report
    if "writer" in r:
        st.markdown("""
        <div class="report-card">
            <div class="report-header">
                <div class="report-title">Research report</div>
            </div>
            <div class="report-content">
        """, unsafe_allow_html=True)
        
        st.markdown(r["writer"])
        
        st.markdown('</div></div>', unsafe_allow_html=True)
        
        # Download
        st.markdown('<div class="download-section">', unsafe_allow_html=True)
        st.download_button(
            label="Download report (Markdown)",
            data=r["writer"],
            file_name=f"research_report_{int(time.time())}.md",
            mime="text/markdown",
            use_container_width=False,
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Critic Feedback
    if "critic" in r:
        with st.expander("Review feedback"):
            st.markdown(f'<div class="raw-content">{r["critic"]}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


st.markdown('</div>', unsafe_allow_html=True)


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-text">
        Intellexa Research · Powered by multi-agent AI · Built with LangChain & Streamlit
    </div>
    <div class="footer-text" style="margin-top: 0.5rem;">
        Dhiraj Rupnawar
    </div>
</div>
""", unsafe_allow_html=True)