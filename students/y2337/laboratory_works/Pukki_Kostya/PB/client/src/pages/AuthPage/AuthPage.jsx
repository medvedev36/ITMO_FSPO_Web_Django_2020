import React, { useContext, useState, useEffect } from 'react'
import styles from './AuthPage.module.css'
import { AuthContext } from './../../context/AuthContext'
import { useHttp } from '../../hooks/http.hook';


const AuthPage = () => {
  const auth = useContext(AuthContext);

  const { request, error, clearError } = useHttp();

  const [form, setForm] = useState({
    'username': '', password: ''
  });

  useEffect(() => {
    if (error)
      Window.toasts(error);

    clearError();
  }, [error, clearError]);


  const changeHangler = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  const registerHandler = async () => {
    try {
      const data = await request('/auth/users/', 'POST', { ...form });

      if (data.id) {
        Window.toasts('Успешная регистрация');
      }
    } catch (e) {

    }
  }

  const loginHandler = async () => {
    try {
      const tokens = await request('/auth/jwt/create/', 'POST', { ...form });

      auth.login(tokens.access, tokens.refresh);
    } catch (e) {

    }
  }

  return (
    <div className={styles.form}>
      <h3>Вход в систему</h3>
      <input type="text" name="username" placeholder="Логин" onChange={changeHangler} />
      <input type="password" name="password" placeholder="Пароль" onChange={changeHangler} />
      <button type="submit" onClick={loginHandler}>Вход</button>
      <button type="submit" onClick={registerHandler}>Регистрация</button>
    </div>
  );
}

export default AuthPage;