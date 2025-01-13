// import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LandingPage from '../pages/LandingPage';
import HomePage from '../pages/HomePage';
import SignInPage from '../pages/SignInPage';
import SignUpPage from '../pages/SignUpPage';
import ProfilePage from '../pages/ProfilePage';
import NotFoundPage from '../pages/NotFoundPage';

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/signin" element={<SignInPage />} />
        <Route path="/signup" element={<SignUpPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;
