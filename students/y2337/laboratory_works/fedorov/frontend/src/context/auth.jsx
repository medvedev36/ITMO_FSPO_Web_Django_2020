import { createContext } from 'react'

let nop = () => { }

export const AuthContext = createContext({
    token: null,
    login: nop,
    logout: nop,
})
