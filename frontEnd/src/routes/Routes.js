import React from "react";
import { BrowserRouter as Router, Route, Routes} from "react-router-dom";
import Home from "../components/home/home";
import Calendar from "../components/calendar/calendar";
import ActivityLog from "../components/activitylog/activitylog";
import Faq from "../components/faq/faq";

const WebRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" exact element={<Home />} />
        <Route path="/calendar" element={<Calendar />} />
        <Route path="/activitylog" element={<ActivityLog />} />
        <Route path="/faq" element={<Faq/>} />
      </Routes>
    </Router>
  );
};

export default WebRoutes;