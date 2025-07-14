import yaml

if __name__ == "__main__":
    with open("yaml_file.yaml") as f:
        template =yaml.safe_load(f)

    print(template)