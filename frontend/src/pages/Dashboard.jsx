import { useEffect, useState } from "react";
import { getLatestMetrics, getAnomaly } from "../services/api";
import MetricsGrid from "../components/MetricsGrid";
import Layout from "../components/Layout";
import HeroStatus from "../components/HeroStatus";
import ChartCard from "../components/ChartCard";
import CpuChart from "../components/CpuChart";
import ResourceChart from "../components/ResourceChart";
import HistoryTable from "../components/HistoryTable";

function Dashboard() {
    const [metrics, setMetrics] = useState(null);
    const [prediction, setPrediction] = useState(null);
    const [history, setHistory] = useState([]);

    async function loadMetrics() {

        const metricData = await getLatestMetrics();
    
        const anomalyData = await getAnomaly();
    
        setMetrics(metricData);
    
        setPrediction(anomalyData.prediction);
    
        setHistory(prev => {
    
            const next = [
                ...prev,
                {
                    time: new Date().toLocaleTimeString([], {
                        hour: "2-digit",
                        minute: "2-digit",
                        second: "2-digit",
                    }),
    
                    cpu: metricData.cpu_percent,
                    memory: metricData.memory_percent,
                    disk: metricData.disk_percent,
    
                    prediction: anomalyData.prediction,
                }
            ];
    
            return next.slice(-12);
    
        });
    
    }


    useEffect(() => {
        loadMetrics();

        const interval = setInterval(() => {
            loadMetrics();
        }, 5000);
    
        return () => clearInterval(interval);

    }, []);

    if (!metrics) {
        return <h1>Loading...</h1>;
    }


    return (
        <Layout>

        <HeroStatus prediction={prediction} />

          
              
          <MetricsGrid metrics={metrics} />  


          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">

    <ChartCard title="CPU Trend">

    <CpuChart history={history} />

    </ChartCard>

    <ChartCard title="Resource Overview">

    <ResourceChart metrics={metrics} />

    </ChartCard>

      </div>

      <HistoryTable history={history} />
          
      </Layout>
  );
}

export default Dashboard;