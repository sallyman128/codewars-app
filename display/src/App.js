import { useState } from "react";

function App() {
  const [username, setUsername] = useState("");
  const [analytics, setAnalytics] = useState();

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setAnalytics({
      data: [
        { language: "ruby", color: "red", rank: 12 },
        { language: "java", color: "green", rank: 3 },
      ],
    });
  };

  return (
    <div className="App">
      <div>
        <form onSubmit={handleSubmit}>
          <label>Enter Codewars Username: </label>
          <input type="text" onChange={updateUsername} />
          <button type="submit">Submit</button>
        </form>
      </div>

      <div>
        {analytics?.data ? (
          <ul>
            {analytics.data.map((item, index) => (
              <li key={index}>
                <strong>Language:</strong> {item.language},{" "}
                <strong>Color:</strong> {item.color}, <strong>Rank:</strong>{" "}
                {item.rank}
              </li>
            ))}
          </ul>
        ) : null}
      </div>
    </div>
  );
}

export default App;
