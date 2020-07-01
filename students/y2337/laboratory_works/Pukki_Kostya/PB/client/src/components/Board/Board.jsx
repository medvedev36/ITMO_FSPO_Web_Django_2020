import React from 'react'
import { NavLink } from 'react-router-dom'
import styles from './Board.module.css'
import imgClose from './../../img/close.svg'

const Board = (props) => {

  return (
    <NavLink to={`/board:${props.id}`} className={styles.board}>
      <div className={styles.boardName}>{props.title}</div>
      <img src={imgClose} className={styles.btnDelete} alt="x" board_id={props.id} onClick={props.deleteHandler} />
    </NavLink>
  )
}

export default Board
