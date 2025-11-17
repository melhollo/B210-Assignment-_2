def aggregate_by_occupation(input_csv_path, output_csv_path):
    import csv
    from collections import defaultdict

    occupation_data = defaultdict(lambda: {
        'total_sleep_duration': 0,
        'total_sleep_quality': 0,
        'total_stress_level': 0,
        'count': 0
    })

    with open(input_csv_path, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            occupation = row['Occupation']
            sleep_duration = float(row['Sleep Duration'])
            sleep_quality = float(row['Sleep Quality'])
            stress_level = float(row['Stress Level'])

            occupation_data[occupation]['total_sleep_duration'] += sleep_duration
            occupation_data[occupation]['total_sleep_quality'] += sleep_quality
            occupation_data[occupation]['total_stress_level'] += stress_level
            occupation_data[occupation]['count'] += 1

    with open(output_csv_path, mode='w', newline='') as outfile:
        fieldnames = ['Occupation', 'Average Sleep Duration', 'Average Sleep Quality', 'Average Stress Level', 'Count']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for occ, data in occupation_data.items():
            count = data['count']
            avg_sleep = round(data['total_sleep_duration'] / count, 2)
            avg_quality = round(data['total_sleep_quality'] / count, 2)
            avg_stress = round(data['total_stress_level'] / count, 2)
            writer.writerow({
                'Occupation': occ,
                'Average Sleep Duration': avg_sleep,
                'Average Sleep Quality': avg_quality,
                'Average Stress Level': avg_stress,
                'Count': count })