import axios from 'axios';
import {logout} from "@/lib/auth.ts";

const api = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use(config => {
  const token = sessionStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

api.interceptors.response.use(
  (response) => response,
  (error) => {
    const requestUrl = error.config?.url;

    const isAuthRoute = requestUrl?.startsWith('/auth');

    if (!isAuthRoute && error.response?.status === 401) {
      logout();
      alert('Token expired. Please login again.');
    }

    return Promise.reject(error);
  }
);

export default api;
