import {createContext} from 'react';

function noop() {};

export const AuthContext = createContext({
  token: null,
  tokenRefresh: null,
  login: noop,
  logout: noop
});