import React, {useContext, useEffect, useState} from "react";
import {AuthContext} from "../context/auth";
import {useAuth} from "../hooks/auth.hook";

const History = () => {
    const auth = useContext(AuthContext)
    const {request} = useAuth(auth.token)
    const [history, setHisory] = useState([])

    useEffect(() => {
        request('/api/history/')
            .then(data => setHisory(data))
            .catch(() => {})
    }, [request])

    const renderHistory = (item) => {
        return (
            <div className="row">
                <div className="col">
                    <p>{item.car.name}</p>
                </div>
                <div className="col">
                    <p>{-item.transaction.delta}</p>
                </div>
                <div className="col">
                    <p>{item.transaction.time}</p>
                </div>
            </div>
        )
    }

    console.log(history)
    return (
        <div className="conatier my-5">
            <h2 className="my-3">История поездок</h2>
            <div className="row">
                <div className="col">
                    <p>Машина</p>
                </div>
                <div className="col">
                    <p>Цена</p>
                </div>
                <div className="col">
                    <p>Время поездки</p>
                </div>
            </div>
            {history.map((item, i) => renderHistory(item))}
        </div>
    )
}

export default History
