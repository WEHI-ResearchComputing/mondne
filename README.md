# Mondne

## Installation

```
pip install git+https://github.com/WEHI-ResearchComputing/mondne.git
```

## Usage

For example, creating a new item (task) in Monday:
```python
from mondne import Client
from mondne.custom_mutations import Mutation

client = Client(url=YOUR_API_URL, headers={"Authorization": YOUR_API_TOKEN})
await client.mutation(Mutation.create_item(
    board_id=...,
    group_id=...,
    item_name=...,
    column_values={
        ...
    }
).fields(
    ItemFields.id,
), operation_name="create_item")
```
