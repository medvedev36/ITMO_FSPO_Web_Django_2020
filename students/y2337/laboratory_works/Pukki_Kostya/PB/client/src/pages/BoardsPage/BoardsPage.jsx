import React, { useRef } from 'react';
import styles from './BoardsPage.module.css'
import Board from '../../components/Board/Board';

const BoardsPage = (props) => {

  const inpRef = useRef(null);

  return (
    <div className={styles.boardsPage}>

      {
        props.boards.map(item => {
          return (<Board id={item.id} title={item.title} deleteHandler={props.deleteHandler} key={item.id}/>);
        })
      }

      <div className={styles.newBoard}>
        <input ref={inpRef} type="text" placeholder="Название новой доски" />
        <button onClick={() => { props.createHandler(inpRef.current.value); inpRef.current.value = '' }}>Создать</button>
      </div>

    </div>
  );
}

export default BoardsPage;