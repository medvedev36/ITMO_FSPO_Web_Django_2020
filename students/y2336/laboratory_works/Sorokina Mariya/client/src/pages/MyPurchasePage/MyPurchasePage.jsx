import React from 'react'
import Purchase from '../../components/Purchase'

const MyPurchase = ({ purchase }) => {

  return (
    <div className="row">
      <h3 className="flow-text center-align">История покупок</h3>

      <div className="col s8 offset-s2">
        {
          purchase &&

          purchase.map(item => {
            return (
              <Purchase
                id={item.id}
                image={item.attraction.image}
                name_attraction={item.attraction.name_attraction}
                price={item.price}
                date={item.date}
                key={item.id}
              />
            )
          })
        }
      </div>
    </div>

  )
}

export default MyPurchase
