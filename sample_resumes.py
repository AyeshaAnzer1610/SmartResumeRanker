"""
Sample resumes for testing the Smart Resume Ranker application.
These can be used to demonstrate the difference between TF-IDF and BERT matching.
"""

# Sample Job Description for Machine Learning Engineer
SAMPLE_JD = """
Machine Learning Engineer

We are seeking a talented Machine Learning Engineer to join our AI team. 
The ideal candidate will have:

Requirements:
- Strong experience with Python, TensorFlow, and PyTorch
- Deep understanding of machine learning algorithms and neural networks
- Experience with data preprocessing, feature engineering, and model evaluation
- Knowledge of cloud platforms (AWS, Azure, or GCP)
- Experience with MLOps and model deployment
- Strong background in statistics and mathematics
- Experience with big data technologies (Spark, Hadoop)
- Excellent problem-solving skills and analytical thinking

Responsibilities:
- Develop and deploy machine learning models
- Optimize model performance and scalability
- Collaborate with data scientists and software engineers
- Implement automated ML pipelines
- Conduct A/B testing and model validation
- Stay updated with latest ML research and technologies

Nice to have:
- Experience with natural language processing (NLP)
- Knowledge of computer vision
- Experience with reinforcement learning
- Publications in ML conferences or journals
"""

# Strong Match Resume (should score high with BERT)
STRONG_MATCH_RESUME = """
JOHN DOE
Machine Learning Engineer
john.doe@email.com | (555) 123-4567 | linkedin.com/in/johndoe

PROFESSIONAL SUMMARY
Experienced Machine Learning Engineer with 5+ years developing and deploying AI solutions. 
Expert in Python, deep learning frameworks, and cloud platforms. Passionate about 
building scalable ML systems and staying current with cutting-edge research.

TECHNICAL SKILLS
Programming: Python, R, Java, SQL
ML/DL Frameworks: TensorFlow, PyTorch, Scikit-learn, Keras
Cloud Platforms: AWS (SageMaker, EC2, S3), Google Cloud Platform
Big Data: Apache Spark, Hadoop, Kafka
MLOps: Docker, Kubernetes, MLflow, Kubeflow
Databases: PostgreSQL, MongoDB, Redis

PROFESSIONAL EXPERIENCE

Senior ML Engineer | TechCorp Inc. | 2021-Present
• Developed and deployed production ML models achieving 95% accuracy
• Built automated ML pipelines reducing deployment time by 60%
• Implemented A/B testing framework for model optimization
• Led team of 3 junior ML engineers on computer vision projects
• Technologies: Python, TensorFlow, AWS, Docker, Kubernetes

Machine Learning Engineer | AI Startup | 2019-2021
• Built recommendation systems using collaborative filtering
• Developed NLP models for sentiment analysis and text classification
• Optimized model performance reducing inference time by 40%
• Implemented feature engineering pipelines for real-time data
• Technologies: PyTorch, Scikit-learn, Apache Spark, GCP

Data Scientist | Analytics Corp | 2017-2019
• Developed predictive models for customer churn analysis
• Created automated reporting dashboards using Tableau
• Conducted statistical analysis and hypothesis testing
• Built ETL pipelines for data preprocessing
• Technologies: Python, R, SQL, Tableau, AWS

EDUCATION
Master of Science in Computer Science | Stanford University | 2017
Bachelor of Science in Mathematics | UC Berkeley | 2015

CERTIFICATIONS
• AWS Certified Machine Learning - Specialty
• Google Cloud Professional ML Engineer
• TensorFlow Developer Certificate

PROJECTS
• Built a real-time fraud detection system using deep learning
• Developed a computer vision model for quality control in manufacturing
• Created an NLP-based chatbot for customer service automation
• Implemented reinforcement learning for dynamic pricing optimization

PUBLICATIONS
• "Efficient Neural Architecture Search for Computer Vision" - ICML 2022
• "Scalable ML Pipeline Architecture" - KDD 2021
"""

# Weak Match Resume (should score low with BERT)
WEAK_MATCH_RESUME = """
JANE SMITH
Marketing Specialist
jane.smith@email.com | (555) 987-6543 | linkedin.com/in/janesmith

PROFESSIONAL SUMMARY
Creative marketing professional with 4 years experience in digital marketing, 
brand management, and customer engagement. Skilled in social media marketing, 
content creation, and campaign analysis.

TECHNICAL SKILLS
Marketing Tools: Google Analytics, Facebook Ads, MailChimp, HubSpot
Design Software: Adobe Creative Suite, Canva, Figma
Social Media: Instagram, Facebook, Twitter, LinkedIn, TikTok
Analytics: Google Analytics, Facebook Insights, Twitter Analytics
CRM: Salesforce, HubSpot, Zoho

PROFESSIONAL EXPERIENCE

Senior Marketing Specialist | BrandCorp | 2021-Present
• Managed social media campaigns reaching 2M+ followers
• Increased brand engagement by 150% through targeted content
• Developed email marketing campaigns with 25% open rate
• Analyzed campaign performance using Google Analytics
• Led team of 2 junior marketers on seasonal campaigns

Marketing Coordinator | Retail Chain | 2019-2021
• Created content for social media platforms
• Managed influencer partnerships and collaborations
• Organized promotional events and product launches
• Tracked KPIs and prepared monthly reports
• Coordinated with graphic designers and copywriters

Marketing Intern | Startup Inc | 2018-2019
• Assisted with social media content creation
• Conducted market research and competitor analysis
• Helped organize trade shows and events
• Created weekly newsletters and blog posts
• Supported email marketing campaigns

EDUCATION
Bachelor of Arts in Marketing | University of Marketing | 2018
Minor in Communications

CERTIFICATIONS
• Google Analytics Individual Qualification
• HubSpot Inbound Marketing Certification
• Facebook Blueprint Certification

PROJECTS
• Launched successful influencer marketing campaign increasing sales by 200%
• Redesigned company website improving conversion rate by 35%
• Created viral social media campaign with 5M+ impressions
• Developed customer loyalty program increasing retention by 40%

ACHIEVEMENTS
• Marketing Excellence Award 2022
• Best Social Media Campaign 2021
• Employee of the Month (3 times)
"""

# Medium Match Resume (should score medium with BERT)
MEDIUM_MATCH_RESUME = """
MIKE JOHNSON
Software Developer
mike.johnson@email.com | (555) 456-7890 | linkedin.com/in/mikejohnson

PROFESSIONAL SUMMARY
Full-stack software developer with 3 years experience building web applications 
and APIs. Proficient in multiple programming languages and frameworks. 
Interested in learning machine learning and AI technologies.

TECHNICAL SKILLS
Programming: JavaScript, Python, Java, C#, SQL
Frameworks: React, Node.js, Django, Spring Boot
Databases: MySQL, PostgreSQL, MongoDB
Cloud: AWS (EC2, S3, Lambda), Azure
Tools: Git, Docker, Jenkins, Jira

PROFESSIONAL EXPERIENCE

Full-Stack Developer | WebTech Inc | 2021-Present
• Developed RESTful APIs using Node.js and Express
• Built responsive web applications with React
• Implemented database design and optimization
• Deployed applications using Docker and AWS
• Collaborated with UX/UI designers on frontend development

Software Developer | StartupXYZ | 2019-2021
• Created web applications using Python and Django
• Integrated third-party APIs and payment systems
• Implemented user authentication and authorization
• Optimized database queries and application performance
• Participated in code reviews and agile development

Junior Developer | Tech Solutions | 2018-2019
• Assisted in developing web applications
• Fixed bugs and implemented new features
• Wrote unit tests and documentation
• Learned new technologies and frameworks
• Supported senior developers in project delivery

EDUCATION
Bachelor of Science in Computer Science | State University | 2018

CERTIFICATIONS
• AWS Certified Developer - Associate
• Microsoft Certified: Azure Developer Associate

PROJECTS
• Built an e-commerce platform with payment integration
• Developed a task management application with real-time updates
• Created a weather app using external APIs
• Built a portfolio website with responsive design

INTERESTS
• Learning machine learning and AI
• Contributing to open-source projects
• Attending tech meetups and conferences
• Reading about emerging technologies
"""

if __name__ == "__main__":
    print("Sample resumes created for testing Smart Resume Ranker")
    print("\nFiles to create:")
    print("1. sample_jd.txt - Job Description")
    print("2. strong_match_resume.txt - Strong ML Engineer candidate")
    print("3. weak_match_resume.txt - Marketing Specialist")
    print("4. medium_match_resume.txt - Software Developer")
    
    # Create the files
    with open("sample_jd.txt", "w") as f:
        f.write(SAMPLE_JD)
    
    with open("strong_match_resume.txt", "w") as f:
        f.write(STRONG_MATCH_RESUME)
    
    with open("weak_match_resume.txt", "w") as f:
        f.write(WEAK_MATCH_RESUME)
    
    with open("medium_match_resume.txt", "w") as f:
        f.write(MEDIUM_MATCH_RESUME)
    
    print("\nFiles created successfully!") 