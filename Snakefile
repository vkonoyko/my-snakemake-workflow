configfile: "config.yaml"

rule all:
    input:
        "output/final_report.txt",
        "output/data_visualization.png"

rule generate_data:
    output:
        "data/raw_data.json"
    params:
        num_points = config["num_points"]
    shell:
        "python scripts/generate_data.py {output}"

rule analyze_data:
    input:
        "data/raw_data.json"
    output:
        report = "output/analysis_report.txt",
        plot = "output/data_visualization.png"
    shell:
        "python scripts/analyze_data.py {input} {output.report}"

rule create_final_report:
    input:
        report = "output/analysis_report.txt",
        data = "data/raw_data.json"
    output:
        "output/final_report.txt"
    shell:
        """
        cat {input.report} > {output}
        echo "" >> {output}
        echo "==================================================" >> {output}
        echo "EXECUTION INFO" >> {output}
        echo "==================================================" >> {output}
        echo "Workflow: Snakemake" >> {output}
        echo "Time: $(date)" >> {output}
        echo "Author: vkonoyko" >> {output}
        """
