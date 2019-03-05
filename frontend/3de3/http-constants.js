import axios from 'axios'

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
if (localStorage.getItem('token')) {
  HTTP.defaults.headers.common['Authorization'] = `JWT `+localStorage.getItem('t');
}
else {
  this.$store.dispatch('nullSession');
}
export {
  HTTP,
  baseURL
}

