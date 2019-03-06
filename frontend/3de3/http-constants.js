import axios from 'axios'
import store from './src/store'

let baseURL

if (!process.env.NODE_ENV || process.env.NODE_ENV === 'development') {
  baseURL = 'http://localhost:8000'
} else {
  baseURL = 'http://api.3de3.gt'
}

const HTTP = axios.create( {
          baseURL: baseURL, 
          headers: {
            common: {
              Authorization: null,
            },
          },
          xsrfCookieName: 'csrftoken',
          xsrfHeaderName: 'X-CSRFToken',
          withCredentials: true
        })
if (localStorage.getItem('t')) {
  HTTP.defaults.headers.common['Authorization'] = `JWT `+localStorage.getItem('t');
}
else {
  store.dispatch('nullToken');
}
//if 401 error, null the token
HTTP.interceptors.response.use(function (response) {
    return response;
  }, function (error) {
    if (error.response.status == 401) {
      store.dispatch('nullToken');
      console.log('nullToken');
    } 
    return Promise.reject(error);
  });
//if there is no token, null whole Authorization header
HTTP.interceptors.request.use(function (config) {
    // if there is no token, delete header
    if (!localStorage.getItem('t')) 
      delete config.headers.common['Authorization'];
    return config;
  }, function (error) {
    // Do something with request error
    return Promise.reject(error);
  });
  
export {
  HTTP,
  baseURL
}

