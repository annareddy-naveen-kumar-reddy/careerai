import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'careerai_production_grade_secret_key_2026')
    DATABASE_PATH = os.getenv('DATABASE_PATH', str(BASE_DIR / 'careerai.db'))
    UPLOAD_FOLDER = str(BASE_DIR / 'uploads')
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB maximum file upload
    ALLOWED_EXTENSIONS = {'pdf'}

    # AI Configuration
    AI_PROVIDER = os.getenv('AI_PROVIDER', 'demo').lower()
    AI_API_KEY = os.getenv('AI_API_KEY', '').strip()
    AI_MODEL = os.getenv('AI_MODEL', 'gemini-1.5-flash')

    # Developer Verified Details (Strictly accurate)
    DEVELOPER_NAME = "Annareddy Naveen Kumar Reddy"
    DEVELOPER_STUDENT_ID = "25301A030039"
    DEVELOPER_UNIVERSITY = "Mohan Babu University"
    DEVELOPER_BRANCH = "Electronics and Communication Engineering (ECE)"
    DEVELOPER_YEAR = "3rd Year"
    DEVELOPER_LOCATION = "Kadapa District, Kamalapuram Mandal, Thurakapalli Village, Andhra Pradesh, India"
    DEVELOPER_EMAIL = "naveenkumarreddyannareddy@gmail.com"
    DEVELOPER_PHONE = "7013998257"
    DEVELOPER_GITHUB = "https://github.com/annareddy-naveen-kumar-reddy"
    DEVELOPER_LINKEDIN = "https://www.linkedin.com/in/annareddy-naveen-kumar-reddy-037343377/"
    DEVELOPER_PORTFOLIO = "https://annareddy-naveen-kumar-reddy.github.io/portfolio/"

# Ensure uploads directory exists
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
