import streamlit as st

def main():
    st.title("Student Dashboard")
    
    # Student's name
    st.header("Student Name: Student")
    
    # Student picture
    student_picture = st.image("placeholder_image.jpg", caption="Student Picture")
    
    # List of subjects and marks
    subjects = ['Math', 'Science', 'English']
    marks = []
    for subject in subjects:
        mark = st.number_input(f"Enter mark for {subject}", min_value=0, max_value=100, value=0)
        marks.append(mark)
    
    # Revise button
    if st.button("Revise"):
        st.write("Click on the link below to watch the revision video.")
        st.markdown("[Revision Video](https://www.example.com)")
        
if __name__ == "__main__":
    main()
