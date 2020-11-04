import React, { useContext, useEffect } from 'react';
import BoardPage from '../BoardPage/BoardPage';
import { useHttp } from '../../hooks/http.hook';
import { AuthContext } from '../../context/AuthContext';
import { useReducer } from 'react';
import { useCallback } from 'react';

const ADD_PANEL = 'add_panel';
const ADD_CARD = 'add_card';
const REMOVE_PANEL = 'remove_panel';
const REMOVE_CARD = 'remove_card';
// const CARD = 'card';
const PANEL = 'panel';
const SET_STATE = 'set_state';
const MOVE_PANEL = 'move_panel';
const MOVE_CARD = 'move_card';

function toMax(a, b) { // Функция для sort
  if (a.index > b.index) return 1;
  if (a.index === b.index) return 0;
  if (a.index < b.index) return -1;
}

function indexArray(arr) {
  arr.forEach((item, i) => {
    item.index = i;
  });
}

const initState = [];

function reducer(state, action) {
  switch (action.type) {

    case SET_STATE: {
      return action.data;
    }

    case ADD_PANEL: {
      let stateCopy = [...state];
      stateCopy.push(action.panel);
      return stateCopy;
    }

    case REMOVE_PANEL: {
      let stateCopy = [...state];
      stateCopy.splice(action.index, 1);
      return stateCopy;
    }

    case ADD_CARD: {
      let stateCopy = [...state];
      stateCopy[action.panelIndex] = { ...state[action.panelIndex] }
      stateCopy[action.panelIndex].card = [...state[action.panelIndex].card]
      stateCopy[action.panelIndex].card.push(action.card);
      return stateCopy;
    }

    case REMOVE_CARD: {
      let stateCopy = [...state];
      stateCopy[action.panelIndex] = { ...state[action.panelIndex] };
      stateCopy[action.panelIndex].card = [...state[action.panelIndex].card]
      stateCopy[action.panelIndex].card.splice(action.cardIndex, 1);
      return stateCopy;
    }

    case MOVE_PANEL: {
      let stateCopy = [...state];
      let elem = stateCopy.splice(action.fromIndex, 1);
      stateCopy.splice(action.toIndex, 0, elem[0]);
      indexArray(stateCopy);
      return stateCopy;
    }

    case MOVE_CARD: {
      let stateCopy = [...state];

      stateCopy[action.from.panelIndex] = { ...state[action.from.panelIndex] };
      stateCopy[action.from.panelIndex].card = [...state[action.from.panelIndex].card];
      let elem = stateCopy[action.from.panelIndex].card.splice(action.from.cardIndex, 1);
      indexArray(stateCopy[action.from.panelIndex].card);

      if (action.from.panelIndex !== action.to.panelIndex) {
        stateCopy[action.to.panelIndex] = { ...state[action.to.panelIndex] };
        stateCopy[action.to.panelIndex].card = [...state[action.to.panelIndex].card];
      }

      stateCopy[action.to.panelIndex].card.splice(action.to.cardIndex, 0, elem[0]);
      indexArray(stateCopy[action.to.panelIndex].card);

      return stateCopy;
    }

    default:
      throw new Error();
  }
}

const BoardPageContainer = (props) => {

  const [state, dispatch] = useReducer(reducer, initState);

  const auth = useContext(AuthContext);

  const { request } = useHttp();

  const boardId = props.match.params.id.slice(1);

  const loadData = useCallback(() => { // Загружает данные с сервера, и сортирует их по index
    request(`/api/board/details/${boardId}`, 'GET', null, {
      'Authorization': 'Bearer ' + auth.token
    })
      .then(data => {
        data.sort(toMax);

        data.forEach(item => {
          item.card.sort(toMax)
        });

        dispatch({ type: SET_STATE, data });
      })
  }, [auth.token, boardId, request])

  const createHandler = (type, params) => { // Обработчик создания панелей и карточек

    if (type === PANEL) {
      request('/api/panel/create', 'POST',
        {
          boardId,
          title: params.title,
          index: state.length
        },
        {
          'Authorization': 'Bearer ' + auth.token
        })
        .then(data => {
          dispatch({ type: ADD_PANEL, panel: data })
        })

    } else {
      request('/api/card/create', 'POST',
        {
          panelId: state[params.panelIndex].id,
          value: params.value,
          index: state[params.panelIndex].card.length
        },
        {
          'Authorization': 'Bearer ' + auth.token
        })
        .then(data => {
          dispatch({ type: ADD_CARD, card: data, panelIndex: params.panelIndex });
        })

    }
  }

  const removeHandler = (type, params) => { // Обработчик удаления панелей и карточек

    if (type === PANEL) {
      //TODO Исправить (возможность отправки множества запросов при плохом соединении)

      request(`/api/panel/delete/${state[params.index].id}`, 'DELETE', null, {
        'Authorization': 'Bearer ' + auth.token
      })
        .then(data => {
          dispatch({ type: REMOVE_PANEL, index: params.index });
        })
    } else {
      request(`/api/card/delete/${params.id}`, 'DELETE', null, {
        'Authorization': 'Bearer ' + auth.token
      })
        .then(data => {
          dispatch({ type: REMOVE_CARD, panelIndex: params.panelIndex, cardIndex: params.cardIndex });
        })
    }

  }

  useEffect(() => {
    loadData();
  }, [loadData]);

  const onDragEnd = (result) => { // Обработчик окончания dnd

    const { destination, source, draggableId, type } = result;

    if (!destination) {
      return;
    }

    if (type === PANEL) {

      dispatch({ type: MOVE_PANEL, fromIndex: source.index, toIndex: destination.index });

      request(`/api/panel/index`, 'PUT', {
        panels: state //* Передаем все состояние (BAD)
      }, {
        'Authorization': 'Bearer ' + auth.token
      })
        .then(data => { })
        .catch(err => {
          window.location.reload();
        })

    } else {
      const fromPanel = state.find(item => {
        return String(item.id) === source.droppableId.slice(5);
      });

      const toPanel = state.find(item => {
        return String(item.id) === destination.droppableId.slice(5);
      });

      dispatch({
        type: MOVE_CARD,
        from: { panelIndex: fromPanel.index, cardIndex: source.index },
        to: { panelIndex: toPanel.index, cardIndex: destination.index }
      })

      let cards = [];

      state.forEach(item => {
        cards = cards.concat(item.card);
      });

      request('/api/card/index', 'PUT', {
        cards
      }, {
        'Authorization': 'Bearer ' + auth.token
      })
        .then(data => {
          request(`/api/card/move/${draggableId.slice(4)}/${toPanel.id}`, 'PUT', null, {
            'Authorization': 'Bearer ' + auth.token
          })
            .then(data => { })
            .catch(err => {
              window.location.reload();
            })
        })
        .catch(err => {
          window.location.reload();
        })
    }
  }

  return (
    <BoardPage
      panels={state}
      createHandler={createHandler}
      removeHandler={removeHandler}
      onDragEnd={onDragEnd}
    />
  );
}

export default BoardPageContainer;