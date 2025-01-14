// import React from 'react';
// // import './LandingPage.css';
import Navbar from '../components/Navbar/Navbar';
import Footer from '../components/Footer/Footer';

const LandingPage = () => {
  return (
    <div className="landing-page">
      <Navbar />
      <header className="landing-header">
        <h1>Welcome to RewardTracker </h1>
      </header>
      <Footer />
    </div>
  );
};

export default LandingPage;
