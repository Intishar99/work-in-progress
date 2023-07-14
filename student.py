import streamlit as st

def main():
    st.title("Student Dashboard")

    # Student information
    st.subheader("Student Details")
    student_name = st.text_input("Name")
    student_picture = st.image("placeholder_image.jpg", caption="Student Picture")

    # Subject marks
    st.subheader("Subject Marks")
    subjects = ["Math", "Science", "English"]
    marks = []
    for subject in subjects:
        mark = st.number_input(subject, min_value=0, max_value=100, value=0)
        marks.append(mark)

    # Revise button
    st.subheader("Revise")
    if st.button("Revise"):
        st.success("Click the link below to watch a revision video:")
        st.markdown("[Revision Video](https://www.example.com/revision)")

if __name__ == "__main__":
    main()
