import {useCallback, useEffect, useState} from 'react'
import {useHttp} from "./http.hook"

const STORAGE = 'carsharestore'

export const useToken = () => {
    const [token, setToken] = useState(null)
    const {request} = useHttp()

    const login = (token) => {
        console.log('login')
        setToken(token)
        localStorage.setItem(STORAGE, JSON.stringify(token))
    }
    const logout = () => {
        console.log('logout')
        setToken(null)
        localStorage.removeItem(STORAGE)
    }

    useEffect(() => {
        const token = JSON.parse(localStorage.getItem(STORAGE))
        if (!!token) {
            request('/auth/jwt/refresh/', 'POST', {'refresh': token.refresh})
                .then(data => login({access: data.access, refresh: token.refresh}))
                .catch(() => logout())
        }

    }, [request])

    return { login, logout, token }
}

export const useAuth = (token) => {
    const {load, request} = useHttp()

    const internal_request = useCallback(async (url, method = 'GET', body = null, headers = {}) => {
        headers['Authorization'] = 'Bearer ' + token.access
        return await request(url, method, body, headers)
    }, [request, token])

    return { request: internal_request, load }
}
