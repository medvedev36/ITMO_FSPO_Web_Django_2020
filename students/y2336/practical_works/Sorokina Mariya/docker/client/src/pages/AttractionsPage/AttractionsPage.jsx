import React, { useState } from 'react'
import Attraction from '../../components/Attraction'

const AttractionsPage = ({ attractions, playgrounds, types }) => {

  const [filters, setFilters] = useState({
    playground: null, type: null
  });

  const changeHandler = (e) => {
    setFilters({ ...filters, [e.target.name]: e.target.value });
  }

  attractions = attractions.filter(item => {

    if (filters.type) {
      if (filters.type !== item.attraction.type.attraction_type)
        return false;
    }

    if (filters.playground) {
      if (filters.playground !== item.playground.address_playground)
        return false;
    }

    return true;
  });

  return (
    <div className="row container center-align">
      <h3 className="flow-text">Аттракционы</h3>

      <div className="col s6 offset-s3">
        {
          attractions &&

          attractions.map((item) => {
            return (
              <Attraction
                id={item.attraction.id}
                image={item.attraction.image}
                name_attraction={item.attraction.name_attraction}
                adult_price={item.attraction.adult_price}
                children_price={item.attraction.children_price}
                address_playground={item.playground.address_playground}
                key={item.id}
              />
            )
          })
        }

      </div>

      <div className="col s3">
        <label>Категория аттракциона</label>
        <select className="browser-default" defaultValue="" name="type" onChange={changeHandler}>
          <option value="">Выберите категорию</option>
          {
            types.map((item, i) => {
              return (
                <option value={item.attraction_type} key={i} >{item.attraction_type}</option>
              );
            })
          }
        </select>

        <label>Площадка</label>
        <select className="browser-default" defaultValue="" name="playground" onChange={changeHandler}>
          <option value="" >Выберите площадку</option>
          {
            playgrounds.map((item, i) => {
              return (
                <option value={item.address_playground} key={i} >{item.address_playground}</option>
              );
            })
          }
        </select>
      </div>

    </div>
  )
}

export default AttractionsPage
