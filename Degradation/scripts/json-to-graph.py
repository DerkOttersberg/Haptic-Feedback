import json
from bokeh.plotting import figure, show
from bokeh.layouts import column, row
from bokeh.models import HoverTool, ColumnDataSource
import numpy as np

# Function to load data from JSON file
def load_data_from_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


# Downsize function
def downsize_data(data, target_size=None):
    if target_size and len(data) > target_size:
        bucket_size = len(data) // target_size
        return [np.mean(data[i * bucket_size:(i + 1) * bucket_size]) for i in range(target_size)]
    return data  # No downsizing needed


# Cap values to limit outliers
def cap_values(data, cap):
    return [min(value, cap) for value in data] if cap is not None else data


# Bin and smooth data for correlation graphs
def bin_and_smooth_data(latency_data, other_data, bin_size, bin_unit="ms"):
    if bin_unit == "KB":
        bin_size /= 1024  # Convert to MB if necessary

    sorted_pairs = sorted(zip(latency_data, other_data))
    sorted_latency, sorted_other = zip(*sorted_pairs)
    latency_bins = np.arange(0, max(sorted_latency) + bin_size, bin_size)
    binned_latency, binned_other = [], []

    for i in range(len(latency_bins) - 1):
        bin_start, bin_end = latency_bins[i], latency_bins[i + 1]
        values_in_bin = [sorted_other[j] for j in range(len(sorted_latency))
                         if bin_start <= sorted_latency[j] < bin_end]
        if values_in_bin:
            binned_other.append(np.mean(values_in_bin))
            binned_latency.append((bin_start + bin_end) / 2)

    return binned_latency, binned_other


# Plotting function for time-based and correlation graphs
def plot_data(latency, other_data, y_label, title):
    source = ColumnDataSource(data=dict(latency=latency, other=other_data))
    plot = figure(title=title, x_axis_label="Network Latency (ms)",
                  y_axis_label=y_label, width=600, height=400)
    plot.line('latency', 'other', source=source, line_width=2, color="blue")
    plot.scatter('latency', 'other', source=source,
                 size=5, color="blue", alpha=0.6)

    hover_tool = HoverTool(
        tooltips=[("Network Latency (ms)", "@latency"), (y_label, "@other")], mode="vline")
    plot.add_tools(hover_tool)
    return plot


# Prepare datasets from JSON file
def prepare_datasets(filepath):
    data = load_data_from_json(filepath)
    datasets = {
            "total_latency_ms": [], "network_latency_ms": [],
            "client_frame_rate": [], "server_frame_rate": [], "bitrate_MBps": []
        }
    if input("Enter 1 for raw data and 2 for downsized data upload: ") == "2":
        datasets["total_latency_ms"] = data.get("total_latency_ms", [])
        datasets["network_latency_ms"] = data.get("network_latency_ms", [])
        datasets["client_frame_rate"] = data.get("client_frame_rate", [])
        datasets["server_frame_rate"] = data.get("server_frame_rate", [])
        datasets["bitrate_MBps"] = data.get("bitrate_MBps", [])
    else:
        for entry in data:
            event_data = entry['event_type']['data']
            if entry['event_type']['id'] == "GraphStatistics":
                datasets["total_latency_ms"].append(
                    event_data['total_pipeline_latency_s'] * 1000)
                datasets["network_latency_ms"].append(
                    event_data['network_s'] * 1000)
                datasets["client_frame_rate"].append(event_data['client_fps'])
                datasets["server_frame_rate"].append(event_data['server_fps'])
                datasets["bitrate_MBps"].append(
                    event_data['actual_bitrate_bps'] / (1024**2))

    return datasets

# Default processing steps for both time-based and correlation graphs
def default_processing(datasets):
    total_latency_ms = downsize_data(datasets["total_latency_ms"], 1000)
    network_latency_ms = downsize_data(datasets["network_latency_ms"], 1000)
    client_frame_rate = downsize_data(datasets["client_frame_rate"], 1000)
    server_frame_rate = downsize_data(datasets["server_frame_rate"], 1000)
    bitrate_MBps = downsize_data(cap_values(
        datasets["bitrate_MBps"], 2000), 1000)
    time_index = list(range(len(datasets["total_latency_ms"])))

    latency_source = ColumnDataSource(data=dict(
        x=time_index, total_latency=total_latency_ms, network_latency=network_latency_ms))
    fps_source = ColumnDataSource(data=dict(
        x=time_index, client_fps=client_frame_rate, server_fps=server_frame_rate))
    bitrate_source = ColumnDataSource(
        data=dict(x=time_index, bitrate=bitrate_MBps))

    latency_figure = figure(title="Total and Network Latency Over Time",
                            x_axis_label="Time Index", y_axis_label="Latency (ms)", width=600, height=400)
    latency_figure.line('x', 'total_latency', source=latency_source,
                        legend_label="Total Latency", line_width=2)
    latency_figure.line('x', 'network_latency', source=latency_source,
                        legend_label="Network Latency", line_color="green", line_width=2)
    latency_figure.add_tools(HoverTool(tooltips=[("Total Latency (ms)", "@total_latency"), (
        "Network Latency (ms)", "@network_latency")], mode="vline", renderers=[latency_figure.renderers[0]]))

    fps_figure = figure(title="Client and Server Frame Rate Over Time",
                        x_axis_label="Time Index", y_axis_label="FPS", width=600, height=400)
    fps_figure.line('x', 'client_fps', source=fps_source,
                    legend_label="Client FPS", line_width=2)
    fps_figure.line('x', 'server_fps', source=fps_source,
                    legend_label="Server FPS", line_color="green", line_width=2)
    fps_figure.add_tools(HoverTool(tooltips=[(
        "Client FPS", "@client_fps"), ("Server FPS", "@server_fps")], mode="vline", renderers=[fps_figure.renderers[0]]))

    bitrate_figure = figure(title="Bitrate Over Time", x_axis_label="Time Index",
                            y_axis_label="Bitrate (MBps)", width=600, height=400)
    bitrate_figure.line('x', 'bitrate', source=bitrate_source,
                        legend_label="Bitrate", line_width=2)
    bitrate_figure.add_tools(
        HoverTool(tooltips=[("Bitrate (MBps)", "@bitrate")], mode="vline"))

    # Call combination_graphs() to get the correlation plots
    plots = combination_graphs(datasets)

    return column(row(latency_figure, fps_figure, bitrate_figure), row(*plots))


def combination_graphs(datasets):
    default_steps = [
        {"use_index_as_time": False, "latency_data": "network_latency_ms", "other_data": "client_frame_rate",
         "latency_cap": None, "other_cap": None, "sample_size": None, "bin_size": 5, "bin_unit": "ms"},
        {"use_index_as_time": False, "latency_data": "network_latency_ms", "other_data": "bitrate_MBps",
         "latency_cap": None, "other_cap": 10, "sample_size": None, "bin_size": 5, "bin_unit": "ms"}
    ]

    plots = []
    for step in default_steps:
        # Use integer index as time axis if specified
        if step.get("use_index_as_time", False):
            latency_data = list(range(len(datasets[step["other_data"]])))
        else:
            latency_data = cap_values(
                datasets[step["latency_data"]], step["latency_cap"])

        other_data = cap_values(
            datasets[step["other_data"]], step["other_cap"])

        # Apply downsizing if needed
        latency_data = downsize_data(latency_data, step["sample_size"])
        other_data = downsize_data(other_data, step["sample_size"])

        # Bin and smooth data
        binned_latency, binned_other = bin_and_smooth_data(
            latency_data, other_data, step["bin_size"], step["bin_unit"])

        # Generate plot
        y_label = step["other_data"].replace('_', ' ').title()
        title = f"{y_label} vs {'Index' if step.get('use_index_as_time', False) else 'Network Latency'}"
        plot = plot_data(binned_latency, binned_other, y_label, title)
        plots.append(plot)

    return plots


def custom_graphs():
    datasets = prepare_datasets(filename)

    print("\nAvailable datasets:")
    for i, key in enumerate(datasets.keys()):
        print(f"{i+1}. {key}")

    plots = []
    while True:
        use_index_as_time = input(
            "\nDo you want to use an integer index as the time axis? (y/n): ").strip().lower()

        if use_index_as_time == 'y':
            latency_data = list(
                range(len(next(iter(datasets.values())))))  # Integer index
            print("Using integer index as time axis.")
        else:
            lat_idx = int(
                input("Select the dataset index for latency data: ")) - 1
            latency_data = list(datasets.values())[lat_idx]

        other_idx = int(
            input("Select the dataset index for other data (e.g., FPS, bitrate): ")) - 1
        other_data = list(datasets.values())[other_idx]

        # Optional cap for latency and other data
        latency_cap = input(
            f"Enter a cap for {list(datasets.keys())[lat_idx]} (or press Enter to skip): ")
        other_cap = input(
            f"Enter a cap for {list(datasets.keys())[other_idx]} (or press Enter to skip): ")
        latency_cap = float(latency_cap) if latency_cap else None
        other_cap = float(other_cap) if other_cap else None

        # Apply capping
        latency_data = cap_values(latency_data, latency_cap)
        other_data = cap_values(other_data, other_cap)

        # Optional downsizing
        sample_size = input(
            "Enter the sample size for downsizing (or press Enter to skip): ")
        sample_size = int(sample_size) if sample_size else None
        latency_data = downsize_data(latency_data, sample_size)
        other_data = downsize_data(other_data, sample_size)

        # Bin size and unit
        bin_size = float(
            input("Enter the bin size (e.g., 5 for ms, or 200 for KB): "))
        bin_unit = input(
            "Enter the unit for bin size (ms, KB, MB): ").strip().upper()

        # Bin and smooth data
        binned_latency, binned_other = bin_and_smooth_data(
            latency_data, other_data, bin_size, bin_unit)

        y_label = list(datasets.keys())[other_idx]
        title = f"{y_label.replace('_', ' ').title()} vs Network Latency"
        plot = plot_data(binned_latency, binned_other, y_label, title)
        plots.append(plot)

        more_plots = input(
            "Do you want to create another plot? (y/n): ").strip().lower()
        if more_plots != 'y':
            break

    show(column(*plots))


# Main execution block
filename = input("Enter the path to the JSON data file: ").replace(
    '"', '').replace("'", "")

try:
    datasets = prepare_datasets(filename)
    if input("\nDo you want to use the default processing steps? (y/n): ").strip().lower() == 'y':
        show(default_processing(datasets))
    else:
        custom_graphs()

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except json.JSONDecodeError as e:
    print("JSON Decode Error:", e)
    print("Error Position:", f"Line {e.lineno}, Column {e.colno}")
