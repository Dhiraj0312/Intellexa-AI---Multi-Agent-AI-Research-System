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

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Intellexa · Research Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,600;1,9..144,300&family=Geist+Mono:wght@300;400;500&family=Geist:wght@300;400;500;600&display=swap');

/* ── Base ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: 'Geist', sans-serif;
    color: #1a1a1a;
}

.stApp {
    background-color: #f5f2ed;
    background-image:
        linear-gradient(180deg, #ede9e2 0%, #f5f2ed 120px);
}

#MainMenu, footer, header { visibility: hidden; }

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── Top navigation bar ── */
.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 3rem;
    height: 56px;
    background: rgba(245, 242, 237, 0.85);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(0,0,0,0.07);
    position: sticky;
    top: 0;
    z-index: 100;
}
.topbar-logo {
    font-family: 'Fraunces', serif;
    font-size: 1.1rem;
    font-weight: 600;
    letter-spacing: -0.01em;
    color: #1a1a1a;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.topbar-logo .dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #2563eb;
    display: inline-block;
}
.topbar-nav {
    font-family: 'Geist Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #888;
    display: flex;
    gap: 2rem;
}
.topbar-badge {
    font-family: 'Geist Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #2563eb;
    border: 1px solid rgba(37,99,235,0.3);
    background: rgba(37,99,235,0.06);
    padding: 0.2rem 0.6rem;
    border-radius: 100px;
}

/* ── Page wrapper ── */
.page-wrap {
    max-width: 1100px;
    margin: 0 auto;
    padding: 3rem 2.5rem 5rem;
}

/* ── Hero ── */
.hero {
    padding: 3.5rem 0 3rem;
    border-bottom: 1px solid rgba(0,0,0,0.08);
    margin-bottom: 3rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    align-items: end;
}
.hero-left {}
.hero-kicker {
    font-family: 'Geist Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #2563eb;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.hero-kicker::before {
    content: '';
    display: block;
    width: 20px;
    height: 1px;
    background: #2563eb;
}
.hero h1 {
    font-family: 'Fraunces', serif;
    font-size: clamp(3rem, 5vw, 4.5rem);
    font-weight: 600;
    line-height: 1.0;
    letter-spacing: -0.04em;
    color: #0f0f0f;
    margin: 0 0 1rem;
}
.hero h1 em {
    font-style: italic;
    font-weight: 300;
    color: #4b5563;
}
.hero-right {
    padding-bottom: 0.5rem;
}
.hero-desc {
    font-size: 0.95rem;
    font-weight: 300;
    color: #6b7280;
    line-height: 1.75;
    max-width: 380px;
    margin-left: auto;
    border-left: 2px solid rgba(0,0,0,0.08);
    padding-left: 1.5rem;
}
.hero-stat-row {
    display: flex;
    gap: 2rem;
    margin-top: 2rem;
    padding-left: 1.5rem;
    border-left: 2px solid rgba(0,0,0,0.08);
}
.hero-stat {}
.hero-stat-num {
    font-family: 'Fraunces', serif;
    font-size: 1.5rem;
    font-weight: 600;
    color: #0f0f0f;
}
.hero-stat-label {
    font-size: 0.72rem;
    color: #9ca3af;
    margin-top: 0.1rem;
    font-weight: 300;
}

/* ── Body layout ── */
.body-grid {
    display: grid;
    grid-template-columns: 1fr 340px;
    gap: 2.5rem;
    align-items: start;
}

/* ── Input section ── */
.input-section-label {
    font-family: 'Geist Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #9ca3af;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.input-section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(0,0,0,0.08);
}

/* Streamlit input ── */
.stTextInput > div > div > input {
    background: #ffffff !important;
    border: 1px solid rgba(0,0,0,0.12) !important;
    border-radius: 8px !important;
    color: #0f0f0f !important;
    font-family: 'Geist', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 300 !important;
    padding: 0.85rem 1.1rem !important;
    transition: border-color 0.15s, box-shadow 0.15s !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04) !important;
}
.stTextInput > div > div > input:focus {
    border-color: #2563eb !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.1) !important;
}
.stTextInput > div > div > input::placeholder {
    color: #c4c4c4 !important;
    font-style: italic !important;
}
.stTextInput > label {
    display: none !important;
}

/* ── Button ── */
.stButton > button {
    background: #0f0f0f !important;
    color: #f5f2ed !important;
    font-family: 'Geist', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
    letter-spacing: 0.01em !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.75rem 2rem !important;
    cursor: pointer !important;
    transition: background 0.15s, transform 0.1s !important;
    width: 100%;
    box-shadow: none !important;
}
.stButton > button:hover {
    background: #2563eb !important;
    transform: none !important;
}
.stButton > button:active {
    transform: scale(0.99) !important;
}

/* ── Example chips ── */
.chip-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 1rem;
}
.chip {
    font-family: 'Geist Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.05em;
    color: #6b7280;
    background: rgba(0,0,0,0.04);
    border: 1px solid rgba(0,0,0,0.07);
    border-radius: 100px;
    padding: 0.25rem 0.75rem;
    cursor: default;
    transition: background 0.1s;
}

/* ── Pipeline sidebar ── */
.pipeline-header {
    font-family: 'Geist Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #9ca3af;
    margin-bottom: 1.25rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.pipeline-header::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(0,0,0,0.08);
}

.pipeline-step {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 1rem 1.1rem;
    border-radius: 10px;
    margin-bottom: 0.6rem;
    background: #fff;
    border: 1px solid rgba(0,0,0,0.07);
    position: relative;
    transition: border-color 0.2s, background 0.2s;
}
.pipeline-step.active {
    border-color: rgba(37,99,235,0.3);
    background: rgba(37,99,235,0.03);
}
.pipeline-step.done {
    border-color: rgba(22,163,74,0.25);
    background: rgba(22,163,74,0.02);
}
.step-icon-wrap {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    border: 1px solid rgba(0,0,0,0.08);
    background: #f9f8f6;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    font-size: 0.85rem;
    transition: all 0.2s;
}
.pipeline-step.active .step-icon-wrap {
    background: rgba(37,99,235,0.08);
    border-color: rgba(37,99,235,0.2);
}
.pipeline-step.done .step-icon-wrap {
    background: rgba(22,163,74,0.08);
    border-color: rgba(22,163,74,0.2);
}
.step-body {}
.step-name {
    font-size: 0.82rem;
    font-weight: 500;
    color: #1a1a1a;
    margin-bottom: 0.1rem;
}
.step-desc {
    font-size: 0.72rem;
    color: #9ca3af;
    font-weight: 300;
}
.step-badge {
    margin-left: auto;
    font-family: 'Geist Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 0.08em;
    padding: 0.2rem 0.5rem;
    border-radius: 100px;
    white-space: nowrap;
    flex-shrink: 0;
}
.badge-wait { color: #c4c4c4; background: rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.05); }
.badge-run  { color: #2563eb; background: rgba(37,99,235,0.08); border: 1px solid rgba(37,99,235,0.2); }
.badge-done { color: #16a34a; background: rgba(22,163,74,0.08); border: 1px solid rgba(22,163,74,0.2); }

/* ── Results ── */
.results-section {
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid rgba(0,0,0,0.08);
}
.results-label {
    font-family: 'Geist Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #9ca3af;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.results-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(0,0,0,0.08);
}

.raw-output {
    background: #fff;
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 10px;
    padding: 1.25rem 1.5rem;
    font-family: 'Geist Mono', monospace;
    font-size: 0.75rem;
    color: #4b5563;
    line-height: 1.8;
    white-space: pre-wrap;
    max-height: 320px;
    overflow-y: auto;
}

.report-wrap {
    background: #fff;
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 12px;
    padding: 2.5rem 3rem;
    margin-bottom: 1.5rem;
}
.report-meta {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding-bottom: 1.5rem;
    margin-bottom: 2rem;
    border-bottom: 1px solid rgba(0,0,0,0.07);
}
.report-tag {
    font-family: 'Geist Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #2563eb;
    background: rgba(37,99,235,0.07);
    border: 1px solid rgba(37,99,235,0.15);
    padding: 0.2rem 0.65rem;
    border-radius: 100px;
}
.report-ts {
    font-family: 'Geist Mono', monospace;
    font-size: 0.65rem;
    color: #c4c4c4;
    margin-left: auto;
}

.critic-wrap {
    background: #f9fafb;
    border: 1px solid rgba(0,0,0,0.07);
    border-radius: 12px;
    padding: 1.75rem 2rem;
    margin-top: 1.5rem;
    border-left: 3px solid #16a34a;
}
.critic-label {
    font-family: 'Geist Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #16a34a;
    margin-bottom: 1.25rem;
}

/* ── Expander styling ── */
details {
    border: 1px solid rgba(0,0,0,0.07) !important;
    border-radius: 8px !important;
    margin-bottom: 0.75rem !important;
    overflow: hidden !important;
    background: #fff !important;
}
details summary {
    font-family: 'Geist Mono', monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 0.08em !important;
    color: #6b7280 !important;
    padding: 0.85rem 1.25rem !important;
    cursor: pointer !important;
    list-style: none !important;
    border-bottom: 1px solid transparent !important;
    transition: background 0.1s !important;
}
details[open] summary {
    border-bottom-color: rgba(0,0,0,0.07) !important;
    background: #fafaf9 !important;
}

/* ── Download button ── */
.stDownloadButton > button {
    background: transparent !important;
    color: #2563eb !important;
    font-family: 'Geist Mono', monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    border: 1px solid rgba(37,99,235,0.25) !important;
    border-radius: 8px !important;
    padding: 0.5rem 1.25rem !important;
    width: auto !important;
    box-shadow: none !important;
}
.stDownloadButton > button:hover {
    background: rgba(37,99,235,0.05) !important;
    border-color: rgba(37,99,235,0.4) !important;
}

/* ── Spinner ── */
.stSpinner > div { color: #2563eb !important; }

/* ── Footer ── */
.site-footer {
    text-align: center;
    padding: 3rem 0 2rem;
    font-family: 'Geist Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.1em;
    color: #c4c4c4;
    border-top: 1px solid rgba(0,0,0,0.06);
    margin-top: 4rem;
}
</style>
""", unsafe_allow_html=True)


# ── Topbar ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topbar">
    <div class="topbar-logo">
        <span class="dot"></span>
        Intellexa
    </div>
    <div class="topbar-nav">
        <span>Research</span>
        <span>Pipeline</span>
        <span>Reports</span>
    </div>
    <div class="topbar-badge">Multi-Agent AI</div>
</div>
""", unsafe_allow_html=True)


# ── Session state init ────────────────────────────────────────────────────────
for key in ("results", "running", "done"):
    if key not in st.session_state:
        st.session_state[key] = {} if key == "results" else False


# ── Page wrap open ────────────────────────────────────────────────────────────
st.markdown('<div class="page-wrap">', unsafe_allow_html=True)


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-left">
        <div class="hero-kicker">Research Intelligence Platform</div>
        <h1>Deep research,<br><em>automated.</em></h1>
    </div>
    <div class="hero-right">
        <p class="hero-desc">
            Four specialized agents work in sequence — searching the web, scraping
            sources, drafting a structured report, and stress-testing it with
            AI-powered critique — so you don't have to.
        </p>
        <div class="hero-stat-row">
            <div class="hero-stat">
                <div class="hero-stat-num">4</div>
                <div class="hero-stat-label">AI Agents</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-num">1</div>
                <div class="hero-stat-label">Final Report</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-num">∞</div>
                <div class="hero-stat-label">Topics</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── Body: two-column ─────────────────────────────────────────────────────────
st.markdown('<div class="body-grid">', unsafe_allow_html=True)

# Left column (input + results)
col_main, col_side = st.columns([3, 1.1])

with col_main:
    st.markdown('<div class="input-section-label">Query</div>', unsafe_allow_html=True)

    topic = st.text_input(
        "topic",
        placeholder="e.g. Quantum computing breakthroughs in 2025",
        key="topic_input",
        label_visibility="hidden",
    )

    run_btn = st.button("Run Research Pipeline →", use_container_width=True)

    st.markdown("""
    <div class="chip-row">
        <span style="font-family:'Geist Mono',monospace;font-size:0.6rem;color:#c4c4c4;letter-spacing:0.1em;text-transform:uppercase;line-height:1.8;">Try →</span>
        <span class="chip">LLM agents 2025</span>
        <span class="chip">CRISPR gene editing</span>
        <span class="chip">Fusion energy progress</span>
        <span class="chip">Neuromorphic computing</span>
    </div>
    """, unsafe_allow_html=True)


# Right column (pipeline)
with col_side:
    r = st.session_state.results
    done_flag = st.session_state.done

    def step_state(step):
        steps = ["search", "reader", "writer", "critic"]
        if step in r:
            return "done"
        if st.session_state.running:
            for k in steps:
                if k not in r:
                    return "running" if k == step else "waiting"
        return "waiting"

    icons = {
        "search": "◎",
        "reader": "◈",
        "writer": "◇",
        "critic": "◉",
    }
    titles = {
        "search": "Search Agent",
        "reader": "Reader Agent",
        "writer": "Writer Chain",
        "critic": "Critic Chain",
    }
    descs = {
        "search": "Live web search",
        "reader": "Content extraction",
        "writer": "Report synthesis",
        "critic": "Quality review",
    }
    badge_map = {
        "waiting": ("Waiting", "badge-wait"),
        "running": ("Running", "badge-run"),
        "done":    ("Done",    "badge-done"),
    }

    st.markdown('<div class="pipeline-header">Pipeline</div>', unsafe_allow_html=True)

    for step in ["search", "reader", "writer", "critic"]:
        ss = step_state(step)
        card_cls = "active" if ss == "running" else ("done" if ss == "done" else "")
        badge_text, badge_cls = badge_map[ss]
        st.markdown(f"""
        <div class="pipeline-step {card_cls}">
            <div class="step-icon-wrap">{icons[step]}</div>
            <div class="step-body">
                <div class="step-name">{titles[step]}</div>
                <div class="step-desc">{descs[step]}</div>
            </div>
            <span class="step-badge {badge_cls}">{badge_text}</span>
        </div>
        """, unsafe_allow_html=True)


st.markdown('</div>', unsafe_allow_html=True)  # close body-grid


# ── Run logic ─────────────────────────────────────────────────────────────────
if run_btn:
    if not topic.strip():
        st.warning("Please enter a research topic to continue.")
    else:
        st.session_state.results = {}
        st.session_state.running = True
        st.session_state.done = False
        st.rerun()

if st.session_state.running and not st.session_state.done:
    results = {}
    topic_val = st.session_state.topic_input

    with st.spinner("Search Agent — scanning the web…"):
        search_agent = build_search_agent()
        sr = search_agent.invoke({
            "messages": [("user", f"Find recent, reliable and detailed information about: {topic_val}")]
        })
        results["search"] = sr["messages"][-1].content
        st.session_state.results = dict(results)

    with st.spinner("Reader Agent — extracting deep content…"):
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

    with st.spinner("Writer — drafting the research report…"):
        research_combined = (
            f"SEARCH RESULTS:\n{results['search']}\n\n"
            f"DETAILED SCRAPED CONTENT:\n{results['reader']}"
        )
        results["writer"] = writer_chain.invoke({
            "topic": topic_val,
            "research": research_combined
        })
        st.session_state.results = dict(results)

    with st.spinner("Critic — reviewing and scoring the report…"):
        results["critic"] = critic_chain.invoke({
            "report": results["writer"]
        })
        st.session_state.results = dict(results)

    st.session_state.running = False
    st.session_state.done = True
    st.rerun()


# ── Results display ───────────────────────────────────────────────────────────
r = st.session_state.results

if r:
    st.markdown('<div class="results-section">', unsafe_allow_html=True)
    st.markdown('<div class="results-label">Output</div>', unsafe_allow_html=True)

    if "search" in r:
        with st.expander("◎  Search Agent — raw output", expanded=False):
            st.markdown(f'<div class="raw-output">{r["search"]}</div>', unsafe_allow_html=True)

    if "reader" in r:
        with st.expander("◈  Reader Agent — scraped content", expanded=False):
            st.markdown(f'<div class="raw-output">{r["reader"]}</div>', unsafe_allow_html=True)

    if "writer" in r:
        st.markdown(f"""
        <div class="report-wrap">
            <div class="report-meta">
                <span class="report-tag">Research Report</span>
                <span class="report-tag" style="color:#6b7280;background:rgba(0,0,0,0.03);border-color:rgba(0,0,0,0.08);">
                    {st.session_state.topic_input[:40] + ("…" if len(st.session_state.topic_input) > 40 else "")}
                </span>
                <span class="report-ts">{time.strftime("%d %b %Y · %H:%M")}</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown(r["writer"])
        st.markdown("</div>", unsafe_allow_html=True)

        st.download_button(
            label="↓  Download as Markdown",
            data=r["writer"],
            file_name=f"intellexa_report_{int(time.time())}.md",
            mime="text/markdown",
        )

    if "critic" in r:
        st.markdown('<div class="critic-wrap">', unsafe_allow_html=True)
        st.markdown('<div class="critic-label">◉ Critic Review</div>', unsafe_allow_html=True)
        st.markdown(r["critic"])
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="site-footer">
    Intellexa AI · LangChain Multi-Agent Pipeline · Built by Dhiraj Rupnawar
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # close page-wrap