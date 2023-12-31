import { useState } from "react";

function App() {
  const [username, setUsername] = useState("");
  const [analytics, setAnalytics] = useState();
  const [error, setError] = useState("");

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setAnalytics({});
    try {
      const apiData = await fetchAnalytics(username);
      if (apiData) {
        setAnalytics(apiData);
        setError("");
      } else {
        console.error("Error fetching data from Analyzer");
      }
    } catch (error) {
      console.error("Error fetching data:", error);
      setError("Invalid Username");
    }
  };

  const fetchAnalytics = async (username) => {
    const url = `http://localhost:5001/fetchcodewars?username=${username}`;
    const resp = await fetch(url);
    if (resp.ok) {
      return resp.json();
    } else {
      throw new Error(`Error: ${resp.status}`);
    }
  };

  return (
    <div className="container">
      <form onSubmit={handleSubmit}>
        <label>Enter Codewars Username: </label>
        <input type="text" onChange={updateUsername} />
        <button type="submit">Submit</button>
      </form>

      <div>
        {error ? (
          <p className="error">{error}</p>
        ) : null}
      </div>

      <div>
        {analytics?.language_scores ? (
          <>
            <h1>Hi {analytics.name} : {analytics.leaderboardPosition}</h1>
            <ul>
              {Object.entries(analytics.language_scores).map(([lang, score], index) => (
                <li key={index}>
                  <strong>Language:</strong> {lang}, <strong>Score:</strong> {score}
                </li>
              ))}
            </ul>
            <p>Your strongest language is: {analytics.topLanguage}</p>
          </>
        ) : null}
      </div>
    </div>
  );
}

export default App;
