from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "me.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Quy Phuc (Fillips) Bui"
PAGE_ICON = ":wave:"
NAME = "Quy Phuc (Fillips) Bui"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL ="fillipsbui@gmail.com"
EMAIL_HOST ="fillips_phuc_bui@apllogistics.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/fillipsbui/",
    "GitHub": "https://github.com/spillif",
    "Tableau": "https://public.tableau.com/app/profile/fillips.bui",
}
PROJECTS = {
    "🏆 Productivity Measurement – Refine the calculation method (2022)": "https://github.com/spillif/Introduction/blob/main/certificates/Innovation.PNG",
    "🏆 Headcounts Forecasting (2021 - 2023)": "https://github.com/spillif/headcount_forecasting/tree/main",
    "🏆 CS Star Performance (2022 - 2023)": "https://github.com/spillif/star_performance",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("💼", EMAIL_HOST)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 5 years working on data-driven decision-making
- ✔️ Strong hands on experience and knowledge in Data analytics and Visualize
- ✔️ Skilled in Data analysis (Operations/ Data Specialist/ Business)
- ✔️ Deep passion for Data, Implementation (Automation), and Data Science
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Tableu
- 🗄️ Databases: MySQL, BigQuery, DataLake
- 📈 Reporting: Brio, WebFocus
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")


# --- JOB 1
st.write('\n')
st.write("🏢", "**Service Quality Analyst  | [APL Logistics Ltd. (APLL)](https://en.wikipedia.org/wiki/APL_Logistics)**")
st.write("06/2020 - Present | Remote")
st.write(
    """
- ► Aligned/ tightened the process (Automation) globally with a 10% increase in productivity
- ► Created the local dashboard (Tableau/ Power BI) for CSR to keep track of performance
- ► Reduced the unprinted invoices (revenue) below 2% to recover the AR and revenue leakage by managing the country profile
- ► Data reporting Lead of Vietnam, Cambodia, and Myanmar
- ► SEA’s lead on the global project enterprise reporting system (Data Lake)
"""
)

# --- JOB 2
st.write("🏢", "**Inventory Control Specialist  | [Nordstrom, Inc.](https://en.wikipedia.org/wiki/Nordstrom)**")
st.write("06/2019 - 03/2021")
st.write(
    """
- ► Preserved the stock's accuracy at 96% yearly and fulfilled the shipping performance
- ► Developed the stock counting application with Headquarter IT apps team in Seattle at the store level to crosscheck after products departed DC to minimize the inbound discrepancies (cost)
- ► Analyzed the sales record with product prices to eliminate revenue leakage while forecasting the high-demands seasons/ items
"""
)

# --- JOB 3
st.write('\n')
st.write("🏢", "**Data Collector & Business Analyst  | [Results Hospitality](https://www.linkedin.com/company/results-hospitality/about/)**")
st.write("01/2019 - 06/2019")
st.write(
    """
- ► Uplifted 2% in revenue (in stocks) for Shangri-La Toronto, Hilton, and Sheraton
- ► Built an inventory cycle for Toronto Pearson International Airport to keep their product turnover high
- ► Retained customer quality through Dashboard and followed up once a week
"""
)

# --- JOB 4
st.write('\n')
st.write("🏢", "**Assistant Manager   | [Fairway Market](https://www.fairwaymarkets.com/about-us)**")
st.write("01/2019 - 06/2019")
st.write(
    """
- ► Increased sales by 3% by redesigning floor and inventory layouts
- ► Maintained the daily stocks at 10% before the new stock came in
- ► Data-driven to manage the daily order (peak season) from customers
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
