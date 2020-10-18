import axios from 'axios';

import { GET_MARKETS } from './types'


// GET MARKETS
export const getMarkets = () => dispatch => {
    axios
        .get('/api/categories/')
        .then(res => {
            dispatch({
                type: GET_MARKETS,
                payload: res.data
            });
        })
        .catch(err => console.log(err));
}