import React, { useContext, useState, useEffect } from 'react';

import { AuthContext } from '../../context/AuthContext'

import { useHttp } from '../../hooks/http.hook'
import BoardsPage from './BoardsPage';
import { useCallback } from 'react';

const BoardsPageContainer = () => {

  const { request } = useHttp();
  const auth = useContext(AuthContext)

  const [boards, setBoards] = useState([])

  const loadBoards = useCallback(() => {
    request('api/boards', 'GET', null, {
      'Authorization': 'Bearer ' + auth.token
    })
      .then(data => { setBoards(data) })
  }, [auth.token, request])

  const deleteHandler = (e) => {
    e.preventDefault();

    const id = e.target.getAttribute('board_id');

    request(`/api/board/delete/${id}`, 'DELETE', null, {
      'Authorization': 'Bearer ' + auth.token
    })
      .then(data => {
        Window.toasts(data.detail);
        loadBoards();
      });
  }

  const createHandler = (title) => {
    if (!title.length) {
      Window.toasts('Некорректный ввод');
      return;
    }

    request('api/board/create', 'POST', { title }, {
      'Authorization': 'Bearer ' + auth.token
    })
      .then(data => {
        Window.toasts(data.detail);
        loadBoards();
      });
  }

  useEffect(() => {
    loadBoards();
  }, [loadBoards]);

  return (
    <BoardsPage
      boards={boards}
      deleteHandler={deleteHandler}
      createHandler={createHandler}
    />
  );
}

export default BoardsPageContainer;