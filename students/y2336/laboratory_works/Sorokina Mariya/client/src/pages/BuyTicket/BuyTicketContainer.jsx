import React, { useContext, useCallback, useEffect, useState } from 'react'
import BuyTicket from './BuyTicket'
import { useHistory } from 'react-router-dom';
import { AuthContext } from '../../context/AuthContext';
import { useHttp } from '../../hooks/http.hook';

const BuyTicketContainer = (props) => {
  const { request } = useHttp();

  const history = useHistory();

  const { token } = useContext(AuthContext);

  if (!token) {
    history.push('auth')
  }

  const attractionId = props.match.params.id.slice(1);

  const [attraction, setAttraction] = useState(null);

  const loadTicket = useCallback(() => {
    request(`api/attraction/${attractionId}`, 'GET')
      .then(data => { setAttraction(data); })
      .catch(err => { window.M.toast({ html: err }) })
  }, [request, attractionId]);

  useEffect(() => {
    loadTicket();
  }, [loadTicket]);


  const buyTicket = (form) => {
    request(`api/buyticket/${attractionId}`, 'POST', form, {
      'Authorization': 'Bearer ' + token
    })
      .then(data => { window.M.toast({ html: data }); history.push('purchase'); })
      .catch(err => { window.M.toast({ html: err }); history.push('purchase'); })
  }

  if (!attraction) {
    return (<div>LOADING</div>);
  }

  return (
    <BuyTicket attraction={attraction} buyTicket={buyTicket} />
  )
}

export default BuyTicketContainer
