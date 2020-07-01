import React, {useContext} from "react";
import {Logout} from "./auth";
import {AuthContext} from "../context/auth";

export const NavBar = () => {
    const auth = useContext(AuthContext)
    const isAuth = !!auth.token

    return (
       <nav className="navbar navbar-dark sticky-top bg-dark">
            <a className="navbar-brand" href="/">Carsharing</a>
            {isAuth && <Logout />}
        </nav>) 
}