import api from "@/lib/axios.ts";

export const getToken = async (username: string, password: string) => {
  try {
    const data = new URLSearchParams()
    data.append('grant_type', 'password')
    data.append('username', username)
    data.append('password', password)

    const response = await api.post('/auth/token', data, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    })

    sessionStorage.setItem('access_token', response.data.access_token);
    sessionStorage.setItem('username', username);

    return await response.data;
  } catch (error) {
    console.error(error)
    throw error;
  }
}

export const register = async (username: string, password: string) => {
  try {
    const response = await api.post('/auth/register/', {
      username,
      password,
    });

    return await response.data;
  } catch (error) {
    console.error(error)
    throw error;
  }
}

export const isAuthenticated = (): boolean => {
  return !!sessionStorage.getItem('access_token')
}

export const logout = () => {
  sessionStorage.removeItem('access_token');
  sessionStorage.removeItem('username');
  window.location.href = '/login';
}
