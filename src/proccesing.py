def filter_by_state(data, state='executed'):
    return [item for item in data if item.get('state') == state]

def sort_by_date(list_of_dicts, reverse=True):
  return sorted(list_of_dicts, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)
