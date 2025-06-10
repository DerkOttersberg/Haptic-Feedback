import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Function to let the user select parameters


def select_parameters(options, param_type):
    print(f"\nAvailable {param_type} parameters:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    choices = input(
        f"Enter the numbers of the {param_type} parameters you want to use, separated by commas: ").strip()

    selected = []
    if choices:
        indices = [int(num.strip())
                   for num in choices.split(",") if num.strip().isdigit()]
        selected = [options[i - 1] for i in indices if 1 <= i <= len(options)]

    return selected if selected else options  # Default to all if none selected


def extract_data(file_list):
    # Initialize an empty list to collect data
    data = []
    # Load each JSON file specified
    for filename in file_list:
        filename = filename.strip().strip('"').strip("'")
        try:
            with open(filename, 'r') as file:
                entries = json.load(file)
                if isinstance(entries, list):
                    for entry in entries:
                        if entry.get("vr_latency", 0) <= 0 and entry.get("haptic_latency", 0) <= 0:
                            continue  # Skip entries with invalid latency values
                        cleaned_entry = {k: (v.strip() if isinstance(
                            v, str) else v) for k, v in entry.items()}
                        data.append(cleaned_entry)
                else:
                    if entries.get("vr_latency", 0) != 0 or entries.get("haptic_latency", 0) != 0:
                        cleaned_entry = {k: (v.strip() if isinstance(
                            v, str) else v) for k, v in entries.items()}
                        data.append(cleaned_entry)
        except Exception as e:
            print(f"Error loading {filename}: {e}")

    return data


def single_x_graph(df, x_axis_data, z_metrics):
    # Required columns check
    required_columns = {"testerId"}

    if not set(z_metrics).issubset(df.columns) or not set(x_axis_data).issubset(df.columns) or not required_columns.issubset(df.columns):
        print("Data does not contain all required columns:", required_columns)
    else:
        # Create subplots based on x-axis variables and y-metrics
        _, axes = plt.subplots(len(z_metrics), len(
            x_axis_data), figsize=(15, 10))
        for i, x_col in enumerate(x_axis_data):
            for j, y_col in enumerate(z_metrics):
                ax = axes[j, i] if len(x_axis_data) > 1 else axes[j]
                sns.scatterplot(data=df, x=x_col, y=y_col, hue="testerId",
                                palette="tab10", legend=False, ax=ax)
                for tester_id, group in df.groupby("testerId"):
                    ax.plot(group[x_col], group[y_col],
                            marker="o", label=f"User {tester_id}")
                ax.set_title(f"{y_col} vs {x_col}")
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                ax.legend()  # Ensure legend appears

        plt.tight_layout()
        plt.show()


def custom_extract(no_x, with_x, x, z, selected_x):

    # Extract data
    data_no_x = extract_data([no_x])
    data_with_x = extract_data([with_x])

    filtered_no_x = []
    filtered_with_x = []

    # Process no_x data (single X variable)
    for entry in data_no_x:
        # Keep only the selected X variable
        subdata = {selected_x: entry[selected_x]}
        for e in z:
            subdata[e] = entry.get(e)  # Add Z-metrics
        filtered_no_x.append(subdata)

    # Process with_x data (both X variables)
    for entry in data_with_x:
        subdata = {i: entry[i] for i in x}  # Keep both X variables
        for e in z:
            subdata[e] = entry.get(e)  # Add Z-metrics
        filtered_with_x.append(subdata)

    return pd.DataFrame(filtered_no_x), pd.DataFrame(filtered_with_x)

def custom_x_graph(df_no_x, df_with_x, x_axis_data, z_metrics, selected_x):
    """
    Plots comparison between datasets with and without an additional X-axis variable.

    Parameters:
    - df_no_x: DataFrame containing the dataset with only one X-axis variable
    - df_with_x: DataFrame containing the dataset with both X-axis variables
    - x_axis_data: List of X-axis variables
    - z_metrics: List of Z-metrics to compare
    """
    missing_x = x_axis_data[1] if selected_x == x_axis_data[0] else x_axis_data[0]

    if selected_x not in df_no_x.columns or selected_x not in df_with_x.columns:
        print(f"Error: Selected X-axis '{selected_x}' not found in data.")
        return

    # Create subplots for each Z-metric
    _, axes = plt.subplots(
        len(z_metrics), 1, figsize=(12, 5 * len(z_metrics)))

    if len(z_metrics) == 1:
        axes = [axes]  # Ensure axes is iterable for a single metric

    for i, z_metric in enumerate(z_metrics):
        ax = axes[i]

        # Scatter plots for each dataset
        sns.scatterplot(data=df_no_x, x=selected_x, y=z_metric,
                        marker="o", label="Without "+missing_x, ax=ax, color="blue")
        sns.scatterplot(data=df_with_x, x=selected_x, y=z_metric,
                        marker="s", label="With "+missing_x, ax=ax, color="red")

        # Function to add offset to the labels to avoid overlap
        def add_offset_to_labels(df, selected_x, z_metric, missing_x, ax, color, offset_step=-0.25):
            used_positions = set()  # Track used positions to check overlap
            for _, row in df.iterrows():
                # If the position is already used, add an offset
                x_val = row[selected_x]
                y_val = row[z_metric]
                offset = 0  # Start with no offset

                while (x_val, y_val + offset) in used_positions:
                    offset += offset_step  # Increase the offset step if overlap occurs

                # Annotate the point with the missing_x value
                ax.text(x_val, y_val + offset, f"{row[missing_x]:.2f}",
                        color=color, fontsize=9, ha="left", va="bottom")
                # Mark the position as used
                used_positions.add((x_val, y_val + offset))

        # Add offset annotations for missing_x
        add_offset_to_labels(df_with_x, selected_x, z_metric,
                             missing_x, ax, color="orange")

        # Connect points for each tester (if 'testerId' exists)
        if "testerId" in df_no_x.columns and "testerId" in df_with_x.columns:
            for tester_id in df_no_x["testerId"].unique():
                no_x_points = df_no_x[df_no_x["testerId"] == tester_id]
                with_x_points = df_with_x[df_with_x["testerId"] == tester_id]

                if not no_x_points.empty and not with_x_points.empty:
                    ax.plot([no_x_points[selected_x].values[0], with_x_points[selected_x].values[0]],
                            [no_x_points[z_metric].values[0],
                                with_x_points[z_metric].values[0]],
                            linestyle="dashed", color="gray", alpha=0.5)

        # Titles & labels
        ax.set_title(f"{z_metric} vs {selected_x}")
        ax.set_xlabel(selected_x)
        ax.set_ylabel(z_metric)
        ax.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Available options
    all_x_axis_options = ["vr_latency", "haptic_latency"]
    all_z_metrics = ["motionSickness", "taskPerformance",
                     "vr_usability", "haptic_accuracy", "haptic_responsiveness"]

    # Let user choose x-axis parameters
    x_axis_data = select_parameters(all_x_axis_options, "X-axis")
    # Let user choose z-metrics
    z_metrics = select_parameters(all_z_metrics, "Z-metric")

    # Prompt user to enter file names (comma-separated) and trim whitespace
    file_list = input(
        "Enter the JSON filenames (comma-separated): ").split(',')

    if len(x_axis_data) == 1:
        df = pd.DataFrame(extract_data(file_list))
        single_x_graph(df=df, x_axis_data=x_axis_data, z_metrics=z_metrics)
    elif len(x_axis_data) == 2:
        for i, entry in enumerate(x_axis_data):
            print(str(i)+': '+str(entry))
        selected_x = x_axis_data[int(
            input("Choose one X-axis variable by index: "))]

        df1, df2 = custom_extract(
            file_list[0], file_list[1], x=x_axis_data, z=z_metrics, selected_x=selected_x)
        custom_x_graph(df_no_x=df1, df_with_x=df2, x_axis_data=x_axis_data,
                       z_metrics=z_metrics, selected_x=selected_x)
