#!/usr/bin/env python3
import random
import json
import sys

def generate_sample_data(num_points=50):
    data = []
    for i in range(num_points):
        if i < num_points // 2:
            x = random.gauss(1.0, 0.3)
            y = random.gauss(1.0, 0.3)
            cluster = "A"
        else:
            x = random.gauss(4.0, 0.3)
            y = random.gauss(4.0, 0.3)
            cluster = "B"
        
        point = {
            "id": i + 1,
            "x": round(x, 2),
            "y": round(y, 2),
            "cluster": cluster
        }
        data.append(point)
    return data

def main():
    data = generate_sample_data()
    output_file = sys.argv[1] if len(sys.argv) > 1 else "data/raw_data.json"
    
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Generated {len(data)} data points")
    print(f"Data saved to: {output_file}")

if __name__ == "__main__":
    main()
