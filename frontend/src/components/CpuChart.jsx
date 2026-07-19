import {
    ResponsiveContainer,
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid,
} from "recharts";

function CpuChart({ history }) {

    return (

        <ResponsiveContainer width="100%" height={260}>

            <LineChart data={history}>

                <CartesianGrid stroke="#e2e8f0" />

                <XAxis dataKey="time" />

                <YAxis domain={[0,100]} />

                <Tooltip />

                <Line
                    type="monotone"
                    dataKey="cpu"
                    stroke="#06b6d4"
                    strokeWidth={3}
                    dot={false}
                />

            </LineChart>

        </ResponsiveContainer>

    );

}

export default CpuChart;