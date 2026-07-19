import {
    ResponsiveContainer,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid,
} from "recharts";

function ResourceChart({ metrics }) {

    const data = [
        {
            name: "CPU",
            value: metrics.cpu_percent,
        },
        {
            name: "Memory",
            value: metrics.memory_percent,
        },
        {
            name: "Disk",
            value: metrics.disk_percent,
        },
    ];

    return (

        <ResponsiveContainer width="100%" height={260}>

            <BarChart data={data}>

                <CartesianGrid stroke="#e2e8f0" />

                <XAxis dataKey="name" />

                <YAxis domain={[0,100]} />

                <Tooltip />

                <Bar
                    dataKey="value"
                    fill="#06b6d4"
                    radius={[8,8,0,0]}
                />

            </BarChart>

        </ResponsiveContainer>

    );
}

export default ResourceChart;