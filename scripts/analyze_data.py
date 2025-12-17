#!/usr/bin/env python3
import json
import statistics
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

def analyze_data(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    cluster_a = [p for p in data if p["cluster"] == "A"]
    cluster_b = [p for p in data if p["cluster"] == "B"]
    
    stats = {
        "total_points": len(data),
        "cluster_a_count": len(cluster_a),
        "cluster_b_count": len(cluster_b),
        "cluster_a_center_x": statistics.mean([p["x"] for p in cluster_a]) if cluster_a else 0,
        "cluster_a_center_y": statistics.mean([p["y"] for p in cluster_a]) if cluster_a else 0,
        "cluster_b_center_x": statistics.mean([p["x"] for p in cluster_b]) if cluster_b else 0,
        "cluster_b_center_y": statistics.mean([p["y"] for p in cluster_b]) if cluster_b else 0,
    }
    return data, stats

def create_scatter_plot(data, output_plot):
    x_a = [p["x"] for p in data if p["cluster"] == "A"]
    y_a = [p["y"] for p in data if p["cluster"] == "A"]
    x_b = [p["x"] for p in data if p["cluster"] == "B"]
    y_b = [p["y"] for p in data if p["cluster"] == "B"]
    
    plt.figure(figsize=(10, 6))
    plt.scatter(x_a, y_a, color='blue', alpha=0.6, label='Cluster A', s=50)
    plt.scatter(x_b, y_b, color='red', alpha=0.6, label='Cluster B', s=50)
    
    plt.title('Generated Data Distribution', fontsize=14)
    plt.xlabel('X Coordinate', fontsize=12)
    plt.ylabel('Y Coordinate', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_plot, dpi=150)
    plt.close()

def main():
    if len(sys.argv) < 3:
        print("Usage: python analyze_data.py <input_file> <output_report>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_report = sys.argv[2]
    
    # Fix: Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_report), exist_ok=True)
    
    # Fix: Use correct plot name - data_visualization.png
    output_plot = output_report.replace('.txt', '.png')
    if 'analysis_report' in output_plot:
        output_plot = output_plot.replace('analysis_report', 'data_visualization')
    
    data, stats = analyze_data(input_file)
    create_scatter_plot(data, output_plot)
    
    with open(output_report, 'w') as f:
        f.write("DATA ANALYSIS REPORT\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Total data points: {stats['total_points']}\n")
        f.write(f"Points in cluster A: {stats['cluster_a_count']}\n")
        f.write(f"Points in cluster B: {stats['cluster_b_count']}\n\n")
        f.write("Cluster centers:\n")
        f.write(f"  Cluster A: ({stats['cluster_a_center_x']:.2f}, {stats['cluster_a_center_y']:.2f})\n")
        f.write(f"  Cluster B: ({stats['cluster_b_center_x']:.2f}, {stats['cluster_b_center_y']:.2f})\n\n")
        f.write(f"Visualization saved: {output_plot}\n")
    
    print(f"Analysis completed!")
    print(f"Report saved: {output_report}")
    print(f"Plot saved: {output_plot}")

if __name__ == "__main__":
    main()
