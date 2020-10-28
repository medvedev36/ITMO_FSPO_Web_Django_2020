import React from 'react'
import { NavLink } from 'react-router-dom'
import Attraction from '../../components/Attraction'

const IndexPage = ({ attraction }) => {

  return (
    <div className="row container">
      <div className="col s12">
        <div className="card center-align hoverable">
          <div className="card-image">
            <img src="https://res.klook.com/images/fl_lossy.progressive,q_65/c_fill,w_1920,h_720,f_auto/w_80,x_15,y_15,g_south_west,l_klook_water/activities/rebnk36tflvwpmtqroib/후지큐하이랜드일일패스버스왕복이동서비스.jpg" alt="Парк" />
            <span className="card-title blue lighten-2">ГОРОДСКИЕ ПАРКИ С АТТРАКЦИОНАМИ</span>
          </div>
          <div className="card-action">
            <NavLink to="playgrounds" className="waves-effect waves-light btn blue darken-4" >Посмотреть полощадки города</NavLink>
          </div>
        </div>
      </div>

      <div className="col s6 offset-s3 center-align">
        <h3 className="flow-text">Самый популярный аттракцион</h3>

        {
          attraction &&
          <Attraction
            id={attraction.attraction.id}
            image={attraction.attraction.image}
            name_attraction={attraction.attraction.name_attraction}
            adult_price={attraction.attraction.adult_price}
            children_price={attraction.attraction.children_price}
            address_playground={attraction.playground.address_playground}
            key={attraction.id}
          />
        }


      </div>
    </div>
  )
}

export default IndexPage
