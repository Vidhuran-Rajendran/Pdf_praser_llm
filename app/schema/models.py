def create_record(entity, attribute, value, unit=None, dimension=None):
    return {
        "entity": entity,
        "attribute": attribute,
        "value": value,
        "unit": unit,
        "dimension": dimension
    }
