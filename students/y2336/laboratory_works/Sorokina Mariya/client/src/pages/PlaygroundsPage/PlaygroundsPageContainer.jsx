import React, { useState, useCallback, useEffect } from 'react'
import PlaygroundsPage from './PlaygroundsPage'
import { useHttp } from '../../hooks/http.hook'

const PlaygroundsPageContainer = () => {
  const { request } = useHttp();

  const [playgrounds, setPlaygrounds] = useState([]);

  const loadData = useCallback(() => {
    request('api/playgrounds', 'GET')
      .then(data => { setPlaygrounds(data); })
  }, [request]);

  useEffect(() => {
    loadData();
  }, [loadData])

  return (
    <PlaygroundsPage
      playgrounds={playgrounds}
    />
  )
}

export default PlaygroundsPageContainer
