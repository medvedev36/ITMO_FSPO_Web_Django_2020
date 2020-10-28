import React from 'react'
import IndexPageContainer from './pages/IndexPage/IndexPageContainer'
import AttractionsPageContainer from './pages/AttractionsPage/AttractionsPageContainer';
import PlaygroundsPageContainer from './pages/PlaygroundsPage/PlaygroundsPageContainer';
import MyPurchasePageContainer from './pages/MyPurchasePage/MyPurchasePageContainer';
import BuyTicketContainer from './pages/BuyTicket/BuyTicketContainer';
import { Switch, Route, Redirect } from 'react-router-dom';
import ContactPage from './pages/ContactPage';
import AuthPage from './pages/AuthPage';

const useRoutes = () => {
  return (
    <Switch>
      <Route path="/" exact>
        <IndexPageContainer />
      </Route>

      <Route path="/attractions" exact>
        <AttractionsPageContainer />
      </Route>

      <Route path="/playgrounds" exact>
        <PlaygroundsPageContainer />
      </Route>

      <Route path="/contacts" exact>
        <ContactPage />
      </Route>

      <Route path="/auth" exact>
        <AuthPage />
      </Route>

      <Route path="/purchase" exact>
        <MyPurchasePageContainer />
      </Route>

      <Route path="/buyticket:id" component={BuyTicketContainer} />
      

      <Redirect to="/" />
    </Switch>
  );
}

export default useRoutes;
