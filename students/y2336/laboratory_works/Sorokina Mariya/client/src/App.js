import React from 'react';
import NavBar from './components/NavBar';
import Footer from './components/Footer';

import useRoutes from './routes';
import { useAuth } from './hooks/auth.hook';
import { AuthContext } from './context/AuthContext';

function App() {
  const { token, login, logout, ready } = useAuth();

  const isAuth = !!token;

  const routes = useRoutes();

  if (!ready) {
    return (<div>LOADING</div>)
  }

  return (
    <AuthContext.Provider value={{ token, login, logout }}>
      <div className="wrapper">
        <NavBar isAuth={isAuth} />

        {routes}

        <Footer />
      </div>
    </AuthContext.Provider>
  );
}

export default App;
