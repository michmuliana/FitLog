import React, { useState} from "react";
import './navbar.css';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCalendar, faComments, faChartSimple, faClipboard} from "@fortawesome/free-solid-svg-icons";
import { faGithub, faLinkedin } from "@fortawesome/free-brands-svg-icons";
import Logo from '../../asset/FitLog.png';

const Navbar = () => {
  const [selectedOption, setSelectedOption] = useState(null);

  const handleOptionClick = (option) => {
    setSelectedOption(option);
  }

  return (
    <nav className="navbar">
      <div className="logoContainer">
        <img src={Logo} alt="Logo" className="logo" />
        <span className="appName">FitLog</span>
      </div>

      <ul className="navList">
        <li className={`navOption ${selectedOption === 'dashboard' ? 'active' : ''}`}>
        {/* <li className="navOption active"> */}
          <a href="/" onClick={() => handleOptionClick('dashboard')}>
            <FontAwesomeIcon icon={faChartSimple} className="icon" />
            Dashboard
          </a>
        </li>
        <li className={`navOption ${selectedOption === 'calendar' ? 'active' : ''}`}>
          <FontAwesomeIcon icon={faCalendar} className="icon" />
          <a href="/calendar" onClick={() => handleOptionClick('calendar')}>Calendar</a>
        </li>
        <li className={`navOption ${selectedOption === 'activitylog' ? 'active' : ''}`}>
          <FontAwesomeIcon icon={faClipboard} className="icon" />
          <a href="/activitylog" onClick={() => handleOptionClick('activitylog')}>Activity Log</a>
        </li>
        <li className={`navOption ${selectedOption === 'faq' ? 'active' : ''}`}>
          <FontAwesomeIcon icon={faComments} className="icon" />
          <a href="/faq" onClick={() => handleOptionClick('faq')}>FAQ</a>
        </li>
      </ul>
      <div className="footer">
        <hr/>
        <p className="ownerName">Made with 💕 by Michelle</p>
        <div className="socialIcons">
          <a
            href="https://github.com/your-github"
            target="_blank"
            rel="noopener noreferrer"
          >
            <FontAwesomeIcon icon={faGithub} className="icon" />
          </a>
          <a
            href="https://linkedin.com/in/your-linkedin"
            target="_blank"
            rel="noopener noreferrer"
          >
            <FontAwesomeIcon icon={faLinkedin} className="icon" />
          </a>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;