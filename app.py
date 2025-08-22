import streamlit as st
from PyPDF2 import PdfMerger
from io import BytesIO

st.title("PDF Merger App")
st.subheader("Upload PDF files and merge them into one")

uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)



if st.button("Merge PDFs"):
    if len(uploaded_files) > 1:
        merger = PdfMerger()
        for pdf_file in uploaded_files:
            merger.append(pdf_file) # Appends the file-like object directly

        # Create a BytesIO object to store the merged PDF
        merged_pdf_buffer = BytesIO()
        merger.write(merged_pdf_buffer)
        merger.close()

        # Ensure the buffer pointer is at the beginning for downloading
        merged_pdf_buffer.seek(0)

        st.success("PDF files merged successfully!")
        st.download_button(
            label="Download Merged PDF",
            data=merged_pdf_buffer,
            file_name="merged.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("Please upload at least two PDF files to merge.")
