import React, { useContext, useEffect, useState } from 'react'
import { AuthContext } from '../context/AuthContext'
import { useHttp } from '../hooks/http.hook';
import { useHistory } from 'react-router-dom';

const AuthPage = () => {
  const auth = useContext(AuthContext);

  const history = useHistory();

  const { request, error, clearError } = useHttp();

  const [form, setForm] = useState({
    'username': '', password: ''
  });

  useEffect(() => {
    if (error)
      window.M.toast({ html: error });

    clearError();
  }, [error, clearError]);

  const changeHangler = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  const registerHandler = async (e) => {
    e.preventDefault();

    try {
      const data = await request('/auth/users/', 'POST', { ...form });

      if (data.id) {
        window.M.toast({ html: 'Успешная регистрация' });
      }
    } catch (e) {

    }
  }

  const loginHandler = async (e) => {
    e.preventDefault();

    try {
      const tokens = await request('/auth/jwt/create/', 'POST', { ...form });

      auth.login(tokens.access, tokens.refresh);

      history.push('/');
    } catch (e) {

    }
  }

  return (
    <div className="row">
      <h1 className="">Авторизация</h1>
      <form className="col s12">
        <div className="row">
          <div className="input-field col s6">
            <input id="icon_prefix" type="text" className="validate" name="username" onChange={changeHangler} />
            <label htmlFor="icon_prefix">Username</label>
          </div>
          <div className="input-field col s6">
            <input id="icon_telephone" type="password" className="validate" name="password" onChange={changeHangler} />
            <label htmlFor="icon_telephone">Password</label>
          </div>
        </div>
        <div className="row">
          <button className="col s6 waves-effect waves-light btn blue darken-4" onClick={loginHandler}>Вход</button>
          <button className="col s6 waves-effect waves-light btn blue darken-4" onClick={registerHandler}>Регистрация</button>
        </div>
      </form>
    </div>
  )
}

export default AuthPage
