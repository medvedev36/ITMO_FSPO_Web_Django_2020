import React from 'react'
import Playground from '../../components/Playground'

const PlaygroundsPage = ({ playgrounds }) => {

  return (
    <div className="row container center-align">
      <h3 className="flow-text">Площадки города</h3>

      <div className="col s6 offset-s3">
        {
          playgrounds.map(item => {
            return (
              <Playground
                id={item.id}
                image={item.image}
                last_name={item.last_name}
                address_playground={item.address_playground}
                key={item.id}
              />
            );
          })
        }
      </div>

    </div>
  )
}

export default PlaygroundsPage
