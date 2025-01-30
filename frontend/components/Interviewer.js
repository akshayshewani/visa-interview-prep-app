import React, { useState } from "react";
import axios from "axios";

const Interviewer = ({ interviewText }) => {
  const [questions, setQuestions] = useState("");

  const startInterview = async () => {
    const response = await axios.post("http://localhost:8000/interview/", new URLSearchParams({ text: interviewText }));
    setQuestions(response.data.questions);
  };

  return (
    <div>
      <button onClick={startInterview}>Start Interview</button>
      <p>{questions}</p>
    </div>
  );
};

export default Interviewer;
