import React, {useState} from "react"
import axios from "axios"

function handleSubmit(e) {
  e.preventDefault();
  console.log("Form submitted!");
}

function App() {
  return (
    <div className="App">
      <h1>Input Finances</h1>
      <form onSubmit={handleSubmit}>
        <input type="number" placeholder="Income"></input>
        <input type="number" placeholder="Savings"></input>
        <input type="number" placeholder="Debt"></input>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;
