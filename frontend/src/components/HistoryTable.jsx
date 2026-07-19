import {
    Card,
    CardHeader,
    CardTitle,
    CardContent,
} from "./ui/card";

function HistoryTable({ history }) {

    return (

        <Card className="mt-8">

            <CardHeader>

                <CardTitle className="text-slate-900">
                    Recent System Activity
                </CardTitle>

            </CardHeader>

            <CardContent>

                <table className="w-full">

                    <thead className="text-slate-500 uppercase tracking-wide text-xs">

                        <tr className="text-slate-500 text-left border-b">

                            <th className="pb-3">Time</th>
                            <th>CPU</th>
                            <th>Memory</th>
                            <th>Disk</th>
                            <th>Status</th>

                        </tr>

                    </thead>

                    <tbody>

                        {history.slice().reverse().map((item, index) => (

                            <tr
                                key={index}
                                 className="border-b border-slate-100 hover:bg-slate-50 transition-colors h-14"
                            >

                                <td>{item.time}</td>

                                <td>{item.cpu}%</td>

                                <td>{item.memory}%</td>

                                <td>{item.disk}%</td>

                                <td>

                                {item.prediction === 1
                                    ? "🟢 Healthy"
                                    : "🔴 Anomaly"}

                                </td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            </CardContent>

        </Card>

    );

}

export default HistoryTable;