import streamlit as st
import pandas as pd

# ---------------- PAGE SETTINGS ---------------- #

st.set_page_config(
    page_title="Student Performance Tracker",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM STYLE ---------------- #

st.markdown("""
<style>

.main{
    background-color:#F4F6F8;
}

h1{
    color:#0E4C92;
    text-align:center;
}

.stButton>button{
    width:100%;
    background-color:#0E4C92;
    color:white;
    border-radius:8px;
    height:45px;
    font-size:17px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.title("🎓 Student Performance Tracker")
st.write("### Python Internship Project")

st.markdown("---")

# ---------------- SESSION ---------------- #

if "students" not in st.session_state:
    st.session_state.students=[]

# ---------------- FORM ---------------- #

st.subheader("➕ Add Student Details")

col1,col2=st.columns(2)

with col1:

    sid=st.text_input("Student ID")

    name=st.text_input("Student Name")

    dept=st.selectbox(
        "Department",
        [
            "CSE",
            "IT",
            "ECE",
            "EEE",
            "MECH"
        ]
    )

with col2:

    python=st.number_input(
        "Python",
        0,
        100
    )

    java=st.number_input(
        "Java",
        0,
        100
    )

    dbms=st.number_input(
        "DBMS",
        0,
        100
    )

add=st.button("Add Student")
# ---------------- ADD STUDENT ---------------- #

if add:

    total = python + java + dbms
    average = round(total / 3, 2)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "Fail"

    student = {
        "ID": sid,
        "Name": name,
        "Department": dept,
        "Python": python,
        "Java": java,
        "DBMS": dbms,
        "Total": total,
        "Average": average,
        "Grade": grade
    }

    st.session_state.students.append(student)

    st.success("✅ Student Added Successfully!")

st.markdown("---")

# ---------------- DASHBOARD ---------------- #

st.subheader("📊 Dashboard")

if len(st.session_state.students) > 0:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Students",
            len(st.session_state.students)
        )

    with col2:

        highest = max(
            st.session_state.students,
            key=lambda x: x["Average"]
        )

        st.metric(
            "Top Student",
            highest["Name"]
        )

    with col3:

        avg = round(
            sum(i["Average"] for i in st.session_state.students)
            / len(st.session_state.students),
            2
        )

        st.metric(
            "Class Average",
            avg
        )

st.markdown("---")

# ---------------- STUDENT TABLE ---------------- #

st.subheader("📋 Student Records")

if len(st.session_state.students) > 0:

    df = pd.DataFrame(st.session_state.students)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No Student Records Available.")
    st.markdown("---")

# ---------------- SEARCH STUDENT ---------------- #

st.subheader("🔍 Search Student")

search_id = st.text_input("Enter Student ID")

if st.button("Search"):

    found = False

    for student in st.session_state.students:

        if student["ID"] == search_id:

            st.success("Student Found")

            st.write("### Student Details")

            st.write("**Student ID :**", student["ID"])
            st.write("**Name :**", student["Name"])
            st.write("**Department :**", student["Department"])
            st.write("**Python :**", student["Python"])
            st.write("**Java :**", student["Java"])
            st.write("**DBMS :**", student["DBMS"])
            st.write("**Total :**", student["Total"])
            st.write("**Average :**", student["Average"])
            st.write("**Grade :**", student["Grade"])

            found = True

            break

    if not found:
        st.error("Student Not Found")

st.markdown("---")

# ---------------- DELETE STUDENT ---------------- #

st.subheader("🗑 Delete Student")

delete_id = st.text_input("Enter Student ID to Delete")

if st.button("Delete Student"):

    deleted = False

    for student in st.session_state.students:

        if student["ID"] == delete_id:

            st.session_state.students.remove(student)

            st.success("Student Deleted Successfully")

            deleted = True

            break

    if not deleted:
        st.error("Student ID Not Found")

st.markdown("---")

# ---------------- DOWNLOAD ---------------- #

if len(st.session_state.students) > 0:

    df = pd.DataFrame(st.session_state.students)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Student Report",
        csv,
        "Student_Report.csv",
        "text/csv"
    )

st.markdown("---")

st.caption("Developed using Python & Streamlit")
