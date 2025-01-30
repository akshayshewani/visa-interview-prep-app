import React, { useState } from "react";
import axios from "axios";

const UploadDocs = ({ setInterviewText }) => {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;

    let formData = new FormData();
    formData.append("file", file);

    const response = await axios.post("http://localhost:8000/upload/", formData);
    setInterviewText(response.data.content);
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default UploadDocs;
