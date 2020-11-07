import Types from "./types";
import axios from "axios";

export const getPosts = () => {
    return dispatch => {
        dispatch({type:Types.POSTS_LOADING, payload:true})
        axios.get('http://localhost:8000/api/posts/')
            .then(response => {
                    dispatch({type:Types.GET_POSTS, payload:response.data})
                }
            )
            .catch(err => {
                    console.log(err)
                    dispatch({type:Types.POSTS_LOADING, payload:false})
                }
            );
    }
}

export const deletePost = (id,cb) => {
    return dispatch => {
        dispatch({type:Types.POSTS_LOADING, payload:true})
        console.log(id)
                console.log(id)
                        console.log(id)
                                console.log(id)
                                        console.log(id)
                                                console.log(id)
                                                        console.log(id)
                                                                console.log(id)
        axios.delete(`http://localhost:8000/api/posts/${id}`)
            .then(response => {
                    dispatch({type:Types.DELETE_POST, payload:id});
                    cb();
                }
            )
            .catch(err => {
                    console.log(err)
                }
            );
    }
}

export const createPost = (data,cb) => {
    return dispatch => {
        axios.post('http://localhost:8000/api/posts/', data)
            .then(response => {
                    console.log(response)
                    dispatch({type:Types.CREATE_POST, payload:response.data});
                    cb()
                }
            )
            .catch(err => {
                    console.log(err)
                    dispatch({type:Types.POSTS_LOADING, payload:false})
                }
            );
    }
}
