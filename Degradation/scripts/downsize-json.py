import json

def load_data_from_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

# Prepare datasets from JSON file
def downsize(filepath):
    data = load_data_from_json(filepath)
    datasets = {
        "total_latency_ms": [], "network_latency_ms": [],
        "client_frame_rate": [], "server_frame_rate": [], "bitrate_MBps": []
    }

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

    with open(input("Enter output filename: "), 'w') as output_file:
        json.dump(datasets, output_file, indent=4)



downsize(input("Please enter the full filePath: ").strip('"'))