import React from 'react';
import { Switch, Route, Redirect } from 'react-router-dom';

import AuthPage from './pages/AuthPage/AuthPage';
import BoardPageContainer from './pages/BoardPage/BoardPageContainer';
import BoardsPageContainer from './pages/BoardsPage/BoardsPageContainer';

export const useRoutes = (isAuth) => {
  if (isAuth) {
    return (
      <Switch>
        <Route path="/boards" exact>
          <BoardsPageContainer />
        </Route>

        <Route path="/board:id" component={BoardPageContainer} />

        <Redirect to="/boards" />
      </Switch>
    );
  }

  return (
    <Switch>
      <Route path="/" exact>
        <AuthPage />
      </Route>

      <Redirect to="/" />
    </Switch>
  );
}