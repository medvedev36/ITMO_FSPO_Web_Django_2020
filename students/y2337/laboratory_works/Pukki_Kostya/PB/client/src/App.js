import React from 'react'

import NavBar from './components/NavBar/NavBar'
import Loader from './components/Loader/Loader';
import { useAuth } from './hooks/auth.hook'
import { AuthContext } from './context/AuthContext';
import { useRoutes } from './routes'

//! box-shadow последней карточки

const App = () => {

  const { token, login, logout, ready } = useAuth();
  const isAuth = !!token;

  const routes = useRoutes(isAuth);

  if (!ready) {
    return (<Loader />);
  }

  return (
    <AuthContext.Provider value={{ token, login, logout }}>
      <div className="App">
        {isAuth && <NavBar />}
        {routes}
      </div>
    </AuthContext.Provider>
  );
}

export default App;
