import React from 'react'
import styles from './CreateCard.module.css'
import imgClose from './../../img/close.svg'
import { useState } from 'react'

const CreateCard = (props) => {

  const [isCreate, setIsCreate] = useState(false);
  const [input, setInput] = useState('');

  const createHandler = () => {
    if (!input) 
      return;

    props.createHandler('card', { value: input, panelIndex: props.panelIndex });
    setIsCreate(false);
    setInput('');
  }

  return (
    <div className={styles.createCard}>

      {!isCreate

        ? <div className={styles.addCard} onClick={() => { setIsCreate(true) }}>
            + Добавить еще одну карточку
          </div>

        : <div className={styles.blockAddCard}>
            <textarea className={styles.inputValueCard} placeholder="Введите значение" autoFocus onChange={(e) => {setInput(e.target.value)}}></textarea>
            <button className={styles.btnAddCard} onClick={createHandler}>Добавить карточку</button>
            <img src={imgClose} className={styles.btnClose} alt="x" onClick={() => { setIsCreate(false); setInput(''); }} />
          </div>
          
      }

    </div>
  )
}

export default CreateCard
