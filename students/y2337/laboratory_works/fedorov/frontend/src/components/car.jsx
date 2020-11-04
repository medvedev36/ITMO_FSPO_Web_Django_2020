import React, {useContext, useEffect, useState} from "react";
import {useHttp} from "../hooks/http.hook";
import {useAuth} from "../hooks/auth.hook";
import {AuthContext} from "../context/auth";

export const Car = (props) => {
    const [car, setCar] = useState({name: "Не найдена", price: "Выгодная", found: false})
    const http = useHttp().request
    const auth = useContext(AuthContext)
    const {request} = useAuth(auth.token)

    useEffect(() => {
        http('/api/car/' + props.match.params.id)
            .then(data => setCar({...data, found: true}))
            .catch(e => {
                alert('Ошибка')
                console.log(e)
            })

    }, [props.match.params.id, http, request])


    return (
        <div>
            <h1>{car.name}</h1>
            <p>Цена за минуту: {car.price}</p>
            {car.found && <a href={"/repair/" + car.pk}>Заметил поломку</a>}
        </div>
    )
}

