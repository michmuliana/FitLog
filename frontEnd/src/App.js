import React from "react";
import Navbar from "./components/navbar/navbar";
import WebRoutes from "./routes/Routes";
import './App.css';

function App() {
  return (
    <div className="App">
      <Navbar/>
      <div className="container">
        <WebRoutes/>
      </div>
    </div>
  );
}

export default App;
