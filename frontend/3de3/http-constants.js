import axios from 'axios'

let baseURL

if (!process.env.NODE_ENV || process.env.NODE_ENV === 'development') {
  baseURL = 'http://localhost:8000'
} else {
  baseURL = 'http://api.3de3.gt'
}

export const HTTP = axios.create( {
  baseURL: baseURL, 
  withCredentials: true
})
