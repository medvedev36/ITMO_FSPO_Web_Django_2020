import React, { useContext } from 'react'
import { NavLink } from 'react-router-dom'
import { AuthContext } from './../../context/AuthContext'
import styles from './NavBar.module.css'

const NavBar = () => {
  const auth = useContext(AuthContext);

  const logoutHandler = (e) => {
    e.preventDefault();
    auth.logout();
  }
  
  return (
    <div className={styles.nav}>
      <NavLink to="/boards" className={styles.btn}>Доски</NavLink>
      <a href="/" onClick={logoutHandler} className={styles.btn}>Выйти</a>
    </div>
  )
}

export default NavBar
