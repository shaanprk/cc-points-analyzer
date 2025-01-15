// import React from 'react';
import '../styles/LandingPage.css';
import Navbar from '../components/Navbar/Navbar';
import Footer from '../components/Footer/Footer';

const LandingPage = () => {
  return (
    <div className="landing-page">
      <Navbar />
      <section className="overview">
        <h1>Track, analyze, and optimize your credit card rewards</h1>
        <h3>
          Get personalized recommendations for the best credit cards based on your spending habits.
        </h3>
      </section>
      <Footer />
    </div>
  );
};

export default LandingPage;
