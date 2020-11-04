import React, { useState, useCallback, useEffect, useContext } from 'react'
import MyPurchasePage from './MyPurchasePage'
import { useHttp } from '../../hooks/http.hook';
import { AuthContext } from '../../context/AuthContext';
import { useHistory } from 'react-router-dom';

const MyPurchasePageContainer = () => {
  const history = useHistory();

  const { token } = useContext(AuthContext);

  const { request } = useHttp();

  if (!token) {
    history.push('auth')
  }

  const [purchase, setPurchase] = useState(null);

  const loadData = useCallback(() => {
    request('api/purchase', 'GET', null, {
      'Authorization': 'Bearer ' + token
    })
      .then(data => { setPurchase(data); })
      .catch(err => { window.M.toast({ html: err }) })
  }, [token, request]);

  useEffect(() => {
    loadData();
  }, [loadData]);

  return (
    <MyPurchasePage purchase={purchase} />
  )
}

export default MyPurchasePageContainer
