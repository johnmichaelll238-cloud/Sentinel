import { Cpu, Memory, HardDrive } from "@phosphor-icons/react";
import {
    Card,
    CardHeader,
    CardTitle,
    CardContent,
} from "./ui/card";


function MetricCard({ title, value, unit }) {
    let Icon;

switch (title) {
    case "CPU":
        Icon = Cpu;
        break;
    case "Memory":
        Icon = Memory;
        break;
    case "Disk":
        Icon = HardDrive;
        break;
    default:
        Icon = Cpu;
}
return (
    <Card className="w-full bg-white border-0 rounded-xl shadow-sm hover:shadow-md transition-all duration-200">
        <CardHeader className="flex flex-row items-center gap-3">
            <Icon size={28} className="text-cyan-400" />
            <CardTitle>{title}</CardTitle>
        </CardHeader>

        <CardContent>
            <p className="text-4xl font-bold">
                {value}
                <span className="text-xl ml-1">{unit}</span>
            </p>
        </CardContent>
    </Card>
);
}

export default MetricCard;