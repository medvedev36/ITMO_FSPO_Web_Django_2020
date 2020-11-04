import { useState, useEffect } from "react";
import { useHttp } from "./http.hook";

const STORAGENAME = 'tokens';

export const useAuth = () => {
  const [token, setToken] = useState(null);
  const [tokenRefresh, setTokenRefresh] = useState(null);

  const [ready, setReady] = useState(false);

  const { request } = useHttp();

  const login = (jwtToken, jwtTokenRefresh) => {
    setToken(jwtToken);
    setTokenRefresh(jwtTokenRefresh);

    localStorage.setItem(STORAGENAME, JSON.stringify({ token: jwtToken, tokenRefresh: jwtTokenRefresh }));
  }

  const logout = () => {
    setToken(null);
    setTokenRefresh(null);

    localStorage.removeItem(STORAGENAME);
  }

  useEffect(() => {
    const tokens = JSON.parse(localStorage.getItem(STORAGENAME));

    if (tokens && tokens.tokenRefresh) {
      request('/auth/jwt/refresh/', 'POST', {
        'refresh': tokens.tokenRefresh
      })
        .then(data => {
          login(data.access, tokens.tokenRefresh);
          setReady(true);
        })
        .catch(err => {
          setReady(true);
          logout();
        })
    } else {
      setReady(true);
    }
  }, [request])

  return {
    login,
    logout,
    token,
    tokenRefresh,
    ready
  }

}