# 💼 Smart Resume Ranker

A powerful AI-powered resume ranking application that uses both traditional keyword matching (TF-IDF) and advanced semantic matching (BERT) to rank resumes against job descriptions.

## 🚀 Features

### 📄 **Multi-Format Support**
- **PDF Resume Support**: Upload `.pdf` files alongside `.docx`
- **Word Document Support**: Upload `.docx` files
- **Automatic Text Extraction**: Handles complex formatting and layouts

### 🧠 **Dual Matching Algorithms**
- **BERT Semantic Matching**: Advanced AI that understands context and meaning
  - Recognizes synonyms (e.g., "ML" ≈ "Machine Learning")
  - Understands related concepts and skills
  - More accurate for complex job descriptions
- **TF-IDF Keyword Matching**: Fast exact keyword matching
  - Quick processing for specific technical terms
  - Shows exact word overlaps
  - Good baseline comparison

### 🔍 **Keyword Highlighting**
- **Visual Keyword Matching**: Shows top overlapping keywords between JD and resume
- **Highlighted Display**: Keywords are visually highlighted in results
- **Match Count**: Displays number of matched keywords per resume

### 📊 **Comprehensive Results**
- **Ranked Results**: Resumes ranked by match score
- **Score Categories**: Color-coded scores (Excellent/Good/Needs Improvement)
- **Detailed Metrics**: Word count, character count, match percentage
- **Expandable Details**: Click to see detailed analysis for each resume

### 📥 **CSV Export**
- **Download Results**: Export ranked results as CSV
- **Detailed Report**: Includes match scores, percentages, and keyword lists
- **Professional Format**: Ready for HR/recruitment use

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/SmartResumeRanker.git
   cd SmartResumeRanker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the app**
   - Open your browser and go to `http://localhost:8501`
   - The app will automatically open in your default browser

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.21.0
scikit-learn>=1.1.0
sentence-transformers>=2.2.0
python-docx>=0.8.11
docx2txt>=0.8
pdfplumber>=0.7.0
```

## 🎯 How to Use

### 1. **Enter Job Description**
- Paste the complete job description in the text area
- The more detailed the description, the better the matching

### 2. **Upload Resumes**
- Click "Browse files" to upload resume files
- Supported formats: `.pdf` and `.docx`
- You can upload multiple files at once

### 3. **Choose Matching Method**
- **BERT Semantic Matching**: For understanding meaning and context
- **TF-IDF Keyword Matching**: For exact keyword matching

### 4. **Analyze Results**
- View ranked results with match scores
- Click on each result to see detailed analysis
- Download results as CSV for further use

## 🧪 Testing with Sample Data

The project includes sample data for testing:

- `sample_jd.txt`: Machine Learning Engineer job description
- `strong_match_resume.txt`: Strong ML Engineer candidate
- `weak_match_resume.txt`: Marketing Specialist (weak match)
- `medium_match_resume.txt`: Software Developer (medium match)

To test:
1. Copy the content from `sample_jd.txt` into the job description field
2. Upload the resume files
3. Compare results between TF-IDF and BERT methods

## 🔬 Technical Details

### **BERT Semantic Matching**
- Uses `all-MiniLM-L6-v2` model (fast and efficient)
- Converts text to high-dimensional embeddings
- Calculates cosine similarity between job description and resumes
- Understands semantic relationships and synonyms

### **TF-IDF Keyword Matching**
- Extracts and weights important terms
- Uses cosine similarity for ranking
- Fast processing for large datasets
- Good for exact technical term matching

### **Text Processing**
- Automatic text extraction from PDF and DOCX files
- Text cleaning and preprocessing
- Stop word removal
- Case-insensitive matching

## 📈 Performance Comparison

| Method | Speed | Accuracy | Use Case |
|--------|-------|----------|----------|
| **BERT** | Slower | Higher | Complex job descriptions, semantic understanding |
| **TF-IDF** | Faster | Lower | Quick screening, exact keyword matching |

## 🎨 Features in Detail

### **Smart UI/UX**
- **Responsive Design**: Works on desktop and mobile
- **Real-time Processing**: Live updates with progress indicators
- **Error Handling**: Graceful handling of file processing errors
- **Professional Styling**: Clean, modern interface

### **Advanced Analytics**
- **Score Visualization**: Color-coded match scores
- **Keyword Analysis**: Detailed keyword matching breakdown
- **Statistics Dashboard**: Summary metrics and trends
- **Export Functionality**: Professional CSV reports

## 🚀 Deployment

### **Local Development**
```bash
streamlit run app.py
```

### **Cloud Deployment**
The app can be deployed on:
- **Streamlit Cloud**: Free hosting for Streamlit apps
- **Heroku**: With proper configuration
- **AWS/GCP**: Using containerization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit**: For the amazing web app framework
- **Hugging Face**: For the sentence-transformers library
- **scikit-learn**: For the TF-IDF implementation
- **pdfplumber**: For PDF text extraction

## 📞 Contact

- **GitHub**: [@yourusername](https://github.com/yourusername)
- **LinkedIn**: [Your Name](https://linkedin.com/in/yourprofile)
- **Email**: your.email@example.com

---

⭐ **Star this repository if you find it helpful!**

🔗 **Share with your network to help others discover this tool!**
