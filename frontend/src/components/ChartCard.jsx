import {
    Card,
    CardHeader,
    CardTitle,
    CardContent,
} from "./ui/card";

function ChartCard({ title, children }) {
    return (
        <Card className="mt-8">

            <CardHeader>
                <CardTitle className="text-slate-900">
                    {title}
                </CardTitle>
            </CardHeader>

            <CardContent>

                <div className="h-72 flex items-center justify-center text-slate-400">

                    {children}

                </div>

            </CardContent>

        </Card>
    );
}

export default ChartCard;