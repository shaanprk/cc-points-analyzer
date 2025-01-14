import React from 'react';
import './Navbar.css';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <Link to="/">RewardTracker</Link>
      </div>
      <ul className="navbar-links">
        <li>
          <Link to="/signin" className="btn-signin">
            Sign In
          </Link>
        </li>
        <li>
          <Link to="/signup" className="btn-signup">
            Sign Up
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
