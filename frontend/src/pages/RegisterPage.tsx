import React, { useState } from 'react';
import axios from 'axios';

import '../styles/RegisterPage.css';

const RegisterPage: React.FC = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
  });

  const [message, setMessage] = useState('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/accounts/register/', formData);
      setMessage(response.data.message || 'Registration successful! Please verify your email.');
    } catch (error: any) {
      setMessage(error.response?.data?.error || 'An error occurred during registration.');
    }
  };

  return (
    <div className="register-page">
      <header className="register-header">
        <h1>Welcome to SignUp</h1>
      </header>
      <main className="register-main">
        <h2>Register Form</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            name="username"
            placeholder="Username"
            value={formData.username}
            onChange={handleChange}
            required
          />
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            required
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            required
          />
          <button type="submit">Register</button>
        </form>
        {message && <p>{message}</p>}
      </main>
      <footer className="register-footer"></footer>
    </div>
  );
};

export default RegisterPage;
