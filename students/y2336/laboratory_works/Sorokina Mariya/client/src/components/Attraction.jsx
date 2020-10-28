import React from 'react'
import { NavLink } from 'react-router-dom'
import defaultImg from './../img/null.jpg'

const Attraction = ({ id, image, name_attraction, adult_price, children_price, address_playground }) => {

  return (
    <div className="card  hoverable">
      <div className="card-image">
        <img src={image || defaultImg} alt="Парк" />
        <span className="card-title blue lighten-2">{name_attraction}</span>
      </div>
      <div className="card-content">
        <p>Взрослый билет: {adult_price}руб</p>
        <p>Детский билет: {children_price}руб</p>
        <p>Адрес: {address_playground}</p>
      </div>
      <div className="card-action">
        <NavLink to={`buyticket:${id}`} className="waves-effect waves-light btn blue darken-4" >Купить билет онлайн</NavLink>
      </div>
    </div>
  )
}

export default Attraction
