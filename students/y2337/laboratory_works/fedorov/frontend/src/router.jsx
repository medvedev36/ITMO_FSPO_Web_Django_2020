import React from 'react'
import {Switch, Route, Redirect, BrowserRouter} from 'react-router-dom';

import {Home} from "./components/home";
import Trip from "./components/trip";
import {Car} from "./components/car";

export const AppRouter = () => {
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/" exact>
                    <Home />
                </Route>
                <Route path="/trip" component={Trip}/>
                <Route path="/car/:id" component={Car} />
                <Redirect to="/" />
            </Switch>
        </BrowserRouter>
    )
}