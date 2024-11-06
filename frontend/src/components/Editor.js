import React, { useState } from 'react';

function Editor() {
  const [content, setContent] = useState("");
  const [suggestions, setSuggestions] = useState("");

  const fetchSuggestions = () => {
    fetch("http://localhost:8000/api/recommendations/content", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content })
    })
    .then(response => response.json())
    .then(data => setSuggestions(data.suggestions))
    .catch(error => console.error("Error:", error));
  };

  return (
    <div>
      <h2>Content Editor</h2>
      <textarea value={content} onChange={(e) => setContent(e.target.value)} />
      <button onClick={fetchSuggestions}>Get Suggestions</button>
      <p>Suggestions: {suggestions}</p>
    </div>
  );
}

export default Editor;
