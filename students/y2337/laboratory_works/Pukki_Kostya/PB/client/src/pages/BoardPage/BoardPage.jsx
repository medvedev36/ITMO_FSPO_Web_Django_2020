import React from 'react';
import Panel from '../../components/Panel/Panel';
import styles from './BoardPage.module.css'
import CreatePanel from '../../components/CreatePanel/CreatePanel';
import { DragDropContext, Droppable } from 'react-beautiful-dnd';

const BoardPage = (props) => {

  const renderPanel = (panel, index) => {
    return (
      <Panel
        id={panel.id}
        title={panel.title}
        index={index}
        cards={panel.card}
        createHandler={props.createHandler}
        removeHandler={props.removeHandler}
        key={panel.id}
      />
    )
  }

  return (

    <DragDropContext onDragEnd={props.onDragEnd}>
      <Droppable droppableId='allPanels' direction="horizontal" type='panel'>
        {provided => (
          <div className={styles.panels} ref={provided.innerRef}>
            {props.panels.map((item, i) => renderPanel(item, i))}
            
            {provided.placeholder}

            <CreatePanel
              createHandler={props.createHandler}
            />
          </div>
        )}
      </Droppable>
    </DragDropContext>

  );
}

export default BoardPage;