import React from 'react'
import styles from './Card.module.css'
import imgClose from './../../img/close.svg'
import { Draggable } from 'react-beautiful-dnd'

const Card = (props) => {

  const removeHandler = () => {
    props.removeHandler('card', { id: props.id, cardIndex: props.index, panelIndex: props.panelIndex });
  }

  return (
    <Draggable draggableId={'card' + String(props.id)} index={props.index}>
      {provided => (
        <div className={styles.card} ref={provided.innerRef} {...provided.draggableProps} {...provided.dragHandleProps}>
          <div className={styles.value}>{props.value}</div>
          <img src={imgClose} className={styles.btnDelete} alt="x" onClick={removeHandler} />
        </div>
      )}
    </Draggable>
  )
}

export default Card
