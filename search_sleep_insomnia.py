def get_condition_menu():
    return [
        {
            'name': 'search_sleep_insomnia',
            'display_name': 'Search Sleep/Insomnia',
            'description': 'Count unique participants with sleep apnea and/or insomnia from text columns in a spreadsheet.',
            'type': 'script',
            'script_path': 'search_sleep_insomnia.py',
            'parameters': [
                {
                    'name': 'file',
                    'type': 'file',
                    'required': True,
                    'description': 'Input data file (.csv, .tsv, .xlsx/.xls, .json)'
                },
                {
                    'name': 'columns',
                    'type': 'string',
                    'required': False,
                    'description': 'Comma-separated list of text columns to search (default: common medical history columns)'
                },
                {
                    'name': 'id_column',
                    'type': 'string',
                    'required': False,
                    'description': 'Column name containing participant id (if not provided, counts rows instead of unique participants)'
                }
            ]
        }
    ]