import React, {useContext, useEffect, useState} from "react";
import {AuthContext} from "../context/auth";
import {useAuth} from "../hooks/auth.hook";

const Repair = (props) => {
    const [canRepair, setPermisttion] = useState(false)
    const auth = useContext(AuthContext)
    const {request} = useAuth(auth.token)

    const url = '/api/repair/' + props.match.params.id

    useEffect(() => {
        request(url)
            .then(() => setPermisttion(true))
            .catch(() => setPermisttion(false))
    }, [request, url])

    const repair = () => {
        request(url, 'POST')
            .then(() => { setPermisttion(false) })
            .catch(() => { setPermisttion(true) })
    }

    if (canRepair) {
        return (
            <div>
                <h1>Починить машину {props.match.params.id}</h1>
                <button type="submit" className="btn btn-primary ml-2" onClick={repair}>Починить</button>
            </div>
        )
    } else {
        return <p>Не требует починки</p>
    }
}

export default Repair
