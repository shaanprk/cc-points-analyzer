import { Link } from 'react-router-dom';
import '../styles/LandingPage.css';
import ReactLogo from '../assets/react.svg';

const LandingPage = () => {
  return (
    <div className="landing-page">
      {/* Header */}
      <header className="landing-header">
        <Link to="/" className="logo">
          <img src={ReactLogo}></img>
          <p>Finance</p>
        </Link>
        <nav className="nav-bar">
          <ul>
            <li>
              <Link to="/signin" className="btn btn-secondary">
                Sign In
              </Link>
            </li>
            <li>
              <Link to="/signup" className="btn btn-primary">
                Sign Up
              </Link>
            </li>
          </ul>
        </nav>
      </header>

      <main className="landing-main">
        {/* Hero Section */}
        <section className="hero-section">
          <h1>Optimize Your Credit Card Rewards</h1>
          <p>Easily track, analyze, and maximize your credit card rewards in one place.</p>
          <a href="/signup" className="btn btn-cta">
            Get Started
          </a>
        </section>

        <section id="features" className="features-section">
          <h2>Features</h2>
          <div className="features">
            <div className="feature">
              <h3>Reward Optimization</h3>
              <p>Find the best credit card for every purchase with real-time recommendations.</p>
            </div>
            <div className="feature">
              <h3>Transaction Analysis</h3>
              <p>Track your spending and discover patterns to make informed decisions.</p>
            </div>
            <div className="feature">
              <h3>Custom Recommendations</h3>
              <p>Receive personalized credit card suggestions based on your habits.</p>
            </div>
          </div>
        </section>

        <section id="about" className="about-section">
          <h2>About Us</h2>
          <p>
            FinanceTracker helps users make the most of their credit card rewards by using
            cutting-edge technology to analyze spending habits and offer personalized
            recommendations.
          </p>
        </section>

        <section id="contact" className="contact-section">
          <h2>Contact</h2>
          <p>
            Have questions? Reach out to us at{' '}
            <a href="mailto:support@financetracker.com">support@financetracker.com</a>.
          </p>
        </section>
      </main>

      <footer className="landing-footer">
        <p>&copy; 2025 FinanceTracker. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default LandingPage;
