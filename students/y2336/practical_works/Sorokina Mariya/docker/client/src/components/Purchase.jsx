import React from 'react'
import defaultImg from './../img/null.jpg'

const Purchase = ({ image, name_attraction, date, price }) => {
  return (
    <div className="card horizontal hoverable">
      <div className="card-image">
        <img src={image || defaultImg} alt="Аттракцион" />
        <span className="card-title blue lighten-2">{name_attraction}</span>
      </div>
      <div className="card-content">
        <p>Дата покупки:  {date}</p>
        <p>Цена покупки: {price}руб </p>
      </div>

    </div>
  )
}

export default Purchase
