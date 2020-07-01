import React from 'react'
import styles from './CreatePanel.module.css'
import imgClose from './../../img/close.svg'
import { useState } from 'react'

const CreatePanel = (props) => {

  const [isCreate, setIsCreate] = useState(false);
  const [input, setInput] = useState('');

  const createHandler = () => {
    if (!input) 
      return;

    props.createHandler('panel', { title: input });
    setIsCreate(false);
    setInput('');
  }

  return (
    <div className={styles.createPanel}>
      
      {!isCreate

        ? <div className={styles.addPanel} onClick={() => { setIsCreate(true) }}>
            + Добавить еще одну колонку
          </div>

        : <div className={styles.blockAddPanel}>
            <input type="text" className={styles.inputValuePanel} placeholder="Введите значение" autoFocus onChange={(e) => {setInput(e.target.value)}}/>
            <button className={styles.btnAddPanel} onClick={createHandler} >Добавить колонку</button>
            <img src={imgClose} className={styles.btnClose} alt="x" onClick={() => { setIsCreate(false); setInput('') }} />
          </div>

      }
    </div>
  )
}

export default CreatePanel
