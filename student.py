import streamlit as st

def main():
    st.title("Student Dashboard")
    
    # Student's name
    st.header("Student Name: Student")
    
    # Student picture
    student_picture = st.image("placeholder_image.jpg", caption="Student Picture")
    
    # List of subjects and marks
    subjects = ['Math', 'Science', 'English']
    marks = [55, 85, 48]  # Hardcoded marks
    
    # Display subject marks
    st.subheader("Subject Marks")
    for i, subject in enumerate(subjects):
        st.write(f"{subject}: {marks[i]}")
    
    # Revise button
    if st.button("Revise"):
        st.write("Click on the link below to watch the revision video.")
        st.markdown("[Revision Video](https://www.example.com)")
        
if __name__ == "__main__":
    main()
