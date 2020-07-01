import React from "react";
import {AppRouter} from "./router";
import {NavBar} from "./components/navbar";
import {AuthContext} from "./context/auth";
import {useToken} from "./hooks/auth.hook";

const App = () => {
    const {login, logout, token} = useToken()
    console.log(token)

    return (
        <AuthContext.Provider value={{login, logout, token}}>
            <NavBar />
            <div className="container my-5">
                <AppRouter />
            </div>
        </AuthContext.Provider>
        )
}

export default App;