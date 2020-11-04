import React, { useContext } from 'react'
import { NavLink } from 'react-router-dom'
import { AuthContext } from '../context/AuthContext'

const NavBar = ({ isAuth }) => {

  const { logout } = useContext(AuthContext);

  return (
    <nav className="blue lighten-2">
      <div className="nav-wrapper container">
        <NavLink to="/" className="brand-logo">Аттракционы.рф</NavLink>
        <ul id="nav-mobile" className="right hide-on-med-and-down">
          <li><NavLink to="/">Главная</NavLink></li>
          <li><NavLink to="playgrounds">Площадки</NavLink></li>
          <li><NavLink to="attractions">Аттракционы</NavLink></li>
          <li><NavLink to="contacts">Контакты</NavLink></li>
          {
            isAuth &&
            <li><NavLink to="purchase" className="light-blue darken-4">Мои покупки</NavLink></li>
          }

          {
            !isAuth &&
            <li><NavLink to="auth" className="waves-effect waves-light btn blue darken-4">Вход</NavLink></li>
          }

          {
            isAuth &&
            <li><NavLink to="/" className="waves-effect waves-light btn blue darken-4" onClick={logout} >Выход</NavLink></li>
          }
        </ul>
      </div>
    </nav>
  )
}

export default NavBar
