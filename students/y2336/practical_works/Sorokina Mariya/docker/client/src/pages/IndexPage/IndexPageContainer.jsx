import React, { useEffect, useState, useCallback } from 'react'
import IndexPage from './IndexPage'
import { useHttp } from '../../hooks/http.hook'

const IndexPageContainer = () => {
  const { request } = useHttp();

  const [attraction, setAttraction] = useState(null);

  const loadData = useCallback(() => {
    request('api/popular_attraction', 'GET')
      .then(data => { setAttraction(data[0]); })
  }, [request]);

  useEffect(() => {
    loadData();
  }, [loadData]);

  return (<IndexPage attraction={attraction} />)
}

export default IndexPageContainer
