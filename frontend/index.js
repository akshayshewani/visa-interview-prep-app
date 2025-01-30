import React, { useState } from "react";
import ReactDOM from "react-dom";
import UploadDocs from "./components/UploadDocs";
import Interviewer from "./components/Interviewer";

const App = () => {
  const [interviewText, setInterviewText] = useState("");

  return (
    <div>
      <h1>Visa Interview Prep App</h1>
      <UploadDocs setInterviewText={setInterviewText} />
      {interviewText && <Interviewer interviewText={interviewText} />}
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById("root"));