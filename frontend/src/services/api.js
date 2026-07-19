import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

export const getLatestMetrics = async () => {
    const response = await api.get("/metrics/latest");
    return response.data;
};

export const getRecentMetrics = async () => {
    const response = await api.get("/metrics?limit=100");
    return response.data;
};

export const getAnomaly = async () => {
    const response = await api.get("/anomaly");
    return response.data;
};