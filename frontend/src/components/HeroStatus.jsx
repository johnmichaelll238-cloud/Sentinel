import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

function HeroStatus({ prediction }) {

    const healthy = prediction === 1;

    return (
        <div className="mb-8 w-full">

            <h1 className="text-4xl font-bold text-slate-900">
                SENTINEL
            </h1>

            <p className="text-slate-400 mt-1 mb-6">
                Intelligent Infrastructure Monitoring
            </p>

            <div className="max-w-2xl">

            <Card className="bg-slate-900 border-slate-800 rounded-[28px] shadow-xl max-w-xl">

            <CardContent className="p-8">

                    <h2 className="text-2xl font-semibold text-white mb-4">
                        AI Assessment
                    </h2>

                    <Badge
                        className={
                            healthy
                                 ? "bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 rounded-full px-4 py-1"
                                 : "bg-red-500/20 text-red-400 border border-red-500/30 rounded-full px-4 py-1"
                        }
                    >
                        {healthy ? "Healthy" : "Anomaly"}
                    </Badge>

                    <p className="text-slate-400 mt-4">
                        {healthy
                            ? "No abnormal behaviour detected."
                            : "Sentinel detected abnormal system behaviour."}
                    </p>

                </CardContent>

            </Card>

            </div>

        </div>
    );
}

export default HeroStatus;