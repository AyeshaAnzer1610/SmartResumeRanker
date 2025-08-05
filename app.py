import os
import re
import docx2txt
import pdfplumber
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

# Load BERT model (small and fast for demo)
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# ----------- Text Extraction -----------
def extract_docx_text(file):
    try:
    return docx2txt.process(file)
    except Exception as e:
        st.error(f"Error processing {file.name}: {str(e)}")
        return ""

def extract_pdf_text(file):
    try:
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text
    except Exception as e:
        st.error(f"Error processing {file.name}: {str(e)}")
        return ""

def load_resume_texts(uploaded_files):
    resumes = {}
    for file in uploaded_files:
        if file.name.endswith(".docx"):
            text = extract_docx_text(file)
            if text:
                resumes[file.name] = text
        elif file.name.endswith(".pdf"):
            text = extract_pdf_text(file)
            if text:
                resumes[file.name] = text
    return resumes

# ----------- Preprocess Text -----------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)
    return text

# ----------- Keyword Highlighting -----------
def highlight_keywords(jd_text, resume_text):
    jd_words = set(clean_text(jd_text).split())
    resume_words = set(clean_text(resume_text).split())
    return jd_words.intersection(resume_words)

def get_important_keywords(text, top_n=10):
    """Extract most important keywords from text"""
    words = clean_text(text).split()
    word_freq = {}
    for word in words:
        if len(word) > 2:  # Skip short words
            word_freq[word] = word_freq.get(word, 0) + 1
    return sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:top_n]

# ----------- TF-IDF Ranking -----------
def rank_resumes_tfidf(jd_text, resumes):
    docs = [jd_text] + list(resumes.values())
    docs = [clean_text(doc) for doc in docs]
    tfidf = TfidfVectorizer(stop_words='english', max_features=1000)
    tfidf_matrix = tfidf.fit_transform(docs)
    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    ranked = sorted(zip(resumes.keys(), scores), key=lambda x: x[1], reverse=True)
    return ranked

# ----------- BERT Semantic Ranking -----------
def rank_resumes_bert(jd_text, resumes):
    try:
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)
    resume_embeddings = model.encode(list(resumes.values()), convert_to_tensor=True)
    scores = util.cos_sim(jd_embedding, resume_embeddings)[0]
    ranked = sorted(zip(resumes.keys(), scores.tolist()), key=lambda x: x[1], reverse=True)
    return ranked
    except Exception as e:
        st.error(f"Error in BERT processing: {str(e)}")
        return []

# ----------- Streamlit App -----------
st.set_page_config(
    page_title="Smart Resume Ranker",
    page_icon="��",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Custom CSS
st.markdown("""
<style>
    /* Main Header */
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    
    /* Cards */
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .result-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
        transition: transform 0.2s ease;
    }
    
    .result-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    /* Keyword Highlighting */
    .keyword-highlight {
        background: linear-gradient(45deg, #ffd700, #ffed4e);
        padding: 0.3rem 0.6rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
        margin: 0.2rem;
        display: inline-block;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Score Indicators */
    .score-excellent {
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: 600;
        display: inline-block;
    }
    
    .score-good {
        background: linear-gradient(45deg, #FF9800, #f57c00);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: 600;
        display: inline-block;
    }
    
    .score-poor {
        background: linear-gradient(45deg, #f44336, #d32f2f);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: 600;
        display: inline-block;
    }
    
    /* Sidebar Styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1rem;
        border-radius: 10px;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
    
    /* File Upload */
    .uploadedFile {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border: 2px dashed #2196F3;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Text Areas */
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        transition: border-color 0.3s ease;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 10px;
        font-weight: 600;
    }
    
    /* Metrics */
    .metric-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 15px;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Main Header
st.markdown("""
<div class="main-header">
    <h1>💼 Smart Resume Ranker</h1>
    <p>AI-Powered Resume Analysis with BERT Semantic Matching & TF-IDF Keyword Analysis</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for settings
with st.sidebar:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1rem; border-radius: 10px; color: white; margin-bottom: 1rem;">
        <h3 style="margin: 0; text-align: center;">⚙️ Settings</h3>
    </div>
    """, unsafe_allow_html=True)
    
    method = st.radio(
        "Select Matching Method:",
        ["BERT Semantic Matching", "TF-IDF (Keyword-Based)"],
        help="BERT: Understands meaning and synonyms. TF-IDF: Exact keyword matching."
    )
    
    st.markdown("---")
    
    # Method Information
    if method == "BERT Semantic Matching":
        st.markdown("""
        <div style="background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%); padding: 1rem; border-radius: 10px; border-left: 4px solid #4CAF50;">
            <h4 style="margin: 0 0 0.5rem 0; color: #2e7d32;">🤖 BERT Semantic Matching</h4>
            <ul style="margin: 0; padding-left: 1.2rem; color: #2e7d32;">
                <li>Understands context and meaning</li>
                <li>Recognizes synonyms (e.g., "ML" ≈ "Machine Learning")</li>
                <li>More accurate for complex job descriptions</li>
                <li>Slower but smarter</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 1rem; border-radius: 10px; border-left: 4px solid #FF9800;">
            <h4 style="margin: 0 0 0.5rem 0; color: #e65100;">🔍 TF-IDF Keyword Matching</h4>
            <ul style="margin: 0; padding-left: 1.2rem; color: #e65100;">
                <li>Fast exact keyword matching</li>
                <li>Good for specific technical terms</li>
                <li>Shows exact word overlaps</li>
                <li>Quick processing</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
        <h3 style="margin: 0 0 1rem 0; color: #1976d2;">📝 Job Description</h3>
    </div>
    """, unsafe_allow_html=True)
    
    jd_input = st.text_area(
        "Enter the job description here...",
        height=300,
        placeholder="Paste the complete job description here. The more detailed, the better the matching will be. Include requirements, responsibilities, and preferred qualifications."
    )

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
        <h3 style="margin: 0 0 1rem 0; color: #7b1fa2;">📄 Upload Resumes</h3>
    </div>
    """, unsafe_allow_html=True)
    
uploaded_files = st.file_uploader(
        "Upload resume files",
    type=["docx", "pdf"],
        accept_multiple_files=True,
        help="Supported formats: .docx and .pdf files. You can upload multiple files at once."
    )
    
    if uploaded_files:
        st.success(f"✅ Successfully uploaded {len(uploaded_files)} file(s)")
        for i, file in enumerate(uploaded_files, 1):
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%); padding: 0.8rem; border-radius: 8px; margin: 0.3rem 0;">
                <span style="font-weight: 600; color: #2e7d32;">📎 {file.name}</span>
            </div>
            """, unsafe_allow_html=True)

# Processing and Results
if jd_input and uploaded_files:
    st.markdown("---")
    st.markdown("""
    <div style="background: linear-gradient(135deg, #fff8e1 0%, #ffecb3 100%); padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem;">
        <h2 style="margin: 0; color: #f57c00; text-align: center;">🎯 Analysis Results</h2>
    </div>
    """, unsafe_allow_html=True)
    
    with st.spinner("🔄 Analyzing resumes with AI..."):
        resumes = load_resume_texts(uploaded_files)

        if not resumes:
            st.error("❌ No valid resume files could be processed. Please check your file formats.")
        else:
            # Rank resumes
            if method == "BERT Semantic Matching":
            results = rank_resumes_bert(jd_input, resumes)
            else:
                results = rank_resumes_tfidf(jd_input, resumes)

            if results:
                st.success(f"✅ Analysis complete! Ranked {len(results)} resume(s)")

                # Display results
        for i, (filename, score) in enumerate(results):
                    # Determine score category
                    if score > 0.7:
                        score_class = "score-excellent"
                        score_text = "Excellent Match"
                    elif score > 0.5:
                        score_class = "score-good"
                        score_text = "Good Match"
                    else:
                        score_class = "score-poor"
                        score_text = "Needs Improvement"
                    
                    with st.expander(f"🏆 #{i+1}: {filename}", expanded=(i==0)):
                        col1, col2 = st.columns([2, 1])
                        
                        with col1:
                            st.markdown(f"""
                            <div class="result-card">
                                <h4 style="margin: 0 0 1rem 0; color: #333;">📊 Match Analysis</h4>
                                <div class="{score_class}">
                                    {score_text}: {score:.3f}
                                </div>
                                <p style="margin: 1rem 0 0 0; font-size: 0.9rem; color: #666;">
                                    Match Percentage: <strong>{score*100:.1f}%</strong>
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Keyword analysis
            matched_keywords = highlight_keywords(jd_input, resumes[filename])
            if matched_keywords:
                                st.markdown("**🔑 Matched Keywords:**")
                                keyword_display = " ".join([f'<span class="keyword-highlight">{kw}</span>' for kw in list(matched_keywords)[:20]])
                                st.markdown(f'<div style="margin: 1rem 0;">{keyword_display}</div>', unsafe_allow_html=True)
            else:
                                st.warning("⚠️ No keyword matches found")
                        
                        with col2:
                            # Show resume stats
                            resume_text = resumes[filename]
                            word_count = len(resume_text.split())
                            char_count = len(resume_text)
                            
                            st.markdown("""
                            <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 1rem; border-radius: 10px;">
                                <h5 style="margin: 0 0 1rem 0; color: #333;">📈 Resume Statistics</h5>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            col_a, col_b = st.columns(2)
                            with col_a:
                                st.metric("Words", f"{word_count:,}")
                                st.metric("Characters", f"{char_count:,}")
                            with col_b:
                                st.metric("Match %", f"{score*100:.1f}%")
                                st.metric("Keywords", len(matched_keywords))
        
        # CSV Export
                st.markdown("---")
                st.markdown("""
                <div style="background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%); padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem;">
                    <h3 style="margin: 0; color: #2e7d32; text-align: center;">📊 Export Results</h3>
                </div>
                """, unsafe_allow_html=True)
                
                # Create detailed DataFrame
                export_data = []
                for filename, score in results:
                    matched_keywords = highlight_keywords(jd_input, resumes[filename])
                    keyword_count = len(matched_keywords)
                    export_data.append({
                        "Resume": filename,
                        "Match Score": round(score, 3),
                        "Match Percentage": f"{score*100:.1f}%",
                        "Matched Keywords": len(matched_keywords),
                        "Keyword List": ", ".join(list(matched_keywords)[:10])
                    })
                
                df = pd.DataFrame(export_data)
                
                col1, col2 = st.columns(2)
                with col1:
        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button(
                        label="📥 Download CSV Report",
            data=csv_data,
                        file_name="resume_rankings_detailed.csv",
                        mime="text/csv",
                        help="Download detailed ranking results as CSV"
                    )
                
                with col2:
                    # Show summary statistics
                    st.markdown("""
                    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 1rem; border-radius: 10px;">
                        <h5 style="margin: 0 0 1rem 0; color: #e65100;">📈 Summary Statistics</h5>
                    </div>
                    """, unsafe_allow_html=True)
                    avg_score = df["Match Score"].mean()
                    max_score = df["Match Score"].max()
                    st.metric("Average Score", f"{avg_score:.3f}")
                    st.metric("Best Match", f"{max_score:.3f}")
            else:
                st.error("❌ Error in processing. Please try again.")

elif not jd_input and uploaded_files:
    st.info("ℹ️ Please enter a job description to start the analysis.")
elif jd_input and not uploaded_files:
    st.info("ℹ️ Please upload at least one resume file to analyze.")
else:
    st.info("ℹ️ Please provide both a job description and resume files to begin analysis.")

# Footer
st.markdown("""
<div class="footer">
    <h4 style="margin: 0 0 0.5rem 0; color: #333;">💼 Smart Resume Ranker</h4>
    <p style="margin: 0; color: #666;">Powered by BERT & TF-IDF | Built with Streamlit</p>
    <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; color: #999;">
        Advanced AI-powered resume analysis for intelligent candidate matching
    </p>
</div>
""", unsafe_allow_html=True)
