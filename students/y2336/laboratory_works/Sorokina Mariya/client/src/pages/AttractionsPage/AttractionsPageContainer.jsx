import React, { useState, useCallback, useEffect } from 'react'
import AttractionsPage from './AttractionsPage'
import { useHttp } from '../../hooks/http.hook';

const AttractionsPageContainer = () => {
  const [attractions, setAttractions] = useState(null);
  const [playgrounds, setPlaygrounds] = useState(null);
  const [types, setTypes] = useState(null);

  const { request } = useHttp();

  const loadData = useCallback(() => {
    request('api/useattractions', 'GET')
      .then(data => { setAttractions(data); })

    request('api/playgrounds', 'GET')
      .then(data => { setPlaygrounds(data); })

    request('api/types', 'GET')
      .then(data => { setTypes(data); })
  }, [request]);

  useEffect(() => {
    loadData();
  }, [loadData])

  if (!attractions || !playgrounds || !types) {
    return(<div>LOADING</div>);
  }

  return (
    <AttractionsPage attractions={attractions} playgrounds={playgrounds} types={types} />
  )
}

export default AttractionsPageContainer
