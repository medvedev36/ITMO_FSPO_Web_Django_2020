import React from 'react'
import img from './../img/null.jpg'

const Playground = ({ image, address_playground, last_name }) => {

  return (
    <div className="card  hoverable">
      <div className="card-image">
        <img src={image || img} alt="Парк" />
        <span className="card-title blue lighten-2">{address_playground}</span>
      </div>
      <div className="card-content">
        <p>Директор площадки: {last_name}</p>
      </div>

    </div>
  )
}

export default Playground
