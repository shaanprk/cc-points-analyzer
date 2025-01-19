import React, { useState } from 'react';
import axios from 'axios';

import '../styles/RegisterPage.css';

const RegisterPage: React.FC = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
    first_name: '',
    last_name: '',
  });

  const [message, setMessage] = useState('');
  const [passwordCriteria, setPasswordCriteria] = useState({
    hasUpperCase: false,
    hasSpecialCharacter: false,
    hasNumber: false,
    isLongEnough: false,
  });

  const [isTypingPassword, setIsTypingPassword] = useState(false); // Track when user is typing in password field
  const [passwordsMatch, setPasswordsMatch] = useState(true); // Track if password and confirm password match

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });

    if (name === 'password') {
      // Update password criteria live as the user types
      setPasswordCriteria({
        hasUpperCase: /[A-Z]/.test(value),
        hasSpecialCharacter: /[!@#$%^&*]/.test(value),
        hasNumber: /\d/.test(value),
        isLongEnough: value.length >= 12,
      });
    }

    if (name === 'password' || name === 'confirmPassword') {
      setPasswordsMatch(
        name === 'password' ? value === formData.confirmPassword : formData.password === value
      );
    }
  };

  const handlePasswordFocus = () => {
    setIsTypingPassword(true);
  };

  const handlePasswordBlur = () => {
    setIsTypingPassword(false);
  };

  const validateForm = () => {
    const usernameRegex = /^[a-zA-Z0-9_.]+$/;
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{12,}$/;

    console.log(formData);

    if (formData.username.length < 6) {
      return 'Username must be at least 6 characters long.';
    }

    if (!usernameRegex.test(formData.username)) {
      return 'Username can only contain letters, numbers, underscores, and periods.';
    }

    if (formData.username.length > 30) {
      return 'Username must be 30 characters or less.';
    }

    if (formData.email.length > 100) {
      return 'Email must be 100 characters or less.';
    }

    if (formData.first_name.length > 50) {
      return 'First name must be 50 characters or less.';
    }

    if (formData.last_name.length > 50) {
      return 'Last name must be 50 characters or less.';
    }

    if (!passwordRegex.test(formData.password)) {
      return 'Password must be at least 12 characters long and contain at least one lowercase letter, one uppercase letter, one number, and one special character.';
    }

    if (
      formData.password.includes(formData.username) ||
      formData.password.includes(formData.email)
    ) {
      return 'Password cannot contain username or email.';
    }

    if (formData.password !== formData.confirmPassword) {
      return 'Passwords do not match.';
    }

    return '';
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const validationMessage = validateForm();
    if (validationMessage) {
      setMessage(validationMessage);
      return;
    }

    try {
      const response = await axios.post('http://127.0.0.1:8000/accounts/register/', formData);
      setMessage(response.data.message || 'Registration successful! Please verify your email.');
    } catch (error: any) {
      if (error.response?.data?.error) {
        if (error.response.data.error.includes('username')) {
          setMessage('Username already taken.');
        } else if (error.response.data.error.includes('email')) {
          setMessage('Another account with this email already exists.');
        } else {
          setMessage('An error occurred during registration.');
        }
      } else {
        setMessage('An error occurred during registration.');
      }
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
          {message.includes('Username') && <p className="error-message">{message}</p>}
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            required
          />
          {message.includes('Email') && <p className="error-message">{message}</p>}
          <input
            type="text"
            name="first_name"
            placeholder="First Name"
            value={formData.first_name}
            onChange={handleChange}
            required
          />
          <input
            type="text"
            name="last_name"
            placeholder="Last Name"
            value={formData.last_name}
            onChange={handleChange}
            required
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            onFocus={handlePasswordFocus} // Show password criteria when user is typing in password field
            onBlur={handlePasswordBlur} // Hide password criteria when user is done typing in password field
            required
          />
          {isTypingPassword && ( // Only show password criteria when user is typing in password field
            <ul className="password-criteria">
              <li className={passwordCriteria.hasUpperCase ? 'valid' : 'invalid'}>
                {passwordCriteria.hasUpperCase ? '✔' : '✘'} Upper Case
              </li>
              <li className={passwordCriteria.hasSpecialCharacter ? 'valid' : 'invalid'}>
                {passwordCriteria.hasSpecialCharacter ? '✔' : '✘'} Special Character
              </li>
              <li className={passwordCriteria.hasNumber ? 'valid' : 'invalid'}>
                {passwordCriteria.hasNumber ? '✔' : '✘'} Number
              </li>
              <li className={passwordCriteria.isLongEnough ? 'valid' : 'invalid'}>
                {passwordCriteria.isLongEnough ? '✔' : '✘'} At least 12 characters long
              </li>
            </ul>
          )}
          <input
            type="password"
            name="confirmPassword"
            placeholder="Confirm Password"
            value={formData.confirmPassword}
            onChange={handleChange}
            required
          />
          {!passwordsMatch && <p className="error-message">The passwords do not match.</p>}
          <button type="submit">Register</button>
        </form>
        {message && <p>{message}</p>}
      </main>
      <footer className="register-footer"></footer>
    </div>
  );
};

export default RegisterPage;
