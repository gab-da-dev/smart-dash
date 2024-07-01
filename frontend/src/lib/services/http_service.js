// httpClient.js
import axios from "axios";

const BASE_URL = "http://localhost:8000/";

const getRequest = (endpoint) => {
  return axios
    .get(`${BASE_URL}${endpoint}`)
    .then((response) => response.data)
    .catch((error) => {
      console.error("Axios GET request failed:", error);
    });
};

const postRequest = (endpoint, data, headers) => {
  return axios
    .post(`${BASE_URL}${endpoint}`, data, {
      headers: headers,
    })
    .then((response) => response.data)
    .catch((error) => {
      console.error("Axios POST request failed:", error);
    });
};

const putRequest = (endpoint, data) => {
  return axios
    .put(`${BASE_URL}${endpoint}`, data)
    .then((response) => response.data)
    .catch((error) => {
      console.error("Axios PUT request failed:", error);
    });
};

const deleteRequest = (endpoint) => {
  return axios
    .delete(`${BASE_URL}${endpoint}`)
    .then((response) => {
      console.log("Resource deleted");
    })
    .catch((error) => {
      console.error("Axios DELETE request failed:", error);
    });
};

const patchRequest = (endpoint, data) => {
  return axios
    .patch(`${BASE_URL}${endpoint}`, data)
    .then((response) => response.data)
    .catch((error) => {
      console.error("Axios PATCH request failed:", error);
    });
};

export { getRequest, postRequest, putRequest, deleteRequest, patchRequest };
