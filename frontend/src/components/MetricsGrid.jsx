import MetricCard from "./MetricCard";

function MetricsGrid({ metrics }) {
    return (
        <div className="grid w-full grid-cols-1 md:grid-cols-3 gap-6 mt-8">

            <MetricCard
                title="CPU USAGE"
                value={metrics.cpu_percent}
                unit="%"
            />

            <MetricCard
                title="MEMORY"
                value={metrics.memory_percent}
                unit="%"
            />

            <MetricCard
                title="DISK"
                value={metrics.disk_percent}
                unit="%"
            />

        </div>
    );
}

export default MetricsGrid;