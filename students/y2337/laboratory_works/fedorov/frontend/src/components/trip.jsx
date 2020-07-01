import React, {useContext, useEffect, useState} from "react";
import {useHistory} from 'react-router-dom';
import {useAuth} from "../hooks/auth.hook";
import {AuthContext} from "../context/auth";

const EndTrip = (props) => {
    return (
        <div>
            <h1>Хорошей дороги!</h1>
            <a href={'/car/' + props.car.pk}>автомобиль</a>
            <p>Тариф: {props.car.price}</p>
            <button type="button" className="btn btn-primary" onClick={props.handler}>Пpиехали!</button>
        </div>
    )
}

const Trip = () => {
    const [inTrip, change] = useState(false)
    const [car, setCar] = useState({name: "Самая комфортная", price: "Самя выгодная"})
    const auth = useContext(AuthContext)
    const {request} = useAuth(auth.token)

    useEffect(() => {
        request('/api/trip/start/')
            .then(data => setCar(data))
            .catch((e) => {
                console.log(e)
            })
    }, [request])

    const gohandler = () => {
        request('/api/trip/start/', 'POST', car)
            .then(() => change(true))
            .catch((e) => {
                console.log(e)
                alert('Ошибка')
            })
    }

    const finishhandler = () => {
        request('/api/trip/finish/', 'POST')
            .then(() => change(false))
            .catch((e) => {
                console.log(e)
                alert('Ошибка')
            })
    }

    if (!inTrip) {
        return (
         <div>
            <h1>{car.name}</h1>
            <p>Цена: {car.price}</p>
            <button type="button" className="btn btn-primary" onClick={gohandler}>Поехали!</button>
            <button type="button" className="btn btn-info ml-5" onClick={finishhandler}>Завершить предыдущие поездки!</button>
         </div>
        )
    } else {
       return (<EndTrip car={car} handler={finishhandler}/>)
    }
}

export default Trip;
