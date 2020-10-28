import React, { useState } from 'react'

const ADULT = 'adult';
const CHILDREN = 'children';

const PurchaseTicket = ({ attraction, buyTicket }) => {

  const [form, setForm] = useState({
    numberCard: '',
    cvv: '',
    date: '',
    name: '',
    type: ''
  })

  const changeHandler = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  const price = form.type === ADULT ? attraction.adult_price : form.type === CHILDREN ? attraction.children_price : '';

  return (
    <div className="row">
      <h3 className="flow-text center-align">Покупка билета на "{attraction.name_attraction}"</h3>

      <form className="col s12" onSubmit={(e) => {e.preventDefault(); buyTicket(form)}}>
        <div className="row">
          <div className="input-field col s6">
            <input id="icon_prefix" type="number" className="validate" name="numberCard" onChange={changeHandler} required />
            <label htmlFor="icon_prefix">Номер карты</label>
          </div>
          <div className="input-field col s6">
            <input id="icon_telephone" type="number" className="validate" name="cvv" onChange={changeHandler} required />
            <label htmlFor="icon_telephone">cvv</label>
          </div>
          <div className="input-field col s6">
            <input id="icon_telephone" type="date" className="validate" name="date" onChange={changeHandler} required />
            <label htmlFor="icon_telephone">Срок действия</label>
          </div>
          <div className="input-field col s6">
            <input id="icon_telephone" type="text" className="validate" name="name" onChange={changeHandler} required />
            <label htmlFor="icon_telephone">Держатель карты</label>
          </div>
        </div>

        <button className="col s6 waves-effect waves-light btn blue darken-4">Купить</button>

        <div className="col s6">
          <label>Категория билета</label>
          <select className="browser-default" name="type" onChange={changeHandler} defaultValue="" required>
            <option value="" disabled>Выберите категорию</option>
            <option value="children">Детский</option>
            <option value="adult">Взрослый</option>
          </select>

          <p className="flow-text">Цена: {price}руб</p>
        </div>

      </form>

    </div>
  )
}

export default PurchaseTicket
