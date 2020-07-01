import React from 'react'
import Card from '../Card/Card'
import styles from './Panel.module.css'
import CreateCard from '../CreateCard/CreateCard'
import imgClose from './../../img/close.svg'
import { Droppable, Draggable } from 'react-beautiful-dnd'

const Panel = (props) => {

  const removeHandler = () => {
    props.removeHandler('panel', { index: props.index });
  }

  const renderCard = (card, index) => {
    return (
      <Card
        id={card.id}
        index={index}
        panelIndex={props.index}
        value={card.value}
        removeHandler={props.removeHandler}
        key={card.id}
      />
    );
  }

  return (
    <Draggable draggableId={'panel' + String(props.id)} index={props.index}>
      {provided => (
        <div {...provided.draggableProps} ref={provided.innerRef} {...provided.dragHandleProps}>
          <Droppable droppableId={'panel' + String(props.id)} type='card'>
            {(provided) => (
              <div className={styles.panel} {...provided.droppableProps} ref={provided.innerRef}>

                <img src={imgClose} className={styles.btnClose} alt="x" onClick={removeHandler} />

                <div className={styles.title}>{props.title}</div>

                <div className={styles.cards}>
                  {props.cards.map((item, i) => renderCard(item, i))}

                  {provided.placeholder}
                </div>

                <CreateCard createHandler={props.createHandler} panelIndex={props.index} />
              </div>
            )}
          </Droppable>
        </div>
      )}
    </Draggable>
  )
}

export default Panel


